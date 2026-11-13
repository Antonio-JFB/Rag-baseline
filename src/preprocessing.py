"""
Preprocesamiento lexico para BM25 (se aplica igual al corpus y a la consulta).

PlainPreprocessor        -> minusculas + tokens \\w+ (el BM25 de referencia; no lematiza
                            ni quita palabras vacias).
SpacyLemmaPreprocessor   -> lematizacion (spaCy, es_core_news_sm) + eliminacion de palabras
                            vacias con la lista estandar de spaCy para espanol.

La lista de palabras vacias es la estandar y NO se ajusta a las preguntas del experimento.
Tiene efectos conocidos: elimina terminos que en algunas preguntas son contenido
(p. ej. 'ultimo' en 'ultimo emperador', 'final', 'antes', 'despues').
"""

import re
from typing import Iterable, Protocol


class Preprocessor(Protocol):
    def tokens(self, text: str) -> list[str]: ...
    def tokens_many(self, texts: Iterable[str]) -> list[list[str]]: ...


class PlainPreprocessor:
    def tokens(self, text: str) -> list[str]:
        return re.findall(r"\w+", text.lower())

    def tokens_many(self, texts: Iterable[str]) -> list[list[str]]:
        return [self.tokens(t) for t in texts]


class SpacyLemmaPreprocessor:
    def __init__(self, model: str = "es_core_news_sm"):
        self.model = model
        self._nlp = None

    @property
    def nlp(self):
        if self._nlp is None:
            import spacy
            self._nlp = spacy.load(self.model, disable=["parser", "ner"])
        return self._nlp

    def _keep(self, token) -> list[str]:
        if token.is_punct or token.is_space:
            return []
        text = token.text.lower()
        lemma = token.lemma_.lower()
        stop = self.nlp.Defaults.stop_words
        if text in stop or lemma in stop:
            return []
        return re.findall(r"\w+", lemma)

    def tokens(self, text: str) -> list[str]:
        return [t for tok in self.nlp(text) for t in self._keep(tok)]

    def tokens_many(self, texts: Iterable[str]) -> list[list[str]]:
        return [[t for tok in doc for t in self._keep(tok)]
                for doc in self.nlp.pipe(texts, batch_size=64)]


def build_preprocessor(name: str) -> Preprocessor:
    if name == "none":
        return PlainPreprocessor()
    if name == "lemma_stopwords":
        return SpacyLemmaPreprocessor()
    raise ValueError(f"preprocesamiento lexico desconocido: {name}")
