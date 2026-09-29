"""Schema de preguntas y ground truth (Pydantic) -- valida questions.json al cargarlo."""

from typing import Literal

from pydantic import BaseModel


class Question(BaseModel):
    id: str
    tipo: Literal["factual", "causalidad", "comparativa", "relacional", "multihop", "trampa"]
    pregunta: str
    puntos_clave: list[str]
    is_trap: bool = False
    nota: str | None = None


class EvaluationDataset(BaseModel):
    questions: list[Question]


def load_questions(path: str = "evaluation/questions.json") -> list[Question]:
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    dataset = EvaluationDataset.model_validate_json(raw)
    return dataset.questions
