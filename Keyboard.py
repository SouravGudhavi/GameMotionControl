from pynput.keyboard import Key, Controller

keys = ["w","a","s","d",]

keyboard = Controller()

def press_key(key):
    if key in keys:
        keyboard.press(key)
    else:
        print(f"Key '{key}' not found in the mapping.")

def release_key(key):
    if key in keys:
        keyboard.release(key)
