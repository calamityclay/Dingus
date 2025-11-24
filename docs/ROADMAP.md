# 📌 Dingus — Roadmap & Architecture (v0.1 → v1.0)

This file defines the authoritative, high-level design for **Dingus**, the modular local-first AI assistant running on Windows with an RTX 4080. All development in adjacent chats should reference this roadmap.

---

## 🎯 Overall Goals

- Fully local personal assistant.
- Runs on **Windows**, uses **Ollama** (for now) for model serving.
- Modular “Dingus Prime → Specialists → Integrations” architecture.
- Long-term support for ACE-style agent reasoning and context curation.

---

## 🧱 Core Architecture

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
    memory.json
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

---

## 🧠 Memory Layers (ACE-Inspired)

### 1. Raw Log Stream
- Complete chronological record of tasks, events, debugging notes, actions.
- Stored in JSON (v0.1) → SQLite (v0.2).

### 2. Working Memory / Session Context
- Short-term relevant subset used during conversation.
- Dynamically selected by heuristics or reflection.

### 3. Playbook (Curated Knowledge)
- Long-term, distilled rules.
- Editable by user (“promote to playbook”).
- Automatically updated by ACE-style reflection loops (v0.3+).

---

## 🧩 Backend Design (Ollama vs llama.cpp)

### Present (v0.1–v0.3)
- Default backend: **Ollama** on Windows.
- Dingus communicates via `http://localhost:11434`.

### Future (v0.4+)
- Add pluggable backends using `core/model_backend.py`.
- Support `llama-server` from llama.cpp for performance builds.
- Switch backends through `data/config.json` without code changes.

---

## 🚦 Version Roadmap

### **v0.1 — Bootstrap**
- Local CLI (REPL)
- JSON memory
- Project logs + summaries
- Manual “promote to playbook”

### **v0.2 — Structure + SQLite**
- Move memory to SQLite
- Better command syntax
- Context window selection for LLM calls

### **v0.3 — Automations & ACE Seeds**
- Discord bot
- n8n automation hooks
- Initial ACE “Reflector” step (suggest playbook entries)

### **v0.4 — ComfyUI Integration**
- Stable Diffusion prompting module
- Image workflow orchestration
- Style consistency via project playbooks

### **v1.0 — Full Orchestrator**
- Multi-specialist routing
- Full ACE loop (Generator → Reflector → Curator)
- Optional remote node support for heavy tasks

---

## 🔁 Tech Check Ritual

- Update `/docs/TECH_CHECKS.md` regularly with backend decisions, memory model changes, agent framework changes, and integration updates.

---

## 🧭 Philosophy

**Local first. Modular always. Private forever.**
