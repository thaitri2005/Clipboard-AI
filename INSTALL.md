# 🚀 Quick Installation Guide

Follow these steps to get Local AI Clipboard up and running:

## Step 1: Install Ollama

1. Download Ollama for Windows: https://ollama.ai/download/windows
2. Run the installer
3. Open PowerShell or Command Prompt and verify:
   ```powershell
   ollama --version
   ```

## Step 2: Pull an AI Model

Choose and download a model (llama3.2 is recommended):

```powershell
# Recommended - Fast and capable (~2GB)
ollama pull llama3.2

# OR for smaller/faster (~700MB)
ollama pull llama3.2:1b

# OR other options
ollama pull mistral
ollama pull phi3
```

Test the model works:
```powershell
ollama run llama3.2
```
Type "Hello!" and press Enter. If you get a response, it's working! Type `/bye` to exit.

## Step 3: Install Python Dependencies

In the project directory, run:

```powershell
pip install -r requirements.txt
```

This will install:
- `pyperclip` - For clipboard access
- `pynput` - For global hotkey detection

## Step 4: Run the Application

### Option A: Use the quick start script
```powershell
.\start.bat
```

### Option B: Run directly
```powershell
python clipboard_ai.py
```

## Step 5: Test It!

1. Copy some text (Ctrl+C): "What is Python?"
2. Press **Ctrl+Shift+G**
3. Wait for the AI to process
4. Paste the result (Ctrl+V)

## 🎯 Customization

Edit `config.py` to:
- Change the AI model
- Add a system prompt (e.g., "Improve this text:")
- Adjust timeout settings

Example config:
```python
MODEL = "llama3.2"
SYSTEM_PROMPT = "You are a helpful writing assistant. Improve and enhance the following text:"
TIMEOUT = 120
VERBOSE = True
```

## ❓ Troubleshooting

### Ollama not found
- Make sure Ollama is installed
- Restart PowerShell/Command Prompt after installation
- Check PATH includes Ollama

### Hotkey not working
- Make sure the script is running in the terminal
- Try running PowerShell/Command Prompt as Administrator
- Check no other app is using Ctrl+Shift+G

### Slow responses
- Try a smaller model: `ollama pull llama3.2:1b`
- Check your CPU/GPU resources
- Increase TIMEOUT in config.py

## 🎉 You're All Set!

Keep the terminal window open and press Ctrl+Shift+G whenever you want to process clipboard content with AI!
