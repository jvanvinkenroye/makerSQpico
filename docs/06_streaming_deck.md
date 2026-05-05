# Schritt 6: Streaming Deck – 6-Tasten-Macro-Keyboard

In diesem Schritt bauen wir ein vollständiges Streaming Deck: 6 physische Tasten senden je eine Tastenkombination an den Rechner. Das Gehäuse lässt sich mit dem Lasercutter fertigen, die Tastenaufsätze mit dem 3D-Drucker.

## Was ist ein Streaming Deck?

Ein Streaming Deck ist ein Eingabegerät mit frei belegbaren Tasten – jede Taste löst eine Tastenkombination oder Aktion aus. Ursprünglich für Streamer entwickelt (Szene wechseln, Stummschalten, Effekte aktivieren), lässt es sich für beliebige Anwendungen nutzen:

- **OBS / Streamlabs** – Szenen wechseln, Aufnahme starten/stoppen
- **Zoom / Teams** – Stummschalten, Kamera ein/aus, Hand heben
- **Video-Schnitt** – Schnittmarken setzen, Effekte anwenden
- **Präsentationen** – Folie vor/zurück, Laser-Pointer aktivieren
- **Eigene Makros** – beliebige Tastenkombinationen

## Hardware

| Bauteil | Anzahl |
|---------|--------|
| Raspberry Pi Pico | 1 |
| Taster (normally open, NO) | 6 |
| Jumperkabel | 12 |
| Breadboard oder Lasercutter-Gehäuse | 1 |

## Verdrahtung

Dieses Beispiel nutzt **Pull-Down** statt Pull-Up wie beim Spacebar-Beispiel. Der Unterschied:

| | Pull-Up | Pull-Down |
|-|---------|-----------|
| Ruhezustand | HIGH (3,3 V) | LOW (0 V) |
| Gedrückt | LOW (GND) | HIGH (3,3 V) |
| Taster verbindet | Pin mit GND | Pin mit 3,3 V |
| Bedingung im Code | `if not btn.value` | `if btn.value` |

Jeder Taster hat eine Seite am GPIO-Pin, die andere Seite an **3,3 V** (Pin 36).

### Pinbelegung

| Taste | GPIO | Pico-Pin | Tastenkombination |
|-------|------|----------|------------------|
| 1 | GP9 | 12 | Ctrl + F7 |
| 2 | GP8 | 11 | Ctrl + F8 |
| 3 | GP7 | 10 | Ctrl + F9 |
| 4 | GP19 | 25 | Ctrl + F10 |
| 5 | GP20 | 26 | Ctrl + F11 |
| 6 | GP21 | 27 | Ctrl + F12 |
| – | 3,3 V | 36 | Versorgung für alle Taster |

Vollständiges Pinout: [Pico R3 Pinout (PDF)](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)

### Schaltplan (je Taster)

```
3,3 V (Pin 36) ──────── [ Taster ] ──────── GP7/8/9/19/20/21
                                                    │
                                               Pull-Down (intern)
                                                    │
                                                   GND
```

## Code auf den Pico laden

Die fertige Datei liegt im Repo unter [`examples/02_streaming_deck/code.py`](https://github.com/jvanvinkenroye/makerSQpico/blob/main/examples/02_streaming_deck/code.py).

**Windows:** Datei im Explorer auf `CIRCUITPY` kopieren (bestehende `code.py` ersetzen)

**macOS:**
```bash
cp examples/02_streaming_deck/code.py /Volumes/CIRCUITPY/code.py
```

**Linux:**
```bash
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
```

## Code-Erklärung

### Listen statt Einzelvariablen

```python
BUTTON_PINS = [board.GP9, board.GP8, board.GP7, ...]
KEYCODES    = [(Keycode.CONTROL, Keycode.F7), ...]
```

Statt 6 einzelner Variablen (`btn1`, `btn2`, …) nutzen wir Listen. Das macht den Code kürzer und einfacher erweiterbar – eine weitere Taste hinzufügen bedeutet nur eine neue Zeile in jeder Liste.

### Buttons in einer Schleife initialisieren

```python
buttons = []
for pin in BUTTON_PINS:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN
    buttons.append(btn)
```

Für jeden Pin in der Liste wird ein Button-Objekt erstellt und zur `buttons`-Liste hinzugefügt. Das Ergebnis ist identisch zu 6 einzelnen Blöcken, aber deutlich kompakter.

### `zip()` und `*keys`

```python
for btn, keys in zip(buttons, KEYCODES):
    if btn.value:
        keyboard.send(*keys)
```

- `zip(buttons, KEYCODES)` kombiniert beide Listen paarweise: `(btn1, (Ctrl, F7))`, `(btn2, (Ctrl, F8))` usw.
- `*keys` entpackt das Tupel: aus `(Keycode.CONTROL, Keycode.F7)` werden zwei einzelne Argumente → `keyboard.send(Keycode.CONTROL, Keycode.F7)`

## Tastenkombinationen anpassen

Einfach die `KEYCODES`-Liste ändern. Alle verfügbaren Codes: [Adafruit HID Keycode-Referenz](https://docs.circuitpython.org/projects/hid/en/latest/api.html#adafruit_hid.keycode.Keycode)

### Beispielbelegung für OBS

```python
KEYCODES = [
    (Keycode.CONTROL, Keycode.F1),   # Szene 1
    (Keycode.CONTROL, Keycode.F2),   # Szene 2
    (Keycode.CONTROL, Keycode.F3),   # Szene 3
    (Keycode.CONTROL, Keycode.F4),   # Szene 4
    (Keycode.ALT, Keycode.F9),       # Aufnahme starten/stoppen
    (Keycode.ALT, Keycode.F10),      # Streaming starten/stoppen
]
```

### Beispielbelegung für Zoom/Teams

```python
KEYCODES = [
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.M),  # Stummschalten
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.V),  # Kamera ein/aus
    (Keycode.ALT, Keycode.Y),                      # Hand heben (Zoom)
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.H),  # Hand heben (Teams)
    (Keycode.CONTROL, Keycode.SHIFT, Keycode.B),  # Hintergrund wechseln
    (Keycode.CONTROL, Keycode.W),                  # Meeting verlassen
]
```

### Medientasten

```python
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

cc = ConsumerControl(usb_hid.devices)

# In der Hauptschleife statt keyboard.send():
cc.send(ConsumerControlCode.PLAY_PAUSE)    # Play/Pause
cc.send(ConsumerControlCode.VOLUME_INCREMENT)  # Lauter
cc.send(ConsumerControlCode.VOLUME_DECREMENT)  # Leiser
cc.send(ConsumerControlCode.MUTE)              # Stummschalten
```

## Gehäuse: Lasercutter

Die SVG-Dateien für das Gehäuse liegen im Repo:

- [`docs/assets/keypad_box.svg`](https://github.com/jvanvinkenroye/makerSQpico/blob/main/docs/assets/keypad_box.svg) – Gehäuse
- [`docs/assets/keypad_keyholder.svg`](https://github.com/jvanvinkenroye/makerSQpico/blob/main/docs/assets/keypad_keyholder.svg) – Tastenhalterung

### Material

- **Sperrholz 3 mm** (empfohlen) – günstig, leicht zu schneiden, gut zu bekleben
- Alternativ: Acrylglas 3 mm für ein transparentes Gehäuse

### Vorbereitung

[Inkscape herunterladen](https://inkscape.org/release/) – kostenlos, Windows/macOS/Linux

### Anleitung

1. SVG-Datei in Inkscape öffnen
2. Maße prüfen: Taster-Ausschnitte müssen zur Taster-Größe passen (typisch 12×12 mm)
3. Linienfarbe und -stärke nach Lasercutter-Vorgabe setzen (meist Rot = Schnitt, Schwarz = Gravur)
4. Datei als SVG oder DXF exportieren und an den Lasercutter übergeben
5. Teile zusammenstecken – die Zapfen-Schlitz-Verbindung hält ohne Kleber

## Tastenaufsätze: 3D-Druck

Individuelle Keycaps lassen sich in TinkerCAD gestalten und auf einem FDM-Drucker drucken.

### Vorbereitung

- [TinkerCAD](https://www.tinkercad.com/dashboard) – kostenlos, läuft im Browser, kein Download
- [PrusaSlicer herunterladen](https://www.prusa3d.com/de/page/prusaslicer_424/) – kostenlos, Windows/macOS/Linux

### Design in TinkerCAD

1. Einloggen → „Neues Design erstellen"
2. Basisquader: 18×18×6 mm (passt auf 12×12 mm Taster)
3. Unterseite: Hohlraum ausschneiden (10×10×4 mm, zentriert) damit der Taster hineinpasst
4. Optional: Text oder Symbol auf der Oberseite als Gravur oder Erhebung hinzufügen
5. Exportieren → STL

### Slicen mit PrusaSlicer

1. STL-Datei importieren
2. Druckerprofil wählen (MK3S oder entsprechendes Modell)
3. Material: PLA (einfach zu drucken, ausreichend stabil)
4. Schichthöhe: 0,2 mm (Standard), Infill: 20 %
5. „Jetzt slicen" → G-Code exportieren
6. G-Code auf SD-Karte kopieren, Karte in Drucker einlegen, Datei auswählen

## Erwartetes Verhalten

- Taster nicht gedrückt: nichts passiert
- Taster 1 gedrückt: Strg+F7 wird gesendet
- Taster 2–6: entsprechend Strg+F8 bis Strg+F12
- Entprellung: 100 ms Pause nach jedem Tastendruck

## Fehlersuche

**Taste reagiert nicht:**
- Verdrahtung prüfen: eine Seite des Tasters muss an **3,3 V** (Pin 36), die andere am GPIO-Pin
- Bei Pull-Down muss der Taster gegen 3,3 V schalten, nicht gegen GND

**Alle Tasten lösen gleichzeitig aus:**
- Kurzschluss zwischen den Pins prüfen; sicherstellen dass 3,3 V nur an den Tastern anliegt

**Falsche Taste wird gesendet:**
- Pinzuordnung in `BUTTON_PINS` gegen die Verdrahtungstabelle prüfen

**`ImportError: no module named 'adafruit_hid'`:**
- Den Ordner `adafruit_hid` vollständig (nicht nur einzelne Dateien) nach `CIRCUITPY/lib/` kopieren

---

[← Zurück: HID – Spacebar-Taster](05_hid_spacebar.md)
