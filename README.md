# RAG — Historia de México

Framework de retrieval-augmented generation (RAG) sobre un corpus de Wikipedia en
español (Historia de México), desarrollado como parte del proyecto de tesis
*Sistemas de Retrieval para Agentes de Datos* (Maestría en Ciencia de Datos,
UNISON / PhiQus).

Incluye dos cosas:

1. **`rag_ollama.py`** — el baseline de Fase 0: un script único (chunking →
   embeddings → FAISS → Ollama) que corre por consola.
2. **`src/` + `demo_app.py`** — la arquitectura de Fase 1 (Proposal 2 del RFC):
   componentes intercambiables detrás de interfaces (`BaseChunker`,
   `BaseRetriever`, `BasePostprocessor`, `BaseGenerator`) con dos retrievers
   ya implementados (Cosine/FAISS y BM25), y un demo en Streamlit que los
   compara en vivo sobre la misma pregunta.

## Estructura del repo

```
rag_ollama.py           # Baseline Fase 0 (script único, interactivo por consola)
src/                     # Arquitectura Proposal 2 (interfaces + implementaciones)
configs/                 # cosine.yaml / bm25.yaml — qué retriever usa cada pipeline
demo_app.py              # Demo Streamlit: compara Cosine vs BM25 lado a lado
data/                    # Corpus descargado de Wikipedia (19 artículos, cacheado)
embeddings/              # Índice FAISS + metadata.json (chunks ya generados)
bm25_index/              # Índice BM25 (pickle, generado en el primer uso)
logs/                    # Logs de sesión (observabilidad: query, chunks, prompt, tiempos)
requirements_ollama.txt  # Dependencias del venv
```

## Requisitos previos

- **Python 3.11**
- **Ollama** instalado y corriendo — [ollama.com/download](https://ollama.com/download)
- El modelo `gemma3:12b` descargado:
  ```bash
  ollama pull gemma3:12b
  ```
  No se necesita GPU (corre en CPU; 32 GB de RAM recomendado). El repo también
  soporta `llama3.2` o `mistral` si quieres algo más rápido — se cambia en la
  variable `OLLAMA_MODEL` de `rag_ollama.py` o en el campo `ollama_model` de
  los YAML en `configs/`.

## Instalación

```bash
git clone https://github.com/Antonio-JFB/Rag-baseline.git
cd Rag-baseline
python -m venv venv
```

Activar el entorno virtual:

```powershell
# PowerShell
venv\Scripts\Activate.ps1
```
```
:: CMD
venv\Scripts\activate.bat
```

Instalar dependencias:

```bash
pip install -r requirements_ollama.txt
```

> Nota: la primera vez que corras cualquiera de los dos programas, se
> descarga el modelo de embeddings (`paraphrase-multilingual-MiniLM-L12-v2`,
> ~470 MB) desde Hugging Face. El corpus (`data/`) y el índice FAISS
> (`embeddings/`) ya vienen generados en el repo, así que no hace falta
> reconstruirlos.

## Opción 1 — Correr el baseline (Fase 0)

Script único, interactivo, por consola:

```bash
python rag_ollama.py
```

- Si ya existe un índice en `embeddings/`, pregunta si quieres reconstruirlo
  desde cero (`s`) o usar el que ya está (`N`, default — más rápido).
- Escribe una pregunta y presiona Enter. Escribe `salir` para terminar.
- Cada sesión se loguea completa en `logs/`.

## Opción 2 — Correr el demo (Proposal 2: Cosine vs BM25)

Compara en vivo dos métodos de retrieval intercambiables sobre el mismo
corpus y el mismo LLM.

```bash
streamlit run demo_app.py
```

Se abre automáticamente `http://localhost:8501`. Ahí:

1. Elige una pregunta sugerida o escribe la tuya.
2. Da clic en **Comparar**.
3. Espera — cada respuesta la genera Ollama en tiempo real, puede tardar
   entre 10 s y ~2 min dependiendo de la carga del equipo (gemma3:12b en CPU
   varía bastante). Precalentar el modelo con una pregunta de prueba antes de
   una presentación en vivo ayuda a que las siguientes respuestas salgan más
   rápido.
4. Verás lado a lado: chunks recuperados con score, tiempos, la respuesta
   generada, y el prompt completo enviado al LLM (expandible).

Para detenerlo: `Ctrl+C` en la terminal.

### Cambiar de configuración

Cada método de retrieval es un archivo YAML en `configs/`. Para agregar uno
nuevo (por ejemplo, otro modelo de Ollama) basta con copiar
`configs/cosine.yaml` o `configs/bm25.yaml` y ajustar los campos — no hay que
tocar el código del pipeline.

## Problemas comunes

- **`ModuleNotFoundError: No module named 'torchvision'` al correr el demo** —
  inofensivo. Es el vigilante de archivos de Streamlit inspeccionando
  submódulos de `transformers` que no usamos. Ya está silenciado vía
  `.streamlit/config.toml` (`fileWatcherType = "none"`); si vuelve a aparecer,
  revisa que ese archivo siga ahí.
- **El modelo no está descargado** — `rag_ollama.py` lo detecta al arrancar y
  te dice exactamente qué correr (`ollama pull <modelo>`).
- **Respuestas muy lentas o que se cortan** — normal en CPU sin GPU. El
  timeout del generador está en 240 s (`src/generators.py`); si necesitas
  algo más ágil para una demo en vivo, usa `llama3.2:3b` en vez de
  `gemma3:12b`.
