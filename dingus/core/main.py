from __future__ import annotations

import sys
from pathlib import Path

from dingus.core.config import Config
from dingus.core.interface import handle_command
from dingus.core.memory import MemoryStore
from dingus.core.model_backend import BackendConfig, OllamaBackend
from dingus.core.modules.project_manager import ProjectManager
from dingus.core.modules.playbook import PlaybookManager

def main() -> int:
    # Load config
    config = Config.load(Path("config.json"))

    backend_cfg = BackendConfig(
        base_url=config.get("model_backend.base_url", "http://localhost:11434"),
        model=config.get("model_backend.model", "llama3")
    )

    backend = OllamaBackend(backend_cfg)
    print(f"[debug] Using model '{backend_cfg.model}'")

    memory = MemoryStore(Path("data") / "memory.json")

    project_mgr = ProjectManager(
        memory,
        default_project=config.get("dingus.default_project", "default")
    )
    
    playbook_mgr = PlaybookManager(Path("data") / "playbooks")

    print("Dingus v0.1 – local CLI (Ollama backend)")
    print("Type /help for commands, /quit to exit.\n")

    while True:
        try:
            user_input = input("dingus> ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting Dingus.")
            break

        if not user_input.strip():
            continue

        # -------------------------------------------
        # PLAYBOOK COMMANDS
        # -------------------------------------------
        if user_input.startswith("/playbook "):
            parts = user_input.split(" ", 2)
            if len(parts) < 2:
                print("Usage: /playbook <show|add> [text]")
                continue

            subcmd = parts[1]
            arg = parts[2] if len(parts) > 2 else ""
            project = project_mgr.active_project

            if subcmd == "show":
                print(playbook_mgr.show(project))
            elif subcmd == "add":
                if not arg.strip():
                    print("Usage: /playbook add <text-to-promote>")
                else:
                    print(playbook_mgr.add_entry(project, arg))
            else:
                print("Unknown playbook subcommand.")
            continue

        # -------------------------------------------
        # PROJECT COMMANDS
        # -------------------------------------------
        if user_input.startswith("/project "):
            parts = user_input.split(" ", 2)

            if len(parts) < 2:
                print("Usage: /project <create|switch|list|summary> [name]")
                continue

            subcmd = parts[1]
            arg = parts[2] if len(parts) > 2 else ""

            if subcmd == "create":
                print(project_mgr.create(arg))
            elif subcmd == "switch":
                print(project_mgr.switch(arg))
            elif subcmd == "list":
                print("\n".join(project_mgr.list()))
            elif subcmd == "summary":
                # If name provided, summarize that project; otherwise current
                target = arg or None
                print(project_mgr.summarize(backend=backend, project=target))
            else:
                print("Unknown project subcommand.")
            continue

        # -------------------------------------------
        # NORMAL MODEL QUERY
        # -------------------------------------------
        memory.log(role="user", text=user_input, project=project_mgr.active_project)

        result = handle_command(user_input, backend=backend)

        if result == "__DINGUS_EXIT__":
            print("Goodbye.")
            break

        if result:
            print(result)
            memory.log(role="assistant", text=result, project=project_mgr.active_project)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())