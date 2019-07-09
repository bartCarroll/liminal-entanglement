import time
import random
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False



def userInteracted():
    print("testing for user input...")
    return False


if __name__ == "__main__":
    print("terminal main init...")
    f = open("quotes.txt", 'r')
    quotes = f.readlines()

    # Start non-blocking keyboard listener
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
    while 1:
        print(random.choice(quotes)) # send to serial or potentially choose random sounds?
        time.sleep(10)
        if userInteracted:
            print()
