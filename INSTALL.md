# 🚀 Installation Guide (Windows)

Follow these steps to get Local Clipboard AI running.

## 1) Install Ollama

Download and install:

<https://ollama.ai/download/windows>

Verify:

```powershell
ollama --version
```

## 2) Pull a model (default: phi3:mini)

```powershell
ollama pull phi3:mini
```

Alternatives:

```powershell
ollama pull qwen2.5-coder:1.5b
ollama pull codellama:7b
```

## 3) Install Python deps

```powershell
pip install -r requirements.txt
```

This includes:

- pyperclip (clipboard)
- pynput (hotkeys)
- python-dotenv (env loading)
- google-generativeai (optional; for Gemini)

## 4) Optional: Configure Gemini

```powershell
Copy-Item .env.example .env
# Edit .env and set GEMINI_API_KEY=AIza...your-key
```

## 5) Run

```powershell
python .\clipboard_ai.py
```

Use:

- Ctrl+Shift+G → Ollama (local)
- Ctrl+Shift+H → Gemini (cloud)
- Ctrl+Shift+Q → exit

## Customize

Edit `config.py`:

```python
MODEL = "phi3:mini"
SYSTEM_PROMPT = ""  # optional
TIMEOUT = 300
VERBOSE = True
GEMINI_MODEL = "gemini-2.5-pro"
```

## Troubleshooting

- “Ollama not found”: restart terminal, check `ollama --version`, reinstall
- “Model not found”: `ollama pull phi3:mini`
- Gemini 429: you hit rate limits—wait a bit and retry
- Hotkeys: hold Ctrl+Shift, then press G/H while app is running
