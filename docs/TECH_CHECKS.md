# 🔁 Dingus Tech Checks

This file tracks important technical decisions and changes over time.

Each entry should be:
- Dated
- Short
- Explicit about what changed and why

---

## 2025-11-23 — Initial Snapshot

- Backend: **Ollama** on Windows chosen as initial model server.
- Backend strategy: all LLM usage goes through `core/model_backend.py` to allow later swap to `llama.cpp` or other servers.
- Memory model: adopt ACE-inspired 3-layer memory (logs, working context, playbook).
- Roadmap: v0.1–v1.0 milestones defined in `ROADMAP.md`.

---

## Template for Future Entries

Copy this format for new entries:

### YYYY-MM-DD — Title

- Backend:
- Memory:
- Agents:
- Integrations:
- Notes:
