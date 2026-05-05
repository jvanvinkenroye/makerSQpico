import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

BUTTON_PINS = [board.GP9, board.GP8, board.GP7, board.GP19, board.GP20, board.GP21]
KEYCODES = [
    (Keycode.CONTROL, Keycode.F7),
    (Keycode.CONTROL, Keycode.F8),
    (Keycode.CONTROL, Keycode.F9),
    (Keycode.CONTROL, Keycode.F10),
    (Keycode.CONTROL, Keycode.F11),
    (Keycode.CONTROL, Keycode.F12),
]

buttons = []
for pin in BUTTON_PINS:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN
    buttons.append(btn)

keyboard = Keyboard(usb_hid.devices)

while True:
    for btn, keys in zip(buttons, KEYCODES):
        if btn.value:
            keyboard.send(*keys)
            time.sleep(0.1)
    time.sleep(0.1)
