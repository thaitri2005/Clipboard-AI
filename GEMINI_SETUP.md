# 🌐 Gemini API Setup Guide

## Get Your Free Gemini API Key

1. **Visit Google AI Studio:**
   https://makersuite.google.com/app/apikey

2. **Sign in** with your Google account

3. **Click "Create API Key"**

4. **Copy your API key** (starts with `AIza...`)

## Configure the App

### 1. Install Required Packages

```powershell
pip install google-generativeai python-dotenv
```

Or install all dependencies:

```powershell
pip install -r requirements.txt
```

### 2. Create .env File

Copy the example file:

```powershell
Copy-Item .env.example .env
```

### 3. Add Your API Key to .env

Edit the `.env` file and add your actual API key:

```
GEMINI_API_KEY=AIzaSyD...your-actual-key-here...
```

**✅ SECURE:** The `.env` file is gitignored and won't be committed!

### 4. Restart the App

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
GEMINI_MODEL = "gemini-2.5-flash"

# Stronger, good for complex tasks
GEMINI_MODEL = "gemini-2.5-pro"

# Legacy model
GEMINI_MODEL = "gemini-2.0-flash-exp"
```

## Cost & Limits

**Free Tier:**
More than enough for typical use!
Check your usage: https://makersuite.google.com/

## When to Use Which?

**Use Ollama (Ctrl+Shift+G) when:**
- You want privacy
- You have no internet
- You don't mind waiting (first time)

**Use Gemini (Ctrl+Shift+H) when:**
- You want fast responses
- You're connected to internet
- You need the latest model
- You want higher quality responses

## Troubleshooting

### "Gemini API not available"

```powershell
pip install google-generativeai python-dotenv
```

Or:

```powershell
pip install -r requirements.txt
```

### "API key not configured"

- Set `GEMINI_API_KEY` in `.env` file (not `config.py`!)
- Make sure the key is valid (starts with `AIza`)
- No extra spaces or quote issues
- Example: `GEMINI_API_KEY=AIzaSyD1234567890...`

### "API quota exceeded"
- You've hit the free tier limit
- Wait for the quota to reset (usually next minute/day)
- Check usage: https://makersuite.google.com/

### "Invalid API key"
- Get a new key: https://makersuite.google.com/app/apikey
- Make sure you copied the entire key
- Check for any typos

## Example Configuration

Your `.env` file should look like:

```bash
# Gemini API Configuration
GEMINI_API_KEY=AIzaSyDcX1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o
```

You can also customize settings in `config.py`:

```python
# config.py
GEMINI_MODEL = "gemini-2.0-flash-exp"
GEMINI_SYSTEM_PROMPT = "You are an SQL expert. Be concise."
```

Run the app and try both:
- **Ctrl+Shift+G** → Ollama (local, private)
- **Ctrl+Shift+H** → Gemini (cloud, fast)

Both put the result in your clipboard for easy pasting!
