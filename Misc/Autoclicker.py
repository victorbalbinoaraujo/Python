# pip install pynput
# pip install keyboard
import time
from pynput import keyboard
from pynput.mouse import Button, Controller
import keyboard

mouse = Controller()
# You can check your mouse position by creating an infinite loop printing the position of your mouse. Then, choose where you want
# to auto click and set the coordinates.
#while True:
#    print(mouse.position)
mouse.position = (1023, 965) # Change this values accordingly to your need.
while True:
    if keyboard.is_pressed('q'): # Hold q to stop.
        print("Exit")
        break
    time.sleep(0.01) # Seconds. It may break if it is TOO fast.
    mouse.click(Button.left, 1)