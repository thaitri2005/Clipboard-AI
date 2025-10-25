# 🌐 Gemini API Setup Guide

## Get Your Free Gemini API Key

1. **Visit Google AI Studio:**
   https://makersuite.google.com/app/apikey

2. **Sign in** with your Google account

3. **Click "Create API Key"**

4. **Copy your API key** (starts with `AIza...`)

## Configure the App

### 1. Install Gemini Package

```powershell
pip install google-generativeai
```

### 2. Add API Key to Config

Edit `config.py`:

```python
# ============================================================
# GEMINI API CONFIGURATION (Ctrl+Shift+H)
# ============================================================

# Paste your API key here:
GEMINI_API_KEY = "AIzaSyD...your-key-here..."

# Choose your model (recommended: gemini-2.0-flash-exp)
GEMINI_MODEL = "gemini-2.0-flash-exp"

# Optional: Different prompt for Gemini
GEMINI_SYSTEM_PROMPT = ""  # Leave empty to use same as Ollama
```

### 3. Restart the App

```powershell
python clipboard_ai.py
```

You should now see:
```
🌐 Gemini model: gemini-2.0-flash-exp
⌨️  Ctrl+Shift+H - Process with Gemini (cloud)
```

## Usage

### Two Modes Available:

**Ctrl+Shift+G** - **Ollama (Local)**
- Runs on your computer
- Private, no internet needed
- Slower first run, fast after
- Free forever

**Ctrl+Shift+H** - **Gemini (Cloud)**
- Runs on Google's servers
- Requires internet connection
- Fast response (2-10 seconds)
- Free tier: 60 requests/minute

## Models Available

Edit `GEMINI_MODEL` in `config.py`:

```python
# Fastest, latest (recommended)
GEMINI_MODEL = "gemini-2.0-flash-exp"

# Fast and efficient
GEMINI_MODEL = "gemini-1.5-flash"

# More capable, slower
GEMINI_MODEL = "gemini-1.5-pro"
```

## Cost & Limits

**Free Tier:**
- 60 requests per minute
- 1,500 requests per day
- 1 million tokens per month

More than enough for typical use!

Check your usage: https://makersuite.google.com/

## When to Use Which?

**Use Ollama (Ctrl+Shift+G) when:**
- You want privacy
- You have no internet
- You're doing many requests
- You don't mind waiting (first time)

**Use Gemini (Ctrl+Shift+H) when:**
- You want fast responses
- You're connected to internet
- You need the latest model
- You want higher quality responses

## Troubleshooting

### "Gemini API not available"
```powershell
pip install google-generativeai
```

### "API key not configured"
- Set `GEMINI_API_KEY` in `config.py`
- Make sure the key is valid (starts with `AIza`)
- No extra spaces or quotes issues

### "API quota exceeded"
- You've hit the free tier limit
- Wait for the quota to reset (usually next minute/day)
- Check usage: https://makersuite.google.com/

### "Invalid API key"
- Get a new key: https://makersuite.google.com/app/apikey
- Make sure you copied the entire key
- Check for any typos

## Example

```python
# config.py
GEMINI_API_KEY = "AIzaSyDcX1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o"
GEMINI_MODEL = "gemini-2.0-flash-exp"
GEMINI_SYSTEM_PROMPT = "You are an SQL expert. Be concise."
```

Run the app and try both:
- **Ctrl+Shift+G** → Ollama (local, private)
- **Ctrl+Shift+H** → Gemini (cloud, fast)

Both put the result in your clipboard for easy pasting!
