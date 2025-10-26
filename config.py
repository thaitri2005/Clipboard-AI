# Configuration file for Local AI Clipboard
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================
# OLLAMA CONFIGURATION (Ctrl+Shift+G)
# ============================================================

# Ollama model to use
# Recommended lightweight models for SQL:
# - "sqlcoder:7b" - Specialized for SQL (7GB)
# - "codellama:7b" - Good for code including SQL (3.8GB) 
# - "phi3:mini" - Very lightweight, handles SQL well (2.3GB) ⭐ RECOMMENDED
# - "qwen2.5-coder:1.5b" - Smallest, fast, decent SQL (1GB)
MODEL = "phi3:mini"

# Optional: Add a system prompt to customize AI behavior
# Leave empty for default behavior
# For SQL tasks, you might want:
# - "You are an SQL expert. Help with the following SQL query:"
# - "Explain this SQL query in simple terms:"
# - "Optimize the following SQL query:"
# - "Convert this to SQL:"
SYSTEM_PROMPT = ""

# Timeout for Ollama response (seconds)
# Increase this if you get timeout errors
# First run might be slow as model loads into memory
TIMEOUT = 300  # 5 minutes (increased from 120s)

# ============================================================
# GEMINI API CONFIGURATION (Ctrl+Shift+H)
# ============================================================

# Get your API key from: https://makersuite.google.com/app/apikey
# Set this in your .env file: GEMINI_API_KEY=your-key-here
# The .env file is gitignored for security
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Gemini model to use
# Available models:
# - "gemini-2.5-pro" - Latest and most capable ⭐ RECOMMENDED
# - "gemini-2.0-flash-thinking-exp-01-21" - Fast with reasoning
# - "gemini-2.0-flash-exp" - Fast and efficient
# - "gemini-1.5-pro" - Previous generation
# - "gemini-1.5-flash" - Previous generation, fast
GEMINI_MODEL = "gemini-2.5-pro"

# Optional: System prompt for Gemini (can be different from Ollama)
# Leave empty to use the same SYSTEM_PROMPT as Ollama
GEMINI_SYSTEM_PROMPT = ""

# ============================================================
# GENERAL SETTINGS
# ============================================================

# Show verbose output in terminal
VERBOSE = True
