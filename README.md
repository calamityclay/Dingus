# Dingus — Local AI Assistant (v0.1)

Dingus is a local-first, modular AI assistant running on Windows and powered by Ollama.
It is designed as a personal orchestrator with clean Python modules, swappable backends,
and room for ACE-style reflection.

## Goals

- Fully local and private
- Modular Python architecture
- Simple CLI interface
- Project manager and creative modules
- Future integrations: n8n, Discord bot, ComfyUI

## Project Structure

```
dingus/
  core/
    main.py
    interface.py
    memory.py
    model_backend.py
    modules/
      project_manager.py
      creative_aide.py
      event_tech.py
      reflector.py
  data/
    memory.json   (ignored)
    config.json
    playbooks/
  integrations/
    n8n_bridge.py
    discord_bot.py
    comfyui_bridge.py
    fastapi_server.py
  prompts/
    system/
    templates/
  docs/
    ROADMAP.md
    ARCHITECTURE.md
    TECH_CHECKS.md
```

## Version Roadmap (Summary)

- v0.1 — Bootstrap: CLI, JSON memory, project logs  
- v0.2 — SQLite memory and better context selection  
- v0.3 — n8n hooks, Discord bot, ACE reflection seeds  
- v0.4 — ComfyUI integration  
- v1.0 — Full orchestrator with multi-specialist routing

## Philosophy

Local first. Modular always. Private forever.
