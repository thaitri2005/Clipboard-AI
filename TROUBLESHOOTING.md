# 🔧 Troubleshooting Guide

## Enhanced Logging

The app now has **detailed logging** to help you see exactly what's happening!

When you run the app, you'll see:
- ✅ Startup confirmation
- 🎧 Keyboard listener status
- 🎯 When hotkey is detected
- 🔍 Debug info (what keys are pressed, clipboard status, Ollama communication)
- ⏱️ Timing information
- ❌ Detailed error messages with solutions

## Common Issues

### 1. "Nothing happens when I press Ctrl+Shift+G"

**Check if the app is running:**
```powershell
# You should see this when you start:
# ============================================================
# 🚀 LOCAL AI CLIPBOARD STARTED SUCCESSFULLY!
# ============================================================
```

**Test the hotkey detection:**
- The app shows `[DEBUG]` messages when keys are pressed
- Try pressing Ctrl+Shift+G - you should see: `🎯 HOTKEY DETECTED: Ctrl+Shift+G pressed!`
- If you don't see anything, the keyboard listener might not be working

**Solutions:**
1. **Run PowerShell/Terminal as Administrator** (most common fix!)
2. Check if another app is using Ctrl+Shift+G
3. Try pressing the keys slowly: Ctrl → Shift → G (hold all three)
4. Restart the application

### 2. "Ollama not found" Error

**You'll see:**
```
❌ ERROR: Ollama not found!
   The command 'ollama' is not recognized.
```

**Solutions:**
1. **Close and reopen PowerShell/Terminal** (PATH needs to refresh)
2. Test if Ollama is installed:
   ```powershell
   ollama --version
   ```
3. If not installed, install it:
   ```powershell
   winget install Ollama.Ollama
   ```
4. Manually add to PATH if needed

### 3. "Model not found" or Ollama error

**You'll see:**
```
❌ Ollama error (exit code 1)
```

**Solutions:**
1. Pull the model first:
   ```powershell
   ollama pull phi3:mini
   ```
2. Check available models:
   ```powershell
   ollama list
   ```
3. Test manually:
   ```powershell
   echo "test" | ollama run phi3:mini
   ```

### 4. "Clipboard is empty" Warning

**You'll see:**
```
⚠️  Clipboard is empty! Copy some text first (Ctrl+C)
```

**Solution:**
- Copy some text BEFORE pressing Ctrl+Shift+G
- The app processes whatever is in your clipboard

### 5. Hotkey Not Detecting

**If you see keys being pressed but hotkey not triggering:**
```
[DEBUG] Keys pressed: ctrl_l + g    # Missing Shift!
```

**Solutions:**
1. Make sure you press **all three keys**: Ctrl + Shift + G
2. Try holding them in order: Ctrl → Shift → G
3. Try using right Ctrl/Shift instead of left
4. **Run as Administrator** - Windows may block keyboard hooks

### 6. Permission/Access Errors

**For clipboard access errors:**
- Run PowerShell as Administrator
- Check antivirus isn't blocking clipboard access
- Close other clipboard managers temporarily

**For keyboard listener errors:**
- Run PowerShell as Administrator
- Windows Defender may block low-level keyboard hooks

### 7. Slow Response or Timeout

**You'll see:**
```
❌ Ollama timed out after 120 seconds
```

**Solutions:**
1. Try a smaller/faster model:
   ```powershell
   ollama pull qwen2.5-coder:1.5b
   ```
   Then edit `config.py`:
   ```python
   MODEL = "qwen2.5-coder:1.5b"
   ```

2. Increase timeout in `config.py`:
   ```python
   TIMEOUT = 300  # 5 minutes
   ```

3. Check system resources (CPU/RAM usage)

## Debug Mode

The app runs in verbose mode by default. You'll see `[DEBUG]` messages showing:
- Key presses
- Clipboard reads/writes
- Ollama communication
- Timing information

If it's too much info, edit `config.py`:
```python
VERBOSE = False  # Less output
```

## Quick Test

Run this to test everything:

```powershell
# 1. Check Ollama
ollama --version
ollama list

# 2. Test model manually
echo "SELECT * FROM users" | ollama run phi3:mini

# 3. Start app as Administrator
# Right-click PowerShell → Run as Administrator
cd D:\Local-AI-Clipboard
python clipboard_ai.py

# 4. Copy text: "Hello World"
# 5. Press Ctrl+Shift+G
# 6. Watch terminal for debug output
```

## Still Not Working?

Check the terminal output carefully - it will tell you exactly what's wrong:
- ❌ Red messages = Errors with solutions
- ⚠️ Yellow messages = Warnings
- 🔍 [DEBUG] messages = What's happening internally
- ✅ Green messages = Success

**Most common fix: Run PowerShell as Administrator!**
