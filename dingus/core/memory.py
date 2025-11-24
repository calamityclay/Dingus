from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional

MemoryRole = Literal["user", "assistant", "system"]


@dataclass
class LogEntry:
    timestamp: str
    role: MemoryRole
    text: str
    project: str = "default"  # we'll make this meaningful later


class MemoryStore:
    """
    Super simple JSON-backed memory for v0.1.

    v0.1:
      - Append-only log of exchanges.
    v0.2:
      - Migrates to SQLite and adds richer structure.
    """

    def __init__(self, path: Path) -> None:
        self.path = path
        self._entries: List[LogEntry] = []
        self._load()

    def _load(self) -> None:
        if self.path.exists():
            try:
                data = json.loads(self.path.read_text(encoding="utf-8"))
                for raw in data:
                    self._entries.append(LogEntry(**raw))
            except Exception:
                # Don't crash just because the file is mangled; start fresh.
                self._entries = []

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data: List[Dict[str, Any]] = [asdict(e) for e in self._entries]
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def log(self, role: MemoryRole, text: str, project: str = "default") -> None:
        entry = LogEntry(
            timestamp=datetime.utcnow().isoformat() + "Z",
            role=role,
            text=text,
            project=project,
        )
        self._entries.append(entry)
        self._save()

    @property
    def entries(self) -> List[LogEntry]:
        return list(self._entries)
