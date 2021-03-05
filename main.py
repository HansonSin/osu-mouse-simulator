# -*- coding: utf-8 -*-

from pynput import keyboard
from pynput.mouse import Button, Controller

mouse = Controller()

def on_press(key):
    key = str(key)
    print(key) # comment this line to stop showing every key pressed
    if key == "'z'" or key == "'x'":
        mouse.press(Button.left)
        mouse.release(Button.left)
        print("pressed")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
