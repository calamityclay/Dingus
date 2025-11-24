# 🧱 Dingus Architecture

This document zooms in on how Dingus is structured internally.

---

## High-Level View

```
Dingus Prime (core/main.py)
        |
        +-- CLI Interface (core/interface.py)
        |
        +-- Model Backend (core/model_backend.py)
        |
        +-- Memory Layer (core/memory.py / future SQLite)
        |
        +-- Modules (core/modules/)
              |-- project_manager.py
              |-- creative_aide.py
              |-- event_tech.py
              |-- reflector.py   (ACE-style reflection)
        |
        +-- Integrations (integrations/)
              |-- n8n_bridge.py
              |-- discord_bot.py
              |-- comfyui_bridge.py
              |-- fastapi_server.py
```

---

## Core Components

### Dingus Prime (core/main.py)

- Starts the REPL (`dingus>` prompt).
- Sends user input to `interface.handle_command()`.
- Prints responses back to the terminal.

### Interface (core/interface.py)

- Parses plain-text commands (e.g. `project new "Event Server Overhaul"`).
- Routes to appropriate module functions (project manager, memory search, etc.).
- Keeps commands simple and human-readable.

### Model Backend (core/model_backend.py)

- Abstracts away the underlying model server.
- Exposes a simple Python interface like `backend.generate(prompt: str) -> str`.
- Has concrete implementations such as:
  - `OllamaBackend` (current default)
  - `LlamaCppBackend` (future)

All modules depend only on this interface, not on Ollama directly.

### Memory (core/memory.py, future SQLite)

- Responsible for storing:
  - Project list
  - Logs
  - Notes
  - Pointers to playbook entries
- v0.1 stores data in `data/memory.json`.
- v0.2 migrates this into SQLite with proper tables.

### Modules (core/modules/)

- **project_manager.py**
  - Creates projects.
  - Logs messages to projects.
  - Requests summaries from the model backend.

- **creative_aide.py** (future)
  - Helps draft text, brainstorm ideas.
  - Uses project playbooks to stay consistent with prior decisions.

- **event_tech.py** (future)
  - Collects and exposes tech workflows, runbooks, and checklists.
  - Eventually can trigger automations via n8n.

- **reflector.py** (ACE future)
  - Takes logs and outcomes as input.
  - Suggests new rules or corrections for project playbooks.
  - Implements a basic Generator/Reflector/Curator loop over time.

---

## Data Layout

```
data/
  memory.json         # projects, logs, notes (v0.1)
  config.json         # backend settings, default model, etc.
  playbooks/
    <project>.md      # curated rules / knowledge for each project
```

- `config.json` selects:
  - Which backend to use (Ollama, llama.cpp, etc.).
  - Default model name (e.g. `"llama3"` or `"mistral"`).

---

## Integrations

- **n8n_bridge.py**
  - Sends events (e.g. `"project_updated"`, `"task_completed"`) to n8n via HTTP/webhooks.
- **discord_bot.py**
  - Provides a Discord interface to Dingus commands.
- **comfyui_bridge.py**
  - Connects to ComfyUI workflows for image generation.
- **fastapi_server.py**
  - Optional HTTP API or web UI layer around Dingus.

These remain thin adapters so the core stays clean and testable.

---

## Future Directions

- Plug-and-play backends beyond Ollama/llama.cpp.
- Richer ACE-style reflection that continuously updates playbooks.
- Distributed setups where heavy workloads run on remote machines.
