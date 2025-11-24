from __future__ import annotations

from typing import Protocol

# A lightweight protocol so we don't import the concrete backend here.
class SupportsGenerate(Protocol):
    def generate(self, prompt: str) -> str:
        ...


def handle_command(user_input: str, backend: SupportsGenerate) -> str:
    """
    Parse and handle a single line of user input.

    v0.1 Milestone A:
      - If input starts with '/', we treat some as control commands.
      - Otherwise, send directly to the LLM backend.

    Future:
      - Recognize commands like:
          project new "Event Server Overhaul"
          project log "..." 
          project summary
      - Route to modules (project_manager, creative_aide, etc.).
    """
    stripped = user_input.strip()

    if not stripped:
        return ""

    # Simple control commands
    if stripped in {"/quit", "/exit"}:
        # The REPL loop will interpret this specially; just echo a marker.
        return "__DINGUS_EXIT__"

    if stripped in {"/help", "/?"}:
        return (
            "Dingus v0.1 – available commands:\n"
            "  /help           Show this help message.\n"
            "  /quit, /exit    Exit Dingus.\n"
            "Anything else is sent to the model backend via Ollama."
        )

    # For now, everything else is just a prompt to the backend.
    return backend.generate(stripped)
