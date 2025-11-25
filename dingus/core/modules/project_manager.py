from __future__ import annotations

from pathlib import Path
from typing import List

from dingus.core.memory import MemoryStore
from dingus.core.model_backend import ModelBackend  # import the base class/interface


class ProjectManager:
    """
    Minimal v0.1 project manager:
      - Tracks active project name
      - Creates new project names
      - Lists existing projects
      - Summarizes project logs via the model backend
    """

    def __init__(self, memory: MemoryStore, default_project: str = "default"):
        self.memory = memory
        self.active_project = default_project

    def create(self, name: str) -> str:
        name = name.strip()
        if not name:
            return "Project name cannot be empty."

        existing = {e.project for e in self.memory.entries}
        if name in existing:
            return f"Project '{name}' already exists."

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

    def summarize(
        self,
        backend: ModelBackend,
        project: str | None = None,
        max_chars: int = 4000,
    ) -> str:
        """
        Ask the model to summarize this project's log.

        v0.1: keep it simple:
          - Pull full user/assistant log for the project
          - Truncate to a rough char limit
          - Ask for a structured summary
        """
        proj = project or self.active_project
        entries = self.memory.get_project_dialogue(proj)

        if not entries:
            return f"No log entries yet for project '{proj}'."

        # Build a plain-text transcript
        lines: list[str] = []
        for e in entries:
            speaker = "User" if e.role == "user" else "Assistant"
            lines.append(f"{speaker}: {e.text}")

        transcript = "\n".join(lines)

        # Rough safety truncation for context size
        if len(transcript) > max_chars:
            transcript = transcript[-max_chars:]

        prompt = (
            "You are Dingus, a local project assistant. "
            "You will be given the log of a project (user + assistant messages). "
            "Write a concise project summary in Markdown.\n\n"
            f"Project name: {proj}\n\n"
            "Log:\n"
            f"{transcript}\n\n"
            "Now summarize with the following sections:\n"
            "## Overview\n"
            "## Key Decisions\n"
            "## Open Questions\n"
            "## Next Actions\n"
        )

        return backend.generate(prompt)
