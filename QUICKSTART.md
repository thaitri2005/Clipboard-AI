# 🎉 Quickstart

## ✅ Prereqs

- Python deps installed (`pip install -r requirements.txt`)
- Ollama installed and in PATH
- Model pulled: `ollama pull phi3:mini`

## 🔄 What you need to do

### Step 1 - Restart PowerShell

Ollama was just installed, so you need to close and reopen PowerShell for it to be available in your PATH.

### Step 2 - Pull the AI model

```powershell
ollama pull phi3:mini
```

This downloads a small model (~2.3GB).

### Step 3 - Test Ollama (optional)

```powershell
ollama run phi3:mini
```

Type something like: `Explain SELECT * FROM users WHERE age > 18;` then `/bye` to exit.

### Step 4 - Run the application

```powershell
./start.bat
```

Or run directly:

```powershell
python .\clipboard_ai.py
```

Optional: enable Gemini

```powershell
Copy-Item .env.example .env
# Edit .env and set GEMINI_API_KEY=AIza...your-key
```

## 🎯 How to use

1. Keep the terminal open (app must run)
2. Copy any text/SQL to clipboard (Ctrl+C)
3. Press Ctrl+Shift+G (Ollama) or Ctrl+Shift+H (Gemini)
4. Wait for processing (watch the terminal)
5. Paste the result (Ctrl+V)

## 💡 Quick test (Ollama)

Try this:

1. Copy: `SELECT * FROM users WHERE age > 18`
2. Press Ctrl+Shift+G
3. Paste the explanation

## 🔧 Customization (config.py)

```python
MODEL = "phi3:mini"
SYSTEM_PROMPT = ""   # optional
TIMEOUT = 300
VERBOSE = True
GEMINI_MODEL = "gemini-2.5-pro"
```

## ❓ Troubleshooting

If Ollama still not found after restart:

- Check system tray for Ollama
- Try manual install: <https://ollama.com/download/OllamaSetup.exe>

If model pull fails:

- Check internet connection
- Try: `ollama pull qwen2.5-coder:1.5b` (smaller)
- Or: `ollama pull codellama:7b` (larger)

You're set! Close this PowerShell, open a new one, and run:

```powershell
cd D:\Local-AI-Clipboard
ollama pull phi3:mini
./start.bat
```
