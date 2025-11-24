from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Optional

import requests


@dataclass
class BackendConfig:
    base_url: str = "http://localhost:11434"
    model: str = "llama3"  # adjust to whatever you've pulled in Ollama


class ModelBackend:
    """Abstract interface for any model backend (Ollama, llama.cpp, etc.)."""

    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class OllamaBackend(ModelBackend):
    """Simple HTTP client for the Ollama server."""

    def __init__(self, config: Optional[BackendConfig] = None) -> None:
        self.config = config or BackendConfig()

    def generate(self, prompt: str) -> str:
        """
        Call Ollama's /api/generate endpoint in non-streaming mode
        and return just the model's text response.
        """
        url = f"{self.config.base_url}/api/generate"
        payload = {
            "model": self.config.model,
            "prompt": prompt,
            "stream": False,
        }

        try:
            resp = requests.post(url, json=payload, timeout=120)
        except requests.RequestException as e:
            return f"[OllamaBackend error] Failed to reach Ollama: {e}"

        if resp.status_code != 200:
            return f"[OllamaBackend error] HTTP {resp.status_code}: {resp.text}"

        try:
            data = resp.json()
        except json.JSONDecodeError:
            return "[OllamaBackend error] Could not decode JSON from Ollama."

        return data.get("response", "").strip()
