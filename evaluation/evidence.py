"""
evidence.py -- el corpus visto como ORACIONES con posicion en palabras.

Base del protocolo de evaluacion del experimento de PLN. La idea central es que la
evidencia relevante se marca sobre ORACIONES del corpus, no sobre chunks; asi la
anotacion no depende de como se segmente el texto y sirve para comparar chunkings
distintos (y, mas adelante, para el reranking de la tesis).

Convenciones (las mismas que los chunkers del framework):
  - 'palabra' = elemento de texto.split(); los offsets de un chunk (inicio_palabra,
    fin_palabra) son indices de palabra DENTRO del articulo.
  - Los articulos con contenido identico (mismo SHA-256) se tratan como UNO: el
    canonico es el de titulo mas largo. Un chunk del duplicado se proyecta al canonico
    (los offsets coinciden porque el texto es identico).
"""

import glob
import hashlib
import json
import os
import re
from dataclasses import dataclass

DATA_DIR = "data"

# Abreviaturas / iniciales tras las que un punto NO termina oracion.
ABBREVIATIONS = {
    "dr", "dra", "sr", "sra", "srta", "lic", "ing", "gral", "gen", "cnel", "col", "cap",
    "vs", "num", "pag", "aprox", "av", "ed", "vol", "tel", "fig", "no", "pp", "ca", "c",
    "a", "n", "e", "d", "s", "p", "h", "j", "m", "f", "l", "r", "t",
}
CLOSERS = "\"'”’»)]"
ZW = "​"          # marcador de nota al pie de Wikipedia pegado a la palabra anterior
HEADING_MAX_WORDS = 10


@dataclass(frozen=True)
class Sentence:
    sid: str            # id estable: "<articulo>#<inicio>-<fin>"
    articulo: str       # titulo canonico
    inicio: int         # indice de palabra (incluido)
    fin: int            # indice de palabra (excluido)
    texto: str
    es_titulo: bool     # encabezado de seccion, no una oracion


def titulo_de(path: str) -> str:
    """Mismo criterio de titulo que rag_ollama.py / load_corpus_chunks (el 'fuente' de un chunk)."""
    return os.path.basename(path).replace(".txt", "").replace("_", " ")


def sha256_file(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def corpus_manifest(data_dir: str = DATA_DIR) -> dict:
    """Inventario del corpus: hash, palabras, duplicados y articulos anomalos.
    Es la 'version de documentos' que pidio el revisor: fija exactamente que texto se evaluo."""
    arts, by_hash = [], {}
    for path in sorted(glob.glob(os.path.join(data_dir, "*.txt"))):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        h = sha256_file(path)
        entry = {"titulo": titulo_de(path), "archivo": os.path.basename(path),
                 "sha256": h, "palabras": len(text.split()), "bytes": os.path.getsize(path)}
        arts.append(entry)
        by_hash.setdefault(h, []).append(entry["titulo"])

    canonical, duplicates = {}, []
    for h, titles in by_hash.items():
        canon = max(titles, key=len)
        for t in titles:
            canonical[t] = canon
        if len(titles) > 1:
            duplicates.append({"sha256": h, "titulos": titles, "canonico": canon})

    for a in arts:
        a["canonico"] = canonical[a["titulo"]]
        a["anomalia"] = "muy corto (articulo casi vacio)" if a["palabras"] < 200 else ""
    return {"articulos": arts, "duplicados": duplicates,
            "articulos_unicos": len(by_hash), "palabras_unicas": sum(
                a["palabras"] for a in arts if a["titulo"] == a["canonico"])}


def canonical_map(data_dir: str = DATA_DIR) -> dict[str, str]:
    return {a["titulo"]: a["canonico"] for a in corpus_manifest(data_dir)["articulos"]}


def split_article(text: str, articulo: str) -> list[Sentence]:
    """Divide un articulo en oraciones con offsets de palabra.

    Fin de oracion: palabra que termina en . ! ? (posible cierre de comillas/parentesis)
    que no sea abreviatura ni inicial y cuya siguiente palabra no empiece en minuscula;
    o salto de linea (parrafo, encabezado, item de lista)."""
    matches = list(re.finditer(r"\S+", text))
    sents: list[Sentence] = []
    start = 0
    for i, m in enumerate(matches):
        last = i == len(matches) - 1
        cut = last
        if not last:
            gap = text[m.end():matches[i + 1].start()]
            if "\n" in gap:
                cut = True
            else:
                core = m.group().replace(ZW, "").rstrip(CLOSERS)
                if core and core[-1] in ".!?":
                    nxt = matches[i + 1].group().lstrip("\"'“‘¿¡([«")
                    stem = re.findall(r"(\w+)\.*$", core[:-1])
                    abbr = bool(stem) and core[-1] == "." and (
                        stem[-1].lower() in ABBREVIATIONS and len(stem[-1]) <= 4
                        or (len(stem[-1]) == 1 and stem[-1].isalpha())
                    )
                    if not abbr and not nxt[:1].islower():
                        cut = True
        if cut:
            words = [w.replace(ZW, "") for w in text[matches[start].start():m.end()].split()]
            body = " ".join(words).lstrip("# ").strip()
            n = i + 1 - start
            ends_punct = body.rstrip(CLOSERS)[-1:] in (".", "!", "?", ":")
            sents.append(Sentence(
                sid=f"{articulo}#{start}-{i + 1}", articulo=articulo, inicio=start, fin=i + 1,
                texto=body, es_titulo=(n <= HEADING_MAX_WORDS and not ends_punct),
            ))
            start = i + 1
    return sents


def load_sentences(data_dir: str = DATA_DIR) -> list[Sentence]:
    """Oraciones de TODOS los articulos unicos (los duplicados se omiten)."""
    man = corpus_manifest(data_dir)
    out: list[Sentence] = []
    for a in man["articulos"]:
        if a["titulo"] != a["canonico"]:
            continue
        with open(os.path.join(data_dir, a["archivo"]), "r", encoding="utf-8") as f:
            out.extend(split_article(f.read(), a["titulo"]))
    return out


def overlap_words(a0: int, a1: int, b0: int, b1: int) -> int:
    return max(0, min(a1, b1) - max(a0, b0))


class EvidenceIndex:
    """Proyecta chunks recuperados a oraciones y consulta la cobertura de evidencia."""

    def __init__(self, data_dir: str = DATA_DIR, min_cover: float = 0.5):
        self.canon = canonical_map(data_dir)
        self.sentences = load_sentences(data_dir)
        self.by_id = {s.sid: s for s in self.sentences}
        self.by_article: dict[str, list[Sentence]] = {}
        for s in self.sentences:
            self.by_article.setdefault(s.articulo, []).append(s)
        self.min_cover = min_cover

    def chunk_key(self, chunk: dict) -> tuple[str, int, int]:
        """Identidad de un chunk por contenido: (articulo canonico, inicio, fin). Dos chunks
        del articulo duplicado y del canonico en la misma posicion tienen la misma clave."""
        art = self.canon.get(chunk["fuente"], chunk["fuente"])
        return art, chunk["inicio_palabra"], chunk["fin_palabra"]

    def covered(self, chunk: dict, sid: str) -> bool:
        """El chunk 'cubre' la oracion si contiene >= min_cover de sus palabras."""
        s = self.by_id[sid]
        art, i0, i1 = self.chunk_key(chunk)
        if art != s.articulo:
            return False
        return overlap_words(i0, i1, s.inicio, s.fin) >= self.min_cover * (s.fin - s.inicio)

    def sentences_in(self, chunk: dict, only_body: bool = True) -> list[Sentence]:
        art, i0, i1 = self.chunk_key(chunk)
        out = []
        for s in self.by_article.get(art, []):
            if s.fin <= i0:
                continue
            if s.inicio >= i1:
                break
            if only_body and s.es_titulo:
                continue
            if overlap_words(i0, i1, s.inicio, s.fin) >= self.min_cover * (s.fin - s.inicio):
                out.append(s)
        return out


if __name__ == "__main__":
    man = corpus_manifest()
    print(json.dumps({k: v for k, v in man.items() if k != "articulos"}, ensure_ascii=False, indent=1))
    ss = load_sentences()
    body = [s for s in ss if not s.es_titulo]
    print(f"{len(ss)} unidades, {len(body)} oraciones (sin titulos); "
          f"palabras/oracion mediana={sorted(s.fin - s.inicio for s in body)[len(body) // 2]}")
