"""
Local AI Clipboard - Send clipboard content to Ollama and get AI response back
Hotkey: Ctrl+Shift+G
"""

import pyperclip
import subprocess
import json
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
import sys
import time

# Try to load config, fall back to defaults
try:
    from config import MODEL, SYSTEM_PROMPT, TIMEOUT, VERBOSE
    OLLAMA_MODEL = MODEL
except ImportError:
    OLLAMA_MODEL = "llama3.2"
    SYSTEM_PROMPT = ""
    TIMEOUT = 120
    VERBOSE = True

OLLAMA_COMMAND = "ollama"

class ClipboardAI:
    def __init__(self):
        self.processing = False
        print(f"🚀 Local AI Clipboard is running!")
        print(f"📋 Using Ollama model: {OLLAMA_MODEL}")
        print(f"⌨️  Press Ctrl+Shift+G to process clipboard content")
        print(f"🛑 Press Ctrl+C to exit\n")

    def get_clipboard_content(self):
        """Get current clipboard content"""
        try:
            content = pyperclip.paste()
            if not content or content.strip() == "":
                print("⚠️  Clipboard is empty!")
                return None
            return content
        except Exception as e:
            print(f"❌ Error reading clipboard: {e}")
            return None

    def send_to_ollama(self, content):
        """Send content to Ollama and get response"""
        try:
            print(f"📤 Sending to Ollama ({OLLAMA_MODEL})...")
            if VERBOSE:
                print(f"📝 Input preview: {content[:100]}{'...' if len(content) > 100 else ''}\n")
            
            # Prepend system prompt if configured
            input_text = content
            if SYSTEM_PROMPT:
                input_text = f"{SYSTEM_PROMPT}\n\n{content}"
                if VERBOSE:
                    print(f"🎯 Using system prompt: {SYSTEM_PROMPT[:50]}{'...' if len(SYSTEM_PROMPT) > 50 else ''}\n")
            
            # Construct the ollama command
            # Using ollama run with the content as input
            process = subprocess.Popen(
                [OLLAMA_COMMAND, "run", OLLAMA_MODEL],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Send input and get output with timeout
            try:
                stdout, stderr = process.communicate(input=input_text, timeout=TIMEOUT)
            except subprocess.TimeoutExpired:
                process.kill()
                print(f"❌ Ollama timed out after {TIMEOUT} seconds")
                return None
            
            if process.returncode != 0:
                print(f"❌ Ollama error: {stderr}")
                return None
            
            response = stdout.strip()
            if response:
                print(f"✅ Received response from Ollama!")
                if VERBOSE:
                    print(f"📝 Output preview: {response[:100]}{'...' if len(response) > 100 else ''}\n")
                return response
            else:
                print("⚠️  Ollama returned empty response")
                return None
                
        except FileNotFoundError:
            print(f"❌ Ollama not found! Please make sure Ollama is installed and in your PATH")
            print(f"   Download from: https://ollama.ai/download")
            return None
        except Exception as e:
            print(f"❌ Error communicating with Ollama: {e}")
            return None

    def set_clipboard_content(self, content):
        """Set clipboard content"""
        try:
            pyperclip.copy(content)
            print("✅ Response copied to clipboard! Press Ctrl+V to paste.\n")
            return True
        except Exception as e:
            print(f"❌ Error writing to clipboard: {e}")
            return False

    def process_clipboard(self):
        """Main processing function"""
        if self.processing:
            print("⚠️  Already processing, please wait...")
            return
        
        self.processing = True
        print("\n" + "="*60)
        print("🔄 Processing clipboard content...")
        print("="*60)
        
        try:
            # Get clipboard content
            clipboard_content = self.get_clipboard_content()
            if not clipboard_content:
                return
            
            # Send to Ollama
            response = self.send_to_ollama(clipboard_content)
            if not response:
                return
            
            # Put response back in clipboard
            self.set_clipboard_content(response)
            
        finally:
            self.processing = False
            print("="*60 + "\n")

def main():
    """Main function to set up hotkey listener"""
    app = ClipboardAI()
    
    # Set to track current pressed keys
    current_keys = set()
    
    def on_press(key):
        """Handle key press"""
        try:
            current_keys.add(key)
            
            # Check for Ctrl+Shift+G
            ctrl_pressed = Key.ctrl_l in current_keys or Key.ctrl_r in current_keys
            shift_pressed = Key.shift in current_keys or Key.shift_r in current_keys
            
            # Check if 'G' is pressed
            if hasattr(key, 'char') and key.char and key.char.lower() == 'g':
                if ctrl_pressed and shift_pressed:
                    app.process_clipboard()
                    
        except AttributeError:
            pass

    def on_release(key):
        """Handle key release"""
        try:
            if key in current_keys:
                current_keys.remove(key)
        except KeyError:
            pass

    # Start listening for keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n👋 Exiting Local AI Clipboard...")
            sys.exit(0)

if __name__ == "__main__":
    main()
