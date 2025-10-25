# Configuration file for Local AI Clipboard

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
TIMEOUT = 120

# Show verbose output in terminal
VERBOSE = True
