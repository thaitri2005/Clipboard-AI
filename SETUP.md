# 🚀 Automated Setup for Local AI Clipboard (SQL-Focused)

This script will install everything you need automatically!

## What This Will Do:

1. ✅ Install Ollama CLI
2. ✅ Pull a lightweight SQL-capable model (phi3:mini - only 2.3GB)
3. ✅ Install Python dependencies
4. ✅ Test the setup

## Run This Script:

```powershell
.\setup.ps1
```

If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup.ps1
```

## Manual Installation (if script fails):

### Step 1: Install Ollama CLI

```powershell
# Download and run installer
winget install Ollama.Ollama

# OR download manually from:
# https://ollama.com/download/OllamaSetup.exe
```

### Step 2: Pull Lightweight SQL Model

```powershell
# Recommended: phi3:mini (2.3GB, fast, good for SQL)
ollama pull phi3:mini

# Alternative options:
# ollama pull qwen2.5-coder:1.5b    # Even smaller (1GB)
# ollama pull codellama:7b          # Larger but better (3.8GB)
# ollama pull sqlcoder:7b           # SQL specialist (7GB)
```

### Step 3: Install Python Dependencies

```powershell
pip install -r requirements.txt
```

### Step 4: Test

```powershell
# Test Ollama
ollama run phi3:mini
# Type: "Write a SQL query to select all users" then /bye

# Run the app
python clipboard_ai.py
```

## 🎯 Ready to Use!

Once setup is complete:
1. Run: `.\start.bat`
2. Copy SQL or text (Ctrl+C)
3. Press Ctrl+Shift+G
4. Paste AI response (Ctrl+V)
