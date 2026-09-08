"""Implementaciones de BaseGenerator."""

import time

import requests

from src.interfaces import BaseGenerator, GenerationResult, RetrievedChunk

PROMPT_TEMPLATE = """Eres un asistente experto en historia de México.
Responde la pregunta ÚNICAMENTE usando los fragmentos de contexto.
Si la información no está en los fragmentos, di: "No encontré esta información en el corpus."
Al final indica qué fuentes usaste.

CONTEXTO:
{contexto}

PREGUNTA: {query}

RESPUESTA:"""


class OllamaGenerator(BaseGenerator):
    def __init__(
        self,
        model: str = "gemma3:12b",
        url: str = "http://localhost:11434/api/generate",
        temperature: float = 0.1,
        num_predict: int = 800,
        timeout: int = 240,
    ):
        self.model = model
        self.url = url
        self.temperature = temperature
        self.num_predict = num_predict
        self.timeout = timeout

    def _build_prompt(self, query: str, resultados: list[RetrievedChunk]) -> str:
        partes = [
            f"[Fragmento {i} | Fuente: {r.chunk.fuente} | Score: {r.score:.3f}]\n{r.chunk.texto}"
            for i, r in enumerate(resultados, 1)
        ]
        contexto = "\n\n---\n\n".join(partes)
        return PROMPT_TEMPLATE.format(contexto=contexto, query=query)

    def generate(self, query: str, resultados: list[RetrievedChunk]) -> GenerationResult:
        prompt = self._build_prompt(query, resultados)

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": self.temperature,
                "num_predict": self.num_predict,
            },
        }

        t0 = time.time()
        try:
            resp = requests.post(self.url, json=payload, timeout=self.timeout)
            resp.raise_for_status()
            respuesta = resp.json().get("response", "Error: respuesta vacía de Ollama")
        except requests.exceptions.Timeout:
            respuesta = "Error: Ollama tardó demasiado. Intenta con un modelo más pequeño."
        except Exception as e:
            respuesta = f"Error al llamar a Ollama: {e}"
        latency_s = time.time() - t0

        return GenerationResult(respuesta=respuesta, prompt=prompt, latency_s=latency_s)
