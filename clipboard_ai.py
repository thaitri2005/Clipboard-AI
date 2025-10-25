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
        self.hotkey_pressed_count = 0
        print("\n" + "="*60)
        print("🚀 LOCAL AI CLIPBOARD STARTED SUCCESSFULLY!")
        print("="*60)
        print(f"📋 Using Ollama model: {OLLAMA_MODEL}")
        print(f"⌨️  Hotkey: Ctrl+Shift+G")
        print(f"🛑 Stop: Ctrl+C in this terminal")
        print(f"🔍 Verbose mode: {VERBOSE}")
        if SYSTEM_PROMPT:
            print(f"💬 System prompt: {SYSTEM_PROMPT[:50]}...")
        print("="*60)
        print("\n✅ Ready! Listening for keyboard input...")
        print("� TIP: Try pressing Ctrl+Shift+G now to test!\n")

    def get_clipboard_content(self):
        """Get current clipboard content"""
        try:
            if VERBOSE:
                print("🔍 [DEBUG] Reading clipboard...")
            content = pyperclip.paste()
            if not content or content.strip() == "":
                print("⚠️  Clipboard is empty! Copy some text first (Ctrl+C)")
                return None
            if VERBOSE:
                print(f"✅ [DEBUG] Clipboard read successfully ({len(content)} characters)")
            return content
        except Exception as e:
            print(f"❌ Error reading clipboard: {e}")
            import traceback
            if VERBOSE:
                traceback.print_exc()
            return None

    def send_to_ollama(self, content):
        """Send content to Ollama and get response"""
        try:
            print(f"📤 Sending to Ollama ({OLLAMA_MODEL})...")
            if VERBOSE:
                print(f"📝 Input preview: {content[:100]}{'...' if len(content) > 100 else ''}")
                print(f"🔍 [DEBUG] Input length: {len(content)} characters\n")
            
            # Prepend system prompt if configured
            input_text = content
            if SYSTEM_PROMPT:
                input_text = f"{SYSTEM_PROMPT}\n\n{content}"
                if VERBOSE:
                    print(f"🎯 Using system prompt: {SYSTEM_PROMPT[:50]}{'...' if len(SYSTEM_PROMPT) > 50 else ''}\n")
            
            # Construct the ollama command
            if VERBOSE:
                print(f"🔍 [DEBUG] Executing: {OLLAMA_COMMAND} run {OLLAMA_MODEL}")
                print(f"⏳ Waiting for Ollama response (timeout: {TIMEOUT}s)...\n")
            
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
                print(f"💡 Try increasing TIMEOUT in config.py or use a smaller model")
                return None
            
            if VERBOSE:
                print(f"🔍 [DEBUG] Process return code: {process.returncode}")
                if stderr:
                    print(f"🔍 [DEBUG] Stderr: {stderr[:200]}")
            
            if process.returncode != 0:
                print(f"❌ Ollama error (exit code {process.returncode})")
                print(f"   Error details: {stderr}")
                print(f"\n💡 Troubleshooting:")
                print(f"   1. Check if Ollama is running: ollama list")
                print(f"   2. Check if model exists: ollama pull {OLLAMA_MODEL}")
                print(f"   3. Test manually: echo 'test' | ollama run {OLLAMA_MODEL}")
                return None
            
            response = stdout.strip()
            if response:
                print(f"✅ Received response from Ollama!")
                if VERBOSE:
                    print(f"📝 Output length: {len(response)} characters")
                    print(f"📝 Output preview: {response[:150]}{'...' if len(response) > 150 else ''}\n")
                return response
            else:
                print("⚠️  Ollama returned empty response")
                return None
                
        except FileNotFoundError:
            print(f"\n❌ ERROR: Ollama not found!")
            print(f"   The command '{OLLAMA_COMMAND}' is not recognized.")
            print(f"\n💡 Solutions:")
            print(f"   1. Close and reopen PowerShell/Terminal")
            print(f"   2. Check if Ollama is installed: ollama --version")
            print(f"   3. Install Ollama: https://ollama.ai/download")
            print(f"   4. Make sure Ollama is in your PATH\n")
            return None
        except Exception as e:
            print(f"❌ Unexpected error communicating with Ollama: {e}")
            import traceback
            if VERBOSE:
                print("\n🔍 [DEBUG] Full traceback:")
                traceback.print_exc()
            return None

    def set_clipboard_content(self, content):
        """Set clipboard content"""
        try:
            if VERBOSE:
                print(f"🔍 [DEBUG] Writing {len(content)} characters to clipboard...")
            pyperclip.copy(content)
            print("✅ Response copied to clipboard! Press Ctrl+V to paste.\n")
            if VERBOSE:
                print("🔍 [DEBUG] Clipboard write successful!")
            return True
        except Exception as e:
            print(f"❌ Error writing to clipboard: {e}")
            import traceback
            if VERBOSE:
                traceback.print_exc()
            return False

    def process_clipboard(self):
        """Main processing function"""
        if self.processing:
            print("⚠️  Already processing, please wait...")
            return
        
        self.processing = True
        self.hotkey_pressed_count += 1
        
        print("\n" + "="*60)
        print(f"🔄 PROCESSING CLIPBOARD (Request #{self.hotkey_pressed_count})")
        print("="*60)
        
        import time
        start_time = time.time()
        
        try:
            # Get clipboard content
            if VERBOSE:
                print("🔍 [DEBUG] Step 1/3: Reading clipboard...")
            clipboard_content = self.get_clipboard_content()
            if not clipboard_content:
                print("❌ Aborted: No clipboard content")
                return
            
            # Send to Ollama
            if VERBOSE:
                print("🔍 [DEBUG] Step 2/3: Sending to Ollama...")
            response = self.send_to_ollama(clipboard_content)
            if not response:
                print("❌ Aborted: No response from Ollama")
                return
            
            # Put response back in clipboard
            if VERBOSE:
                print("🔍 [DEBUG] Step 3/3: Writing to clipboard...")
            self.set_clipboard_content(response)
            
            elapsed = time.time() - start_time
            print(f"⏱️  Total time: {elapsed:.2f} seconds")
            
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            import traceback
            if VERBOSE:
                traceback.print_exc()
        finally:
            self.processing = False
            print("="*60)
            print("✅ Ready for next request. Press Ctrl+Shift+G again!\n")

def main():
    """Main function to set up hotkey listener"""
    app = ClipboardAI()
    
    # Set to track current pressed keys
    current_keys = set()
    
    def on_press(key):
        """Handle key press"""
        try:
            current_keys.add(key)
            
            # Debug: Show what keys are pressed if in verbose mode
            if VERBOSE and len(current_keys) > 1:
                key_names = []
                for k in current_keys:
                    if hasattr(k, 'char') and k.char:
                        key_names.append(k.char)
                    else:
                        key_names.append(str(k).replace('Key.', ''))
                if len(key_names) > 1:  # Only show combinations
                    print(f"🔍 [DEBUG] Keys pressed: {' + '.join(key_names)}")
            
            # Check for Ctrl+Shift+G
            ctrl_pressed = Key.ctrl_l in current_keys or Key.ctrl_r in current_keys
            shift_pressed = Key.shift in current_keys or Key.shift_r in current_keys
            
            # Check if 'G' is pressed
            if hasattr(key, 'char') and key.char and key.char.lower() == 'g':
                if ctrl_pressed and shift_pressed:
                    print("🎯 HOTKEY DETECTED: Ctrl+Shift+G pressed!")
                    app.process_clipboard()
                elif VERBOSE:
                    print(f"🔍 [DEBUG] 'G' pressed but missing: Ctrl={ctrl_pressed}, Shift={shift_pressed}")
                    
        except AttributeError:
            pass
        except Exception as e:
            print(f"❌ Error in key press handler: {e}")
            if VERBOSE:
                import traceback
                traceback.print_exc()

    def on_release(key):
        """Handle key release"""
        try:
            if key in current_keys:
                current_keys.remove(key)
        except KeyError:
            pass
        except Exception as e:
            if VERBOSE:
                print(f"🔍 [DEBUG] Error in key release handler: {e}")

    # Start listening for keyboard events
    print("🎧 Keyboard listener started...")
    if VERBOSE:
        print("🔍 [DEBUG] Listening for Ctrl+Shift+G combination...")
        print("🔍 [DEBUG] Try pressing keys to see them detected\n")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n👋 Exiting Local AI Clipboard...")
            sys.exit(0)

if __name__ == "__main__":
    main()
