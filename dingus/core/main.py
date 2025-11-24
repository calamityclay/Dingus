from __future__ import annotations

import sys
from pathlib import Path

from dingus.core.interface import handle_command
from dingus.core.memory import MemoryStore
from dingus.core.model_backend import OllamaBackend


def main() -> int:
    print("Dingus v0.1 – local CLI (Ollama backend)")
    print("Type /help for commands, /quit to exit.\n")

    backend = OllamaBackend()
    memory = MemoryStore(Path("data") / "memory.json")

    while True:
        try:
            user_input = input("dingus> ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting Dingus.")
            break

        if not user_input.strip():
            continue

        # Log user input
        memory.log(role="user", text=user_input)

        result = handle_command(user_input, backend=backend)

        if result == "__DINGUS_EXIT__":
            print("Goodbye.")
            break

        if result:
            print(result)
            # Log assistant reply
            memory.log(role="assistant", text=result)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
