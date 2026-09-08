"""
RAG Baseline - Historia de México (Wikipedia)
Versión: Ollama (100% local y gratuito)
=============================================
Arquitectura:
  - Corpus    : Wikipedia en español (wikipedia-api)
  - Chunking  : ventana deslizante ~300 palabras con overlap de 50
  - Embeddings: sentence-transformers (paraphrase-multilingual-MiniLM-L12-v2)
  - Vector DB : FAISS IndexFlatIP (cosine similarity local)
  - LLM       : Ollama local (llama3.2:3b por defecto, 100% gratis y offline)
"""

import os
import json
import time
import logging
import requests
import numpy as np
import faiss
import wikipediaapi
from sentence_transformers import SentenceTransformer
from datetime import datetime

# ─── CONFIG ────────────────────────────────────────────────────────────────────

CHUNK_SIZE    = 300
CHUNK_OVERLAP = 50
TOP_K         = 5
MODEL_EMBED   = "paraphrase-multilingual-MiniLM-L12-v2"

# Modelo de Ollama — opciones recomendadas para 16 GB RAM:
#   llama3.2:3b   → más rápido (~2s respuesta), buen español
#   gemma3:4b     → mejor español, un poco más lento
#   mistral:7b    → más inteligente, requiere ~8 GB libres
OLLAMA_MODEL = "gemma3:12b"
OLLAMA_URL    = "http://localhost:11434/api/generate"

LOG_DIR       = "logs"
INDEX_PATH    = "embeddings/faiss.index"
META_PATH     = "embeddings/metadata.json"

ARTICULOS = [
    "Historia de México",
    "Imperio azteca",
    "Conquista de México",
    "Independencia de México",
    "Revolución mexicana",
    "Reforma (México)",
    "Virreinato de Nueva España",
    "Civilización maya",
    "Cultura olmeca",
    "Porfiriato",
    "Guerra de Reforma",
    "Emiliano Zapata",
    "Pancho Villa",
    "Miguel Hidalgo y Costilla",
    "Benito Juárez",
    "Moctezuma II",
    "Hernán Cortés",
    "Tenochtitlan",
    "Cultura teotihuacana",
    "Guerra de Independencia de México",
]

# ─── LOGGING ───────────────────────────────────────────────────────────────────

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs("embeddings", exist_ok=True)
os.makedirs("data", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(
            f"{LOG_DIR}/rag_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log",
            encoding="utf-8"
        ),
        logging.StreamHandler(),
    ]
)
log = logging.getLogger(__name__)


# ─── VERIFICAR OLLAMA ──────────────────────────────────────────────────────────

def verificar_ollama():
    """Comprueba que Ollama esté corriendo y el modelo esté disponible."""
    try:
        resp = requests.get("http://localhost:11434/api/tags", timeout=5)
        modelos = [m["name"] for m in resp.json().get("models", [])]
        log.info(f"Ollama activo. Modelos disponibles: {modelos}")

        # Buscar si el modelo configurado está (permite match parcial)
        modelo_base = OLLAMA_MODEL.split(":")[0]
        disponible = any(modelo_base in m for m in modelos)

        if not disponible:
            print(f"\n  El modelo '{OLLAMA_MODEL}' no está descargado.")
            print(f"   Corre en otra terminal:  ollama pull {OLLAMA_MODEL}")
            print(f"   Espera a que termine y vuelve a ejecutar este script.\n")
            return False
        return True

    except requests.exceptions.ConnectionError:
        print("\n  Ollama no está corriendo.")
        print("   1. Instala Ollama desde: https://ollama.com/download")
        print("   2. Ábrelo (en Mac aparece en la barra superior)")
        print(f"   3. Descarga el modelo: ollama pull {OLLAMA_MODEL}")
        print("   4. Vuelve a correr este script.\n")
        return False


# ─── PASO 1: DESCARGA DE CORPUS ────────────────────────────────────────────────

def descargar_corpus():
    """Descarga artículos de Wikipedia en español. Usa cache si ya existen."""
    log.info("=== PASO 1: Descargando corpus de Wikipedia ===")
    wiki = wikipediaapi.Wikipedia(
        language="es",
        user_agent="RAG-Baseline-Tesis/1.0"
    )
    descargados = []

    for titulo in ARTICULOS:
        path = f"data/{titulo.replace(' ', '_').replace('/', '-')}.txt"
        if os.path.exists(path):
            log.info(f"  [CACHE] {titulo}")
            descargados.append(path)
            continue

        pagina = wiki.page(titulo)
        if not pagina.exists():
            log.warning(f"  [SKIP]  No encontrado: {titulo}")
            continue

        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {pagina.title}\n\n{pagina.text}")

        log.info(f"  [OK]    {titulo} ({len(pagina.text):,} chars)")
        descargados.append(path)
        time.sleep(0.3)

    log.info(f"Corpus listo: {len(descargados)} artículos")
    return descargados


# ─── PASO 2: CHUNKING ──────────────────────────────────────────────────────────

def chunk_texto(texto, titulo):
    """
    Divide el texto en chunks de ~CHUNK_SIZE palabras con overlap.
    Limitación: puede cortar oraciones a la mitad.
    """
    palabras = texto.split()
    chunks = []
    inicio = 0

    while inicio < len(palabras):
        fin = min(inicio + CHUNK_SIZE, len(palabras))
        chunks.append({
            "id": f"{titulo}_{len(chunks):04d}",
            "texto": " ".join(palabras[inicio:fin]),
            "fuente": titulo,
            "inicio_palabra": inicio,
            "fin_palabra": fin,
            "num_palabras": fin - inicio,
        })
        if fin == len(palabras):
            break
        inicio += CHUNK_SIZE - CHUNK_OVERLAP

    return chunks


def construir_chunks(archivos):
    log.info("=== PASO 2: Construyendo chunks ===")
    todos_chunks = []
    for path in archivos:
        titulo = os.path.basename(path).replace(".txt", "").replace("_", " ")
        with open(path, "r", encoding="utf-8") as f:
            texto = f.read()
        chunks = chunk_texto(texto, titulo)
        todos_chunks.extend(chunks)
        log.info(f"  {titulo}: {len(chunks)} chunks")
    log.info(f"Total chunks: {len(todos_chunks)}")
    return todos_chunks


# ─── PASO 3: EMBEDDINGS + ÍNDICE FAISS ─────────────────────────────────────────

def construir_indice(chunks):
    """
    Genera embeddings locales y construye índice FAISS.
    Método: IndexFlatIP con vectores normalizados = cosine similarity exacta.
    """
    log.info(f"=== PASO 3: Generando embeddings con {MODEL_EMBED} ===")
    model = SentenceTransformer(MODEL_EMBED)
    textos = [c["texto"] for c in chunks]
    log.info(f"  Codificando {len(textos)} chunks... (1-2 min la primera vez)")

    embeddings = model.encode(
        textos,
        batch_size=32,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype(np.float32)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    log.info(f"  Índice guardado: {index.ntotal} vectores, dim={dim}")
    return index, chunks, model


def cargar_indice():
    log.info("=== Cargando índice existente desde disco ===")
    index = faiss.read_index(INDEX_PATH)
    with open(META_PATH, "r", encoding="utf-8") as f:
        chunks = json.load(f)
    model = SentenceTransformer(MODEL_EMBED)
    log.info(f"  Índice cargado: {index.ntotal} vectores")
    return index, chunks, model


# ─── PASO 4: RETRIEVAL ─────────────────────────────────────────────────────────

def recuperar(query, index, chunks, model, top_k=TOP_K):
    """
    Busca los top_k chunks más similares a la query.
    Limitación: sin reranking ni filtrado post-retrieval (baseline puro).
    """
    q_emb = model.encode(
        [query],
        normalize_embeddings=True,
        convert_to_numpy=True,
    ).astype(np.float32)

    scores, indices = index.search(q_emb, top_k)
    resultados = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0:
            continue
        resultados.append({"chunk": chunks[idx], "score": float(score)})
    return resultados


# ─── PASO 5: GENERACIÓN CON OLLAMA ─────────────────────────────────────────────

def generar_respuesta_ollama(query, resultados):
    """
    Llama a Ollama (API local) con el contexto recuperado.
    
    Trade-off vs API en la nube:
      + Gratis, offline, sin límites
      - Más lento, calidad variable según modelo
      - Requiere RAM (~4-8 GB según modelo)
    """
    partes = []
    for i, r in enumerate(resultados, 1):
        partes.append(
            f"[Fragmento {i} | Fuente: {r['chunk']['fuente']} | "
            f"Score: {r['score']:.3f}]\n{r['chunk']['texto']}"
        )
    contexto = "\n\n---\n\n".join(partes)
    log.info(f"PROMPT_ENVIADO:\n{prompt}")


    prompt = f"""Eres un asistente experto en historia de México.
Responde la pregunta ÚNICAMENTE usando los fragmentos de contexto.
Si la información no está en los fragmentos, di: "No encontré esta información en el corpus."
Al final indica qué fuentes usaste.

CONTEXTO:
{contexto}

PREGUNTA: {query}

RESPUESTA:"""

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,          # False = espera respuesta completa
        "options": {
            "temperature": 0.1,   # bajo para respuestas más factuales
            "num_predict": 800,   # máximo de tokens en respuesta
        }
    }

    try:
        resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
        resp.raise_for_status()
        return resp.json().get("response", "Error: respuesta vacía de Ollama")
    except requests.exceptions.Timeout:
        return "Error: Ollama tardó demasiado. Intenta con un modelo más pequeño."
    except Exception as e:
        return f"Error al llamar a Ollama: {e}"


# ─── OBSERVABILIDAD ────────────────────────────────────────────────────────────

def log_sesion(query, resultados, respuesta, t_retrieval, t_llm):
    log.info("=" * 70)
    log.info(f"QUERY     : {query}")
    log.info(f"RETRIEVAL : {t_retrieval:.3f}s | LLM: {t_llm:.3f}s | "
             f"Total: {t_retrieval+t_llm:.3f}s")
    log.info(f"CHUNKS RECUPERADOS ({len(resultados)}):")
    for i, r in enumerate(resultados, 1):
        c = r["chunk"]
        log.info(
            f"  [{i}] score={r['score']:.4f} | fuente={c['fuente']} | "
            f"palabras {c['inicio_palabra']}-{c['fin_palabra']}"
        )
        log.info(f"       preview: {c['texto'][:120].strip()}...")
    log.info(f"RESPUESTA:\n{respuesta}")
    log.info("=" * 70)


# ─── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    print("\n" + "=" * 60)
    print("  RAG BASELINE — Historia de México")
    print(f"  LLM: Ollama local ({OLLAMA_MODEL})")
    print("=" * 60)

    # Verificar que Ollama esté activo
    if not verificar_ollama():
        return

    # Construir o cargar índice
    if os.path.exists(INDEX_PATH) and os.path.exists(META_PATH):
        print("\n  Índice encontrado en disco.")
        print("    ¿Quieres reconstruirlo desde cero? (s/N): ", end="", flush=True)
        resp = input().strip().lower()
        if resp == "s":
            archivos = descargar_corpus()
            chunks   = construir_chunks(archivos)
            index, chunks, model = construir_indice(chunks)
        else:
            index, chunks, model = cargar_indice()
    else:
        print("\n  Primera ejecución — construyendo índice (~2 min)...")
        archivos = descargar_corpus()
        chunks   = construir_chunks(archivos)
        index, chunks, model = construir_indice(chunks)

    print(f"\n  Sistema listo — {index.ntotal} chunks indexados")
    print(f"    Modelo LLM: {OLLAMA_MODEL} (local)")
    print("    Escribe tu pregunta o 'salir' para terminar.\n")

    while True:
        print("─" * 60)
        try:
            query = input("  Pregunta: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n¡Hasta luego!")
            break

        if not query:
            continue
        if query.lower() in ("salir", "exit", "quit"):
            print("¡Hasta luego!")
            break

        t0 = time.time()

        # Retrieval
        resultados  = recuperar(query, index, chunks, model)
        t_retrieval = time.time() - t0

        print(f"\n  Chunks recuperados (retrieval: {t_retrieval:.2f}s):")
        for i, r in enumerate(resultados, 1):
            print(f"  [{i}] score={r['score']:.3f} | {r['chunk']['fuente']}")
            print(f"       \"{r['chunk']['texto'][:90].strip()}...\"")

        # Generación
        print(f"\n  Generando respuesta con {OLLAMA_MODEL}... (puede tardar ~10-30s)")
        t1        = time.time()
        respuesta = generar_respuesta_ollama(query, resultados)
        t_llm     = time.time() - t1

        print(f"\n  Respuesta (LLM: {t_llm:.2f}s):")
        print("─" * 40)
        print(respuesta)
        print("─" * 40)
        print(f"   Tiempo total: {t_retrieval + t_llm:.2f}s")

        log_sesion(query, resultados, respuesta, t_retrieval, t_llm)


if __name__ == "__main__":
    main()
