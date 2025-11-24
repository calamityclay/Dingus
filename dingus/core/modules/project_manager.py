from __future__ import annotations

from pathlib import Path
from typing import List

from dingus.core.memory import MemoryStore


class ProjectManager:
    """
    Minimal v0.1 project manager:
      - Tracks active project name
      - Creates new project names
      - Lists existing projects
    """

    def __init__(self, memory: MemoryStore, default_project: str = "default"):
        self.memory = memory
        self.active_project = default_project

    def create(self, name: str) -> str:
        name = name.strip()
        if not name:
            return "Project name cannot be empty."

        # If any log has this project name, it already exists.
        existing = {e.project for e in self.memory.entries}
        if name in existing:
            return f"Project '{name}' already exists."

        # Create an empty placeholder log entry to mark project creation
        self.memory.log(role="system", text=f"[created project {name}]", project=name)
        return f"Created project '{name}'."

    def list(self) -> List[str]:
        projects = {e.project for e in self.memory.entries}
        if not projects:
            return ["default"]
        return sorted(projects)

    def switch(self, name: str) -> str:
        name = name.strip()
        if not name:
            return "Project name cannot be empty."

        projects = {e.project for e in self.memory.entries}
        if name not in projects:
            return f"Project '{name}' does not exist."

        self.active_project = name
        return f"Switched to project '{name}'."
