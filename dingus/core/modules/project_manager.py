"""
Project Manager module (stub for v0.1 Milestone A).

Future responsibilities:
  - Create and list projects.
  - Attach logs to specific projects.
  - Request summaries from the model backend.
  - Promote important insights into project playbooks.
"""

from __future__ import annotations

from typing import Iterable

from dingus.core.memory import MemoryStore


def list_projects(memory: MemoryStore) -> Iterable[str]:
    """
    v0.1 stub: infer project names from existing logs.
    Later we will have explicit project objects.
    """
    projects = {entry.project for entry in memory.entries}
    if not projects:
        return ["default"]
    return sorted(projects)
