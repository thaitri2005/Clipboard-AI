# Local AI Clipboard

Send clipboard content to your local Ollama instance with a hotkey and get AI-processed results back!

## 🎯 Features

- **Hotkey Activation**: Press `Ctrl+Shift+G` to process clipboard content
- **Local AI Processing**: Uses your local Ollama instance
- **Seamless Workflow**: Copy → Process → Paste
- **Privacy First**: Everything runs locally on your machine

## 📋 Prerequisites

### 1. Install Ollama

Download and install Ollama from: https://ollama.ai/download

After installation, verify it's working:
```powershell
ollama --version
```

### 2. Pull an AI Model

Download a model (e.g., llama3.2):
```powershell
ollama pull llama3.2
```

Available models you can try:
- `llama3.2` - Fast and capable (recommended)
- `llama3.2:1b` - Smaller, faster
- `mistral` - Good alternative
- `codellama` - Specialized for code
- `phi3` - Compact and efficient

### 3. Install Python

Make sure Python 3.7+ is installed:
```powershell
python --version
```

If not installed, download from: https://www.python.org/downloads/

## 🚀 Installation

1. Clone this repository:
```powershell
git clone <your-repo-url>
cd Local-AI-Clipboard
```

2. Install Python dependencies:
```powershell
pip install -r requirements.txt
```

## ⚙️ Configuration

Edit `clipboard_ai.py` to change the Ollama model:

```python
OLLAMA_MODEL = "llama3.2"  # Change to your preferred model
```

## 🎮 Usage

1. Start the application:
```powershell
python clipboard_ai.py
```

2. Copy any text to your clipboard (Ctrl+C)

3. Press `Ctrl+Shift+G` to process it with AI

4. Wait for processing (you'll see progress in the terminal)

5. Paste the AI response (Ctrl+V)

## 💡 Example Use Cases

- **Writing Enhancement**: Copy text → Process → Get improved version
- **Code Explanation**: Copy code → Process → Get explanation
- **Translation**: Copy text → Process → Get translation
- **Summarization**: Copy article → Process → Get summary
- **Question Answering**: Copy question → Process → Get answer

## 🔧 Customization

You can customize the behavior by:

1. **Changing the model**: Edit `OLLAMA_MODEL` in `clipboard_ai.py`
2. **Adding prompts**: Modify the `send_to_ollama` function to prepend instructions
3. **Changing hotkey**: Modify the key detection in the `on_press` function

## 🐛 Troubleshooting

### "Ollama not found"
- Make sure Ollama is installed and in your PATH
- Try running `ollama --version` in terminal
- Restart your terminal after installing Ollama

### "Model not found"
- Pull the model: `ollama pull llama3.2`
- Check available models: `ollama list`

### Clipboard not working
- Make sure you have clipboard permissions
- Try running as administrator

### Hotkey not detected
- Make sure the application is running in the terminal
- Try running with administrator privileges

## 📝 Notes

- The application runs in the foreground and shows progress in the terminal
- Processing time depends on your hardware and the model size
- Larger models provide better results but take longer to process

## 🛑 Stopping the Application

Press `Ctrl+C` in the terminal window to stop the application.

## 📄 License

MIT License - Feel free to modify and use as needed!
