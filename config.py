# Configuration file for Local AI Clipboard
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============================================================
# OLLAMA CONFIGURATION (Ctrl+Shift+G)
# ============================================================

# Ollama model to use
MODEL = "phi3:mini"

# Optional: Add a system prompt to customize AI behavior
# Leave empty for default behavior
SYSTEM_PROMPT = '''

'''

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
GEMINI_MODEL = "gemini-2.5-pro"

# Optional: System prompt for Gemini (can be different from Ollama)
# Leave empty to use the same SYSTEM_PROMPT as Ollama
GEMINI_SYSTEM_PROMPT = '''

'''

# ============================================================
# GENERAL SETTINGS
# ============================================================

# Show verbose output in terminal
VERBOSE = True
