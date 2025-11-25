# dingus/core/modules/playbook.py

from __future__ import annotations

from datetime import datetime
from pathlib import Path


class PlaybookManager:
    """
    v0.1 manual playbooks:
      - One markdown file per project in data/playbooks/
      - /playbook add: append a timestamped bullet
      - /playbook show: display contents
    """

    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _path_for(self, project: str) -> Path:
        safe = project.replace(" ", "_")
        return self.base_dir / f"{safe}.md"

    def add_entry(self, project: str, text: str) -> str:
        path = self._path_for(project)
        exists = path.exists()

        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%MZ")

        if not exists:
            header = f"# Playbook – {project}\n"
        else:
            header = ""

        entry = f"\n\n### {timestamp}\n\n- {text.strip()}\n"

        with path.open("a", encoding="utf-8") as f:
            if header:
                f.write(header)
            f.write(entry)

        return f"Added playbook entry for project '{project}'. ({path})"

    def show(self, project: str) -> str:
        path = self._path_for(project)
        if not path.exists():
            return f"No playbook yet for project '{project}'."
        return path.read_text(encoding="utf-8")
