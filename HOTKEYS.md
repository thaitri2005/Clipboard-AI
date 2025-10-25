# ⌨️ Hotkey Reference

## Active Hotkeys

### Ctrl+Shift+G - Process Clipboard
**Main function** - Sends clipboard content to AI and returns the result

**How to use:**
1. Copy text (Ctrl+C)
2. Press **Ctrl+Shift+G**
3. Wait for processing
4. Paste result (Ctrl+V)

**Debug output:**
```
🎯 HOTKEY DETECTED: Ctrl+Shift+G pressed!
```

### Ctrl+Shift+Q - Exit Application
**Exit the app cleanly**

**How to use:**
- Press **Ctrl+Shift+Q** to shut down the application
- Or just close the terminal window

**Debug output:**
```
👋 Exit hotkey (Ctrl+Shift+Q) detected!
Shutting down...
```

## Troubleshooting Hotkeys

### Keys Not Being Detected

If you see:
```
🔍 [DEBUG] Keys currently held: shift + ctrl_l
```
But missing the 'G' character, try:

1. **Press keys in order and hold:**
   - Press and hold **Ctrl**
   - While holding Ctrl, press and hold **Shift**
   - While holding both, press **G**

2. **Try different timing:**
   - Press all three keys quickly
   - OR press them slowly and deliberately

3. **Try right-side keys:**
   - Right Ctrl + Right Shift + G

4. **Run as Administrator** (most important!)
   - Right-click PowerShell → "Run as Administrator"
   - This fixes most keyboard detection issues

### Verbose Debug Output

The app shows you exactly what keys it detects:
```
🔍 [DEBUG] Keys currently held: 'g' + ctrl_l + shift
🔍 [DEBUG] Key detected: G=True, Q=False, Ctrl=True, Shift=True
🎯 HOTKEY DETECTED: Ctrl+Shift+G pressed!
```

If you see `G=True, Ctrl=True, Shift=True` but the hotkey doesn't trigger, there's a bug - let me know!

## Alternative: Disable Verbose Mode

If the debug output is too much, edit `config.py`:
```python
VERBOSE = False
```

You'll still see the important messages like "HOTKEY DETECTED" but not all the debug info.
