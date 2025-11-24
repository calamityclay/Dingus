from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


class Config:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.data = data

    @classmethod
    def load(cls, path: Path) -> "Config":
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")

        with path.open("r", encoding="utf-8") as f:
            raw = json.load(f)

        return cls(raw)

    def get(self, dotted_path: str, default: Any = None) -> Any:
        """
        Access nested configs like: get('model_backend.model')
        """
        node = self.data
        for part in dotted_path.split("."):
            if isinstance(node, dict) and part in node:
                node = node[part]
            else:
                return default
        return node
