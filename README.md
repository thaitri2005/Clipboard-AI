# Clipboard AI

Send clipboard content to a local Ollama model or Google Gemini with a hotkey, and get the result copied back to your clipboard. Copy → Process → Paste.

## Features

- Dual modes
  - Ctrl+Shift+G → Ollama (local, private, free)
  - Ctrl+Shift+H → Gemini (cloud, fast; optional with .env)
- Result copied back to clipboard automatically
- Layout-independent hotkeys (virtual key codes)
- Robust clipboard retries and clean output (ANSI stripped)
- Verbose logging for easy troubleshooting

## Quick start (Windows PowerShell)

Automated setup:

```powershell
./setup.ps1
```

Manual essentials:

```powershell
# In repo root
pip install -r requirements.txt
ollama pull phi3:mini
python .\clipboard_ai.py
```

Optional Gemini (.env):

```powershell
Copy-Item .env.example .env
# Edit .env and set: GEMINI_API_KEY=AIza...your-key
```

## Start the app

You can launch it either way:

- Double-click `start.bat` (recommended for everyday use)
  - Creates/uses a local venv (if present), installs deps if needed, ensures `.env`, and starts the app
- From a terminal (inside the repo):

  ```powershell
  python .\clipboard_ai.py
  ```

## Usage

1) Copy any text (Ctrl+C)
2) Press a hotkey while the app is running
   - Ctrl+Shift+G → process with Ollama (local)
   - Ctrl+Shift+H → process with Gemini (cloud)
3) Paste the result (Ctrl+V)
4) Exit anytime with Ctrl+Shift+Q

## Configuration

Edit `config.py`:

```python
MODEL = "phi3:mini"      # default Ollama model
TIMEOUT = 300             # seconds
VERBOSE = True            # debug output
SYSTEM_PROMPT = ""        # optional

GEMINI_MODEL = "gemini-2.5-pro"   # cloud
# GEMINI_API_KEY comes from .env
```

Notes:
- API key must be in `.env` as `GEMINI_API_KEY=...` (the file is gitignored)
- We removed conversation history to keep it fast and lightweight

## Recommended Ollama models:

- phi3:mini (default) — small, fast
- qwen2.5-coder:1.5b — very small and quick
- codellama:7b — bigger, stronger

Pull another model:

```powershell
ollama pull qwen2.5-coder:1.5b
```

## Troubleshooting

- “Ollama not found”: restart PowerShell; check `ollama --version`; install from https://ollama.ai/download
- “Model not found”: `ollama pull phi3:mini`; check `ollama list`
- Gemini 429 (rate limit): wait and retry; keep requests modest
- Hotkeys: run app; press and hold Ctrl+Shift, then tap G/H; layout independent
- Clipboard conflicts: other clipboard managers can lock access; we retry automatically

More tips in `TROUBLESHOOTING.md` and hotkey details in `HOTKEYS.md`.

## License

MIT
