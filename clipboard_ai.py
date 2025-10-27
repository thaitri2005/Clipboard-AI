"""
Local AI Clipboard - Send clipboard content to Ollama and get AI response back
Hotkey: Ctrl+Shift+G
"""

import pyperclip
import subprocess
import json
import re
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
import sys
import time

# Try to load config, fall back to defaults
try:
    from config import MODEL, SYSTEM_PROMPT, TIMEOUT, VERBOSE
    from config import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_SYSTEM_PROMPT
    OLLAMA_MODEL = MODEL
except ImportError:
    OLLAMA_MODEL = "llama3.2"
    SYSTEM_PROMPT = ""
    TIMEOUT = 120
    VERBOSE = True
    GEMINI_API_KEY = ""
    GEMINI_MODEL = "gemini-2.0-flash-exp"
    GEMINI_SYSTEM_PROMPT = ""

OLLAMA_COMMAND = "ollama"

# Import Gemini if API key is configured
if GEMINI_API_KEY:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        GEMINI_AVAILABLE = True
    except ImportError:
        print("⚠️  Warning: google-generativeai not installed. Run: pip install google-generativeai")
        GEMINI_AVAILABLE = False
else:
    GEMINI_AVAILABLE = False

class ClipboardAI:
    def __init__(self):
        self.processing = False
        self.hotkey_pressed_count = 0
        self.gemini_pressed_count = 0
        self.should_exit = False
        print("\n" + "="*60)
        print("🚀 LOCAL AI CLIPBOARD STARTED SUCCESSFULLY!")
        print("="*60)
        print(f"📋 Ollama model: {OLLAMA_MODEL}")
        print(f"⌨️  Ctrl+Shift+G - Process with Ollama (local)")
        
        if GEMINI_AVAILABLE and GEMINI_API_KEY:
            print(f"🌐 Gemini model: {GEMINI_MODEL}")
            print(f"⌨️  Ctrl+Shift+H - Process with Gemini (cloud)")
        else:
            print(f"⚠️  Gemini API: Not configured")
            print(f"💡 Set GEMINI_API_KEY in config.py to enable Ctrl+Shift+H")
        
        print(f"🛑 Exit: Press Ctrl+Shift+Q OR close this window")
        print(f"🔍 Verbose mode: {VERBOSE}")
        if SYSTEM_PROMPT:
            print(f"💬 System prompt: {SYSTEM_PROMPT[:50]}...")
        print("="*60)
        print("\n✅ Ready! Listening for keyboard input...")
        print("💡 TIP: Try pressing Ctrl+Shift+G (Ollama) or Ctrl+Shift+H (Gemini)!\n")

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
            
            # Build the prompt with system prompt if configured
            full_prompt = ""
            if SYSTEM_PROMPT:
                full_prompt += f"System: {SYSTEM_PROMPT}\n\n"
            full_prompt += f"User: {content}\n\nAssistant:"
            
            # Add current input
            full_prompt += f"User: {content}\n\nAssistant:"
            
            # Construct the ollama command
            # Disable streaming and use --nowordwrap for clean output
            if VERBOSE:
                print(f"🔍 [DEBUG] Executing: {OLLAMA_COMMAND} run {OLLAMA_MODEL} --nowordwrap")
                print(f"⏳ Waiting for Ollama response (timeout: {TIMEOUT}s)...\n")
            
            # Set environment to disable streaming animations
            env = subprocess.os.environ.copy()
            env['TERM'] = 'dumb'  # Disable ANSI escape codes
            
            process = subprocess.Popen(
                [OLLAMA_COMMAND, "run", OLLAMA_MODEL, "--nowordwrap"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                errors='replace',  # Replace undecodable characters instead of crashing
                env=env
            )
            
            # Send input and get output with timeout
            try:
                stdout, stderr = process.communicate(input=full_prompt, timeout=TIMEOUT)
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
                print(f"   Error details: {stderr[:500]}")  # Limit error message length
                print(f"\n💡 Troubleshooting:")
                print(f"   1. Check if Ollama is running: ollama list")
                print(f"   2. Check if model exists: ollama pull {OLLAMA_MODEL}")
                print(f"   3. Test manually: echo 'test' | ollama run {OLLAMA_MODEL}")
                print(f"   4. Try restarting Ollama service")
                return None
            
            # Strip ANSI escape codes from response
            response = stdout.strip()
            
            # Remove ANSI escape sequences (like ←[?25l, ←[1G, etc.)
            # Pattern matches ANSI escape codes
            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            response = ansi_escape.sub('', response)
            response = response.strip()
            
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
            print(f"❌ Error communicating with Ollama: {e}")
            import traceback
            if VERBOSE:
                print("\n🔍 [DEBUG] Full traceback:")
                traceback.print_exc()
            return None
    
    def send_to_gemini(self, content):
        """Send content to Gemini API and get response"""
        try:
            if not GEMINI_AVAILABLE:
                print(f"❌ Gemini API not available!")
                print(f"💡 Install: pip install google-generativeai")
                print(f"💡 Set GEMINI_API_KEY in config.py")
                return None
            
            if not GEMINI_API_KEY:
                print(f"❌ Gemini API key not configured!")
                print(f"💡 Get your key from: https://makersuite.google.com/app/apikey")
                print(f"💡 Set GEMINI_API_KEY in config.py")
                return None
            
            print(f"📤 Sending to Gemini API ({GEMINI_MODEL})...")
            if VERBOSE:
                print(f"📝 Input preview: {content[:100]}{'...' if len(content) > 100 else ''}")
                print(f"🔍 [DEBUG] Input length: {len(content)} characters\n")
            
            # System prompt for Gemini
            system_prompt = GEMINI_SYSTEM_PROMPT if GEMINI_SYSTEM_PROMPT else SYSTEM_PROMPT
            
            if VERBOSE:
                print(f"🔍 [DEBUG] Initializing Gemini model...")
            
            # Initialize Gemini model
            model = genai.GenerativeModel(GEMINI_MODEL)
            
            # Build the prompt with system prompt if configured
            full_prompt = ""
            if system_prompt:
                full_prompt += f"System: {system_prompt}\n\n"
            full_prompt += f"User: {content}\n\nAssistant:"
            
            if VERBOSE:
                print(f"⏳ Waiting for Gemini response (cloud API)...\n")
            
            # Generate response
            response = model.generate_content(full_prompt)
            
            if response and response.text:
                result = response.text.strip()
                print(f"✅ Received response from Gemini!")
                if VERBOSE:
                    print(f"📝 Output length: {len(result)} characters")
                    print(f"📝 Output preview: {result[:150]}{'...' if len(result) > 150 else ''}\n")
                return result
            else:
                print("⚠️  Gemini returned empty response")
                return None
                
        except Exception as e:
            print(f"❌ Error communicating with Gemini API: {e}")
            print(f"\n💡 Troubleshooting:")
            print(f"   1. Check your API key is valid")
            print(f"   2. Check your internet connection")
            print(f"   3. Verify API quota: https://makersuite.google.com/")
            import traceback
            if VERBOSE:
                print("\n🔍 [DEBUG] Full traceback:")
                traceback.print_exc()
            return None

    def set_clipboard_content(self, content):
        """Set clipboard content with retry logic"""
        import time
        max_retries = 5
        retry_delay = 0.5  # seconds
        
        for attempt in range(max_retries):
            try:
                if VERBOSE and attempt > 0:
                    print(f"🔍 [DEBUG] Retry attempt {attempt + 1}/{max_retries}...")
                
                if VERBOSE:
                    print(f"🔍 [DEBUG] Writing {len(content)} characters to clipboard...")
                
                # Try to copy to clipboard
                pyperclip.copy(content)
                
                # Verify it was copied correctly
                time.sleep(0.1)  # Small delay to ensure clipboard is updated
                copied = pyperclip.paste()
                
                if copied == content:
                    print("✅ Response copied to clipboard! Press Ctrl+V to paste.\n")
                    if VERBOSE:
                        print("🔍 [DEBUG] Clipboard write verified successfully!")
                    return True
                else:
                    if VERBOSE:
                        print(f"⚠️  [DEBUG] Clipboard verification failed, retrying...")
                    raise Exception("Clipboard verification failed")
                    
            except Exception as e:
                if attempt < max_retries - 1:
                    if VERBOSE:
                        print(f"⚠️  [DEBUG] Clipboard access failed: {e}")
                        print(f"⏳ Waiting {retry_delay}s before retry...")
                    time.sleep(retry_delay)
                    retry_delay *= 1.5  # Exponential backoff
                else:
                    print(f"❌ Error writing to clipboard after {max_retries} attempts: {e}")
                    print(f"💡 TIP: Close other clipboard managers or wait a moment and try again")
                    if VERBOSE:
                        import traceback
                        traceback.print_exc()
                    return False
        
        return False

    def process_clipboard(self, use_gemini=False):
        """Main processing function"""
        if self.processing:
            print("⚠️  Already processing, please wait...")
            return
        
        self.processing = True
        
        if use_gemini:
            self.gemini_pressed_count += 1
            mode_name = "GEMINI API"
            request_num = self.gemini_pressed_count
        else:
            self.hotkey_pressed_count += 1
            mode_name = "OLLAMA"
            request_num = self.hotkey_pressed_count
        
        print("\n" + "="*60)
        print(f"🔄 PROCESSING WITH {mode_name} (Request #{request_num})")
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
            
            # Send to AI (Ollama or Gemini)
            if use_gemini:
                if VERBOSE:
                    print("🔍 [DEBUG] Step 2/3: Sending to Gemini API...")
                response = self.send_to_gemini(clipboard_content)
                if not response:
                    print("❌ Aborted: No response from Gemini")
                    return
            else:
                if VERBOSE:
                    print("🔍 [DEBUG] Step 2/3: Sending to Ollama...")
                response = self.send_to_ollama(clipboard_content)
                if not response:
                    print("❌ Aborted: No response from Ollama")
                    return
            
            # Put response back in clipboard
            if VERBOSE:
                print("🔍 [DEBUG] Step 3/3: Writing to clipboard...")
            
            # Small delay to ensure clipboard is not locked by previous operation
            time.sleep(0.2)
            
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
            if use_gemini:
                print("✅ Ready for next request. Press Ctrl+Shift+H (Gemini) or Ctrl+Shift+G (Ollama)!\n")
            else:
                print("✅ Ready for next request. Press Ctrl+Shift+G (Ollama) or Ctrl+Shift+H (Gemini)!\n")

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
            if VERBOSE:
                key_names = []
                for k in current_keys:
                    if hasattr(k, 'char') and k.char:
                        key_names.append(f"'{k.char}'")
                    elif hasattr(k, 'name'):
                        key_names.append(k.name)
                    elif hasattr(k, 'vk'):  # Virtual key code
                        key_names.append(f"vk_{k.vk}")
                    else:
                        key_names.append(str(k).replace('Key.', ''))
                if len(key_names) > 0:
                    print(f"🔍 [DEBUG] Keys currently held: {' + '.join(key_names)}")
            
            # Check for Ctrl+Shift modifiers
            ctrl_pressed = Key.ctrl_l in current_keys or Key.ctrl_r in current_keys or Key.ctrl in current_keys
            shift_pressed = Key.shift in current_keys or Key.shift_r in current_keys or Key.shift_l in current_keys
            
            # Check for G, H, Q keys using virtual key codes (most reliable)
            g_pressed = False
            h_pressed = False
            q_pressed = False
            
            # Only check the key that was just pressed (not all held keys)
            # Method 1: Check virtual key code (most reliable for hotkeys)
            if hasattr(key, 'vk'):
                # G key = virtual key 71 (0x47)
                # H key = virtual key 72 (0x48)
                # Q key = virtual key 81 (0x51)
                if key.vk == 71 or key.vk == 0x47:
                    g_pressed = True
                    if VERBOSE:
                        print(f"🔍 [DEBUG] G key detected via virtual key code!")
                elif key.vk == 72 or key.vk == 0x48:
                    h_pressed = True
                    if VERBOSE:
                        print(f"🔍 [DEBUG] H key detected via virtual key code!")
                elif key.vk == 81 or key.vk == 0x51:
                    q_pressed = True
                    if VERBOSE:
                        print(f"🔍 [DEBUG] Q key detected via virtual key code!")
            
            # Method 2: Fallback to character check (works on some systems)
            if not (g_pressed or h_pressed or q_pressed):
                if hasattr(key, 'char') and key.char:
                    char_lower = key.char.lower()
                    if char_lower == 'g':
                        g_pressed = True
                    elif char_lower == 'h':
                        h_pressed = True
                    elif char_lower == 'q':
                        q_pressed = True
            
            # Method 3: Fallback to name attribute
            if not (g_pressed or h_pressed or q_pressed):
                if hasattr(key, 'name'):
                    if key.name.lower() == 'g':
                        g_pressed = True
                    elif key.name.lower() == 'h':
                        h_pressed = True
                    elif key.name.lower() == 'q':
                        q_pressed = True
            
            if VERBOSE and (g_pressed or h_pressed or q_pressed):
                print(f"🔍 [DEBUG] Key detected: G={g_pressed}, H={h_pressed}, Q={q_pressed}, Ctrl={ctrl_pressed}, Shift={shift_pressed}")
            
            # Check for Ctrl+Shift+Q to exit
            if q_pressed and ctrl_pressed and shift_pressed:
                print("\n👋 Exit hotkey (Ctrl+Shift+Q) detected!")
                print("Shutting down...")
                app.should_exit = True
                import os
                os._exit(0)
            
            # Check for Ctrl+Shift+H to process with Gemini
            if h_pressed and ctrl_pressed and shift_pressed:
                print("\n🎯 HOTKEY DETECTED: Ctrl+Shift+H pressed! (Gemini mode)")
                app.process_clipboard(use_gemini=True)
            
            # Check for Ctrl+Shift+G to process with Ollama
            if g_pressed and ctrl_pressed and shift_pressed:
                print("\n🎯 HOTKEY DETECTED: Ctrl+Shift+G pressed! (Ollama mode)")
                app.process_clipboard(use_gemini=False)
                    
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
        print("🔍 [DEBUG] Listening for:")
        print("🔍 [DEBUG]   - Ctrl+Shift+G (Ollama)")
        print("🔍 [DEBUG]   - Ctrl+Shift+H (Gemini)")
        print("🔍 [DEBUG]   - Ctrl+Shift+Q (exit)")
        print("🔍 [DEBUG] Press keys to see them detected")
        print("🔍 [DEBUG] Or just close the terminal window to exit\n")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n👋 Exiting Local AI Clipboard...")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Listener error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
