# 🛠️ Dingus Dev Notes

A scratchpad for development thoughts, ideas, and gotchas.

---

## Conventions

- Prefer boring, explicit code over clever, magical code.
- Keep modules small and single-purpose.
- When in doubt, add a short docstring or comment.

---

## Useful Patterns

- Centralize all model calls through `core/model_backend.py`.
- Keep command parsing in `core/interface.py` simple; let modules do the heavy lifting.
- Log new lessons and best practices into project playbooks over time.

---

## TODO (General)

- Implement `model_backend.py` with at least `OllamaBackend`.
- Add a `reflector.py` stub that we can later expand into ACE-style behavior.
- Define a minimal schema for SQLite for v0.2.
