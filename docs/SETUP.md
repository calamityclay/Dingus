# ⚙️ Dingus Setup Guide (Windows, RTX 4080)

This guide walks through the basic environment setup for Dingus.

---

## 1. Install Prerequisites

- **Python** 3.11+ from python.org
- **Git** (optional but recommended)
- **Ollama for Windows** from ollama.com (for local models)

Verify Python:

```powershell
python --version
```

Verify Git (optional):

```powershell
git --version
```

---

## 2. Create Project Folder

Pick a folder, e.g.:

```powershell
mkdir C:\dev\dingus
cd C:\dev\dingus
```

If you have a prepared zip, extract it here so it contains `core/`, `data/`, `docs/`, etc.

---

## 3. Virtual Environment

```powershell
python -m venv venv
venv\Scripts\activate
```

Your prompt should now start with `(venv)`.

---

## 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

If `requirements.txt` is empty or minimal, this step should be quick.

---

## 5. Setup Ollama

Install Ollama for Windows and then in **a separate terminal**:

```powershell
ollama serve
ollama pull mistral
# or
ollama pull llama3
```

You can test the API:

```powershell
curl http://localhost:11434/api/tags
```

You should see a JSON list of models.

---

## 6. Run Dingus

From inside your project folder with the virtual environment active:

```powershell
python core\main.py
```

You should see something like:

```text
Dingus Prime (v0.1) — local-first assistant
Type 'help' for commands.
dingus>
```

---

## 7. First Commands

Try:

```text
help
projects
project new "Event Server Overhaul"
log "Event Server Overhaul" "Fixed OBS reconnect issue."
summarize "Event Server Overhaul"
recall "OBS"
quit
```

If `summarize` fails because Ollama isn't running, Dingus should fall back to a naive summary.

---

## 8. Where to Change Settings

- `data/config.json` controls:
  - Default model name
  - Ollama endpoint URL
  - Future: backend selection

---

## 9. Next Steps

- Wire in `model_backend.py` to cleanly handle different model servers.
- Migrate memory to SQLite (v0.2).
- Add Discord and n8n integrations (v0.3).
