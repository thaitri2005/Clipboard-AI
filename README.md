# Local AI Clipboard

Send clipboard content to your local Ollama instance with a hotkey and get AI-processed results back!

**Optimized for SQL tasks with a lightweight model!**

## 🎯 Features

- **Hotkey Activation**: Press `Ctrl+Shift+G` to process clipboard content
- **Local AI Processing**: Uses your local Ollama CLI
- **Lightweight**: Configured with phi3:mini (~2.3GB, fast, SQL-capable)
- **Seamless Workflow**: Copy → Process → Paste
- **Privacy First**: Everything runs locally on your machine
- **SQL Optimized**: Great for SQL queries, explanations, and optimization

## 🚀 Quick Start (Automated)

Run the automated setup script:

```powershell
.\setup.ps1
```

That's it! The script will:
1. Install Ollama CLI
2. Download phi3:mini model (~2.3GB)
3. Install Python dependencies
4. Test everything

## � Manual Installation

If you prefer manual setup, see [INSTALL.md](INSTALL.md) or [SETUP.md](SETUP.md)

## ⚙️ Configuration

Edit `config.py` to customize:

```python
MODEL = "phi3:mini"  # Lightweight, SQL-capable model
SYSTEM_PROMPT = ""   # Add custom instructions like "Explain this SQL:"
TIMEOUT = 120        # Response timeout in seconds
VERBOSE = True       # Show detailed output
```

### Recommended Models for SQL:
- **phi3:mini** (2.3GB) - ⭐ Default, fast, lightweight, good SQL
- **qwen2.5-coder:1.5b** (1GB) - Smallest, very fast
- **codellama:7b** (3.8GB) - Better for complex SQL
- **sqlcoder:7b** (7GB) - SQL specialist (requires more resources)

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

### SQL-Focused Tasks:
- **Query Explanation**: Copy SQL → Process → Get plain English explanation
- **Query Optimization**: Copy slow query → Process → Get optimized version
- **Query Generation**: Copy requirements → Process → Get SQL query
- **Error Debugging**: Copy error message → Process → Get solution
- **Schema Design**: Copy requirements → Process → Get table schemas

### General Tasks:
- **Code Explanation**: Copy code → Process → Get explanation
- **Text Enhancement**: Copy draft → Process → Get improved version
- **Summarization**: Copy article → Process → Get summary

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
