# Schritt 4: Erste HID-Anwendung – Spacebar-Taster

In diesem Schritt verbinden wir einen physischen Taster mit dem Pico. Ein Tastendruck soll eine Leertaste (Spacebar) an den Rechner senden – so als würde man auf der Tastatur die Leertaste drücken.

## Hardware-Aufbau

### Benötigte Teile

- Raspberry Pi Pico
- 1 Taster (Druckknopf, normally open)
- 2 Jumperkabel

### Schaltplan

```
Pico GP15 (Pin 20) ----[ Taster ]---- GND (Pin 18 oder 23 oder 38)
```

Einen Widerstand braucht man **nicht** – der interne Pull-up-Widerstand des Pico hält den Pin auf HIGH (3,3 V), bis der Taster gedrückt wird und GP15 mit GND verbindet.

### Pinout-Referenz (relevante Pins)

| Pico-Pin | Funktion | Verwendung |
|----------|----------|------------|
| 20       | GP15     | Taster-Eingang |
| 18       | GND      | Masse |

Vollständiges Pinout: https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf

### Aufbau mit Breadboard

1. Pico in das Breadboard stecken (über die Mittellinie)
2. Taster ebenfalls ins Breadboard stecken
3. Jumperkabel: Pico **GP15** (Pin 20) → eine Seite des Tasters
4. Jumperkabel: Pico **GND** (Pin 18) → andere Seite des Tasters

## Code auf den Pico laden

Die fertige Datei liegt unter [`../examples/01_spacebar/code.py`](../examples/01_spacebar/code.py).

Kopiere die Datei auf das `CIRCUITPY`-Laufwerk und benenne sie `code.py`:

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

## Code-Erklärung

```python
import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
```

- `board` – gibt Zugriff auf die Pin-Namen des Pico (`board.GP15`)
- `digitalio` – digitale Ein-/Ausgabe für GPIO-Pins
- `usb_hid` – USB-HID-Schnittstelle (in CircuitPython eingebaut)
- `Keyboard`, `Keycode` – Tastatur-Klasse und Tastencodes aus `adafruit_hid`

```python
keyboard = Keyboard(usb_hid.devices)
```

Erstellt ein Tastatur-Objekt, das sich gegenüber dem Betriebssystem als USB-Tastatur ausgibt.

```python
button = digitalio.DigitalInOut(board.GP15)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
```

- GP15 wird als Eingang konfiguriert
- `Pull.UP` aktiviert den internen Pull-up-Widerstand
- `button.value` ist `True` (HIGH) im Ruhezustand, `False` (LOW) wenn gedrückt

```python
while True:
    if not button.value:        # Taster gedrückt (LOW)
        keyboard.send(Keycode.SPACEBAR)
        time.sleep(0.3)         # Entprellung: 300 ms warten
    time.sleep(0.01)            # Schleife 100x pro Sekunde
```

- `keyboard.send()` drückt und lässt eine Taste in einem Schritt los
- `time.sleep(0.3)` verhindert, dass ein einzelner Tastendruck als mehrere Leerzeichen registriert wird (Entprellung)

## Testen

1. Einen Texteditor öffnen (z.B. Notepad, TextEdit, gedit)
2. In das Textfeld klicken
3. Taster drücken → ein Leerzeichen erscheint im Textfeld

## Fehlersuche

**Kein Leerzeichen erscheint:**
- Prüfen ob `adafruit_hid` in `CIRCUITPY/lib/` vorhanden ist
- REPL öffnen (serielles Terminal) und auf Fehlermeldungen prüfen
- Kabelverbindungen prüfen (GP15 ↔ Taster ↔ GND)

**Endlose Leerzeichen:**
- `time.sleep(0.3)` nach `keyboard.send()` erhöhen

**`ImportError: no module named 'adafruit_hid'`:**
- Den Ordner `adafruit_hid` vollständig (nicht nur einzelne Dateien) nach `CIRCUITPY/lib/` kopieren

**Pico reagiert nicht:**
- USB-Verbindung prüfen (Datenkabel, nicht Ladekabel)
- Pico-Reset: kurz USB abstecken und wieder anstecken

## Erweiterungsideen

- Mehrere Taster für verschiedene Tasten (z.B. Pfeiltasten, Enter)
- LED-Feedback beim Tastendruck (onboard-LED an `board.LED`)
- Medientasten (Play/Pause, Lautstärke) mit `ConsumerControl` aus `adafruit_hid`
