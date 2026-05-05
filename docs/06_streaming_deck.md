# Schritt 6: Streaming Deck – 6-Tasten-Macro-Keyboard

In diesem Schritt bauen wir ein vollständiges Streaming Deck: 6 physische Tasten senden je eine Tastenkombination an den Rechner. Das Gehäuse lässt sich mit dem Lasercutter fertigen, die Tastenaufsätze mit dem 3D-Drucker.

## Hardware

| Bauteil | Anzahl |
|---------|--------|
| Raspberry Pi Pico | 1 |
| Taster (normally open) | 6 |
| Jumperkabel | 12 |
| Breadboard oder Lasercutter-Gehäuse | 1 |

## Verdrahtung

Anders als beim Spacebar-Beispiel verwenden wir hier **Pull-Down**-Widerstände: der Pin liegt im Ruhezustand auf LOW (0 V) und wird beim Drücken auf HIGH (3,3 V) gezogen. Daher muss eine Seite jedes Tasters an **3,3 V** (nicht GND).

| Taste | GPIO | Pico-Pin | Tastenkombination |
|-------|------|----------|------------------|
| 1 | GP9 | 12 | Ctrl + F7 |
| 2 | GP8 | 11 | Ctrl + F8 |
| 3 | GP7 | 10 | Ctrl + F9 |
| 4 | GP19 | 25 | Ctrl + F10 |
| 5 | GP20 | 26 | Ctrl + F11 |
| 6 | GP21 | 27 | Ctrl + F12 |

Vollständiges Pinout: [Pico R3 Pinout (PDF)](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)

## Code auf den Pico laden

Die fertige Datei liegt im Repo unter [`examples/02_streaming_deck/code.py`](https://github.com/jvanvinkenroye/makerSQpico/blob/main/examples/02_streaming_deck/code.py).

```bash
# macOS
cp examples/02_streaming_deck/code.py /Volumes/CIRCUITPY/code.py

# Linux
cp examples/02_streaming_deck/code.py /media/$USER/CIRCUITPY/code.py
```

## Code

```python title="examples/02_streaming_deck/code.py"
import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

btn1_pin = board.GP9
btn2_pin = board.GP8
btn3_pin = board.GP7
btn4_pin = board.GP19
btn5_pin = board.GP20
btn6_pin = board.GP21

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)

while True:
    if btn1.value:
        keyboard.send(Keycode.CONTROL, Keycode.F7)
        time.sleep(0.1)
    if btn2.value:
        keyboard.send(Keycode.CONTROL, Keycode.F8)
        time.sleep(0.1)
    if btn3.value:
        keyboard.send(Keycode.CONTROL, Keycode.F9)
        time.sleep(0.1)
    if btn4.value:
        keyboard.send(Keycode.CONTROL, Keycode.F10)
        time.sleep(0.1)
    if btn5.value:
        keyboard.send(Keycode.CONTROL, Keycode.F11)
        time.sleep(0.1)
    if btn6.value:
        keyboard.send(Keycode.CONTROL, Keycode.F12)
        time.sleep(0.1)
    time.sleep(0.1)
```

## Code-Erklärung: Pull-Down vs. Pull-Up

Im Spacebar-Beispiel haben wir `Pull.UP` genutzt – der Pin ist im Ruhezustand HIGH und wird beim Drücken LOW. Deshalb war die Bedingung `if not btn.value`.

Hier verwenden wir `Pull.DOWN` – der Pin ist im Ruhezustand LOW und wird beim Drücken HIGH. Die Bedingung lautet daher einfach `if btn.value`.

```python
btn1.pull = digitalio.Pull.DOWN   # Ruhezustand: LOW (False)
                                   # Gedrückt:    HIGH (True)

if btn1.value:                     # True = gedrückt
    keyboard.send(Keycode.CONTROL, Keycode.F7)
```

`keyboard.send()` mit mehreren Keycodes drückt alle Tasten gleichzeitig – ideal für Tastenkombinationen wie Ctrl+F7.

## Tastenkombinationen anpassen

Die Tastenkombinationen lassen sich frei ändern. Alle verfügbaren Keycodes finden sich in der [Adafruit HID Keycode-Referenz](https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.keycode.Keycode).

Beispiele:

```python
# Stummschalten (Teams/Zoom)
keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)

# Screenshot
keyboard.send(Keycode.COMMAND, Keycode.SHIFT, Keycode.FOUR)   # macOS
keyboard.send(Keycode.WINDOWS, Keycode.SHIFT, Keycode.S)       # Windows

# Mediensteuerung
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)
cc.send(ConsumerControlCode.PLAY_PAUSE)
```

## Gehäuse: Lasercutter

Die SVG-Dateien für das Gehäuse liegen im Repo:

- [`docs/assets/keypad_box.svg`](https://github.com/jvanvinkenroye/makerSQpico/blob/main/docs/assets/keypad_box.svg) – Gehäuse
- [`docs/assets/keypad_keyholder.svg`](https://github.com/jvanvinkenroye/makerSQpico/blob/main/docs/assets/keypad_keyholder.svg) – Tastenhalterung

### Vorbereitung

[Inkscape herunterladen](https://inkscape.org/release/)

### Anleitung

1. SVG-Datei in Inkscape öffnen
2. Maße prüfen und ggf. anpassen
3. Datei an den Lasercutter übergeben

## Tastenaufsätze: 3D-Druck

### Vorbereitung

- [TinkerCAD](https://www.tinkercad.com/dashboard) – Online-Tool, kein Download nötig
- [PrusaSlicer herunterladen](https://www.prusa3d.com/de/page/prusaslicer_424/)

### Anleitung

1. Design in TinkerCAD kopieren und anpassen
2. Als STL exportieren
3. In PrusaSlicer importieren
4. Druckerprofil wählen (MK3S), PLA auswählen
5. Slicen und G-Code auf SD-Karte exportieren
6. SD-Karte in den Drucker, Datei auswählen und drucken
