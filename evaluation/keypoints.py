"""
keypoints.py -- ayuda para localizar en el texto los puntos clave de una pregunta.

Es una AYUDA para el anotador, no un juez: un chunk puede mencionar un punto
clave sin ser relevante, o ser relevante sin mencionarlo literalmente. Sirve para
(1) mostrar en la hoja que puntos clave aparecen en cada chunk recuperado, y
(2) estimar el total de chunks relevantes del corpus (Recall@5) con datos y no a ojo.
"""

import glob
import hashlib
import os
import re
import unicodedata

STOPWORDS = {
    "entre", "sobre", "desde", "hasta", "como", "para", "porque", "cuando", "donde",
    "siendo", "sido", "tiene", "esta", "este", "estos", "estas", "otro", "otra",
    "otros", "pero", "aunque", "mismo", "cada", "todo", "todos", "antes", "despues",
    "durante", "segun", "tambien", "ademas", "dentro", "contra", "hacia",
}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return re.sub(r"[​\s]+", " ", text)


def split_keypoints(puntos_clave: list[str]) -> list[str]:
    """Divide los puntos clave largos ('Olmecas: civilizacion madre, cabezas colosales')
    en sub-puntos mas especificos."""
    out = []
    for pc in puntos_clave:
        for part in re.split(r"[:,;]", pc):
            part = part.strip()
            if part:
                out.append(part)
    return out


def significant_tokens(phrase: str) -> list[str]:
    toks = re.findall(r"[a-z0-9]+", normalize(phrase))
    sig = []
    for t in toks:
        if t.isdigit():
            if len(t) >= 3:
                sig.append(t)
        elif len(t) >= 4 and t not in STOPWORDS:
            sig.append(t)
    return sig


def keypoint_hits(text: str, puntos_clave: list[str], threshold: float = 0.6) -> list[str]:
    """Sub-puntos clave cuyos tokens significativos aparecen (>= threshold) en el texto."""
    norm = normalize(text)
    hits = []
    for kp in split_keypoints(puntos_clave):
        toks = significant_tokens(kp)
        if not toks:
            continue
        found = sum(1 for t in toks if t in norm)
        if found / len(toks) >= threshold:
            hits.append(kp)
    return hits


def find_candidates(chunks: list[dict], puntos_clave: list[str]) -> list[dict]:
    """Chunks DISTINTOS (texto no repetido) que mencionan al menos un punto clave,
    ordenados por numero de puntos clave presentes."""
    seen, cands = set(), []
    for c in chunks:
        key = hashlib.md5(c["texto"].encode("utf-8")).hexdigest()
        if key in seen:
            continue
        seen.add(key)
        hits = keypoint_hits(c["texto"], puntos_clave)
        if hits:
            cands.append({**c, "hits": hits})
    cands.sort(key=lambda c: -len(c["hits"]))
    return cands


def load_chunk_set(name: str) -> list[dict]:
    """Chunks del corpus como dicts: 'baseline' (ventana 300/50 de Fase 0) o 'paragraph'."""
    import json
    if name == "baseline":
        with open("embeddings/metadata.json", "r", encoding="utf-8") as f:
            return json.load(f)
    if name == "paragraph":
        from src.chunkers import ParagraphChunker
        chunker = ParagraphChunker(85)
        chunks = []
        for path in sorted(glob.glob("data/*.txt")):
            titulo = os.path.basename(path).replace(".txt", "").replace("_", " ")
            with open(path, "r", encoding="utf-8") as f:
                chunks.extend(c.model_dump() for c in chunker.chunk(f.read(), titulo))
        return chunks
    raise ValueError(f"chunk set desconocido: {name}")
