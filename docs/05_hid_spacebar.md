# Schritt 5: Erste HID-Anwendung – Spacebar-Taster

In diesem Schritt verbinden wir einen physischen Taster mit dem Pico. Ein Tastendruck soll eine Leertaste (Spacebar) an den Rechner senden – so als würde man auf der Tastatur die Leertaste drücken.

## Was ist HID?

**HID** steht für *Human Interface Device* – ein USB-Standard für Eingabegeräte. Tastatur, Maus und Gamepad sind HID-Geräte. Das Betriebssystem erkennt sie automatisch, ohne Treiber.

CircuitPython meldet den Pico beim Anstecken als USB-HID-Tastatur an. Alles was der Code über `keyboard.send()` schickt, landet genauso beim Rechner als würde man eine physische Taste drücken – in jedem Programm, ohne weitere Konfiguration.

**Typische Anwendungen:**
- Präsentationssteuerung (Folie weiter/zurück)
- Barrierefreiheit (große Einzeltaste für bestimmte Aktionen)
- Gaming-Makros
- Streaming-Steuerung (Szene wechseln, Stummschalten)

## Hardware-Aufbau

### Benötigte Teile

| Bauteil | Anzahl |
|---------|--------|
| Raspberry Pi Pico | 1 |
| Taster (normally open, NO) | 1 |
| Jumperkabel | 2 |
| Breadboard (optional) | 1 |

### Schaltplan

```
3,3 V (intern)
    │
   [R]  ← interner Pull-up (aktiviert per Software)
    │
GP15 (Pin 20) ──────────┤
                        │
                    [ Taster ]
                        │
                       GND (Pin 18)
```

Beim Drücken verbindet der Taster GP15 mit GND → der Pin fällt von HIGH auf LOW.  
Im Ruhezustand hält der interne Pull-up-Widerstand den Pin auf HIGH (3,3 V).  
Ein externer Widerstand ist **nicht nötig**.

### Pinout-Referenz

| Pico-Pin | Funktion | Verwendung |
|----------|----------|------------|
| 20 | GP15 | Taster-Eingang |
| 18 | GND | Masse (eine der drei GND-Buchsen) |

Vollständiges Pinout: [Pico R3 Pinout (PDF)](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)

### Aufbau mit Breadboard

1. Pico quer über die Mittellinie des Breadboards stecken
2. Taster in das Breadboard stecken (überbrückt die Mittellinie)
3. Jumperkabel: **GP15** (Pin 20) → eine Seite des Tasters
4. Jumperkabel: **GND** (Pin 18) → andere Seite des Tasters

## Code auf den Pico laden

Die fertige Datei liegt im Repo unter [`examples/01_spacebar/code.py`](https://github.com/jvanvinkenroye/makerSQpico/blob/main/examples/01_spacebar/code.py).

**Windows:** Datei im Explorer auf `CIRCUITPY` kopieren (bestehende `code.py` ersetzen)

**macOS:**
```bash
cp examples/01_spacebar/code.py /Volumes/CIRCUITPY/code.py
```

**Linux:**
```bash
cp examples/01_spacebar/code.py /media/$USER/CIRCUITPY/code.py
```

Der Pico startet automatisch neu und führt den neuen Code aus.

## Code

```python title="examples/01_spacebar/code.py"
import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    if not button.value:
        keyboard.send(Keycode.SPACEBAR)
        time.sleep(0.3)
    time.sleep(0.01)
```

## Code-Erklärung

```python
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
```

- `usb_hid` – die USB-HID-Schnittstelle von CircuitPython (kein Download nötig, eingebaut)
- `Keyboard` – Klasse, die eine USB-Tastatur gegenüber dem Betriebssystem darstellt
- `Keycode` – enthält alle Tastencodes (`Keycode.SPACEBAR`, `Keycode.ENTER`, `Keycode.A` usw.)

```python
keyboard = Keyboard(usb_hid.devices)
```

Registriert den Pico als Tastatur beim Betriebssystem. Ab jetzt kann `keyboard.send()` Tastenanschläge senden.

```python
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
```

- `Direction.INPUT` – GP15 liest einen Signalpegel, gibt keinen aus
- `Pull.UP` – interner Widerstand zieht den Pin auf HIGH; wird LOW wenn Taster GND verbindet
- `button.value` ist `True` im Ruhezustand, `False` wenn gedrückt

```python
while True:
    if not button.value:        # False = Taster gedrückt (LOW)
        keyboard.send(Keycode.SPACEBAR)
        time.sleep(0.3)         # Entprellung
    time.sleep(0.01)            # 100 Abfragen pro Sekunde
```

### Was ist Entprellung?

Mechanische Taster „prellen": beim Drücken öffnet und schließt der Kontakt mehrfach innerhalb weniger Millisekunden, bevor er stabil liegt. Ohne Entprellung würde ein einzelner Druck 5–20 Leerzeichen senden.

`time.sleep(0.3)` pausiert die Schleife nach jedem Tastendruck für 300 ms – länger als das Prellen dauert, kürzer als ein bewusster zweiter Tastendruck.

### `send()` vs. `press()` / `release()`

| Methode | Verhalten |
|---------|-----------|
| `keyboard.send(Keycode.X)` | Drückt und lässt sofort los |
| `keyboard.press(Keycode.X)` | Hält die Taste gedrückt |
| `keyboard.release_all()` | Lässt alle gehaltenen Tasten los |

`send()` ist für einzelne Tastendrücke. `press()` + `release_all()` braucht man wenn eine Taste dauerhaft gehalten werden soll (z.B. für Wiederholung).

## Erweiterung: LED-Feedback

Die onboard-LED leuchtet, solange der Taster gedrückt ist:

```python
import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    if not button.value:
        led.value = True
        keyboard.send(Keycode.SPACEBAR)
        time.sleep(0.3)
    else:
        led.value = False
    time.sleep(0.01)
```

## Erweiterung: Andere Tasten

Einfach `Keycode.SPACEBAR` ersetzen:

```python
# Pfeiltasten
keyboard.send(Keycode.RIGHT_ARROW)

# Tastenkombination: Strg+C
keyboard.send(Keycode.CONTROL, Keycode.C)

# Medien: Play/Pause
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
cc = ConsumerControl(usb_hid.devices)
cc.send(ConsumerControlCode.PLAY_PAUSE)
```

Alle verfügbaren Keycodes: [Adafruit HID Keycode-Referenz](https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.keycode.Keycode)

## Testen

1. Texteditor öffnen (Notepad, TextEdit, gedit)
2. In das Textfeld klicken
3. Taster drücken → ein Leerzeichen erscheint

## Fehlersuche

**Kein Leerzeichen erscheint:**
- Prüfen ob `adafruit_hid` in `CIRCUITPY/lib/` vorhanden ist
- REPL öffnen und auf Fehlermeldungen prüfen
- Kabelverbindungen prüfen: GP15 ↔ Taster ↔ GND

**Viele Leerzeichen auf einmal:**
- `time.sleep(0.3)` erhöhen (z.B. auf `0.5`)

**`ImportError: no module named 'adafruit_hid'`:**
- Den Ordner `adafruit_hid` vollständig (nicht nur einzelne Dateien) nach `CIRCUITPY/lib/` kopieren

**Pico wird nicht als Tastatur erkannt:**
- USB-Verbindung prüfen (Datenkabel, nicht Ladekabel)
- Pico neu starten: USB kurz abstecken

---

[← Zurück: Blink](04_blink.md) | [Weiter: Streaming Deck →](06_streaming_deck.md)
