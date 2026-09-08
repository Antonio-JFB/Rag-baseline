"""
Demo visual — Proposal 2 (SoC + interfaces) del RFC de Fase 1.

Corre la misma pregunta contra dos retrievers intercambiables (Cosine/FAISS
semántico vs BM25 léxico) sobre el mismo corpus e índice de chunks, para
mostrar que cambiar el método de retrieval no requiere tocar el pipeline:
solo se elige otra clase concreta desde el YAML de configuración.
"""

import streamlit as st

from src.config import build_pipeline, load_config
from src.pipeline import RAGPipeline, load_chunks

st.set_page_config(page_title="RAG Historia de México — Proposal 2", layout="wide")

PREGUNTAS_SUGERIDAS = [
    "(escribe tu propia pregunta)",
    "¿Quién fue Miguel Hidalgo y Costilla?",
    "¿Cuáles fueron las causas de la Revolución Mexicana?",
    "¿Qué diferencias hay entre la Conquista de México y la Independencia de México?",
    "¿Qué relación existe entre el Porfiriato y la Revolución Mexicana?",
    "¿Quién ganó el mundial de fútbol de 1970?",  # pregunta trampa: fuera del corpus
]

CONFIGS = {
    "cosine": "configs/cosine.yaml",
    "bm25": "configs/bm25.yaml",
}


@st.cache_resource(show_spinner="Cargando pipeline...")
def get_pipeline(config_path: str) -> RAGPipeline:
    cfg = load_config(config_path)
    pipeline = build_pipeline(cfg)
    pipeline.index(load_chunks())
    return pipeline


st.title("RAG — Historia de México")
st.caption(
    "Arquitectura SoC (Proposal 2 del RFC): el pipeline solo conoce `BaseRetriever`. "
    "Aquí se comparan dos implementaciones concretas sobre el **mismo** corpus (1,334 chunks) "
    "y el **mismo** LLM (Ollama · gemma3:12b) — lo único que cambia es la clase de retrieval."
)

with st.expander("Arquitectura", expanded=False):
    st.markdown(
        "```\n"
        "Query\n"
        "  │\n"
        "  ▼\n"
        "BaseRetriever ──┬── CosineFaissRetriever  (embeddings + FAISS, semántico)\n"
        "                └── BM25Retriever          (frecuencia de términos, léxico)\n"
        "  │\n"
        "  ▼\n"
        "BasePostprocessor  (NoOpPostprocessor — sin reranking en el baseline)\n"
        "  │\n"
        "  ▼\n"
        "BaseGenerator ──── OllamaGenerator  (gemma3:12b, local)\n"
        "  │\n"
        "  ▼\n"
        "Respuesta + prompt completo + tiempos (observabilidad 7/7)\n"
        "```\n"
        "Cambiar de retriever = crear una clase que herede `BaseRetriever` + una línea en el YAML "
        "(`configs/cosine.yaml` / `configs/bm25.yaml`). El pipeline (`src/pipeline.py`) no cambia."
    )

pregunta_sel = st.selectbox("Pregunta sugerida", PREGUNTAS_SUGERIDAS)
query = st.text_input(
    "O escribe tu propia pregunta",
    value="" if pregunta_sel == PREGUNTAS_SUGERIDAS[0] else pregunta_sel,
)

comparar = st.button("Comparar", type="primary")

if comparar and query.strip():
    col_cosine, col_bm25 = st.columns(2)

    for col, key, label in [
        (col_cosine, "cosine", "Cosine / FAISS (semántico)"),
        (col_bm25, "bm25", "BM25 (léxico)"),
    ]:
        with col:
            st.subheader(label)
            pipeline = get_pipeline(CONFIGS[key])
            with st.spinner(f"Recuperando + generando ({label})..."):
                result = pipeline.answer(query)

            m1, m2 = st.columns(2)
            m1.metric("Retrieval", f"{result.t_retrieval:.3f}s")
            m2.metric("Total", f"{result.t_total:.3f}s")

            st.markdown("**Chunks recuperados**")
            for i, rc in enumerate(result.retrieved, 1):
                st.markdown(f"`[{i}]` score={rc.score:.3f} · **{rc.chunk.fuente}**")
                st.caption(rc.chunk.texto[:180].strip() + "...")

            st.markdown("**Respuesta**")
            st.write(result.generation.respuesta)

            with st.expander("Prompt completo enviado al LLM"):
                st.text(result.generation.prompt)
elif comparar:
    st.warning("Escribe o selecciona una pregunta primero.")
