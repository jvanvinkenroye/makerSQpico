# Schritt 2: CircuitPython installieren

## Warum CircuitPython?

CircuitPython ist eine Python-Variante von Adafruit, die speziell für Mikrocontroller entwickelt wurde. Für unser HID-Projekt hat es gegenüber MicroPython einen entscheidenden Vorteil: **USB-HID ist nativ eingebaut** und funktioniert ohne Anpassungen am Firmware-Image.

Weitere Vorteile für Einsteiger:
- Kein Kompilieren – Dateien direkt auf das Laufwerk speichern
- Änderungen an `code.py` werden beim Speichern automatisch neu gestartet
- Eingebauter serieller REPL für schnelle Tests

## UF2-Datei herunterladen

1. Öffne die [CircuitPython-Downloadseite für den Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/)
2. Lade die aktuelle stabile Version herunter (`.uf2`-Datei, z.B. `adafruit-circuitpython-raspberry_pi_pico-en_US-9.x.x.uf2`)
3. Speichere die Datei irgendwo auf deinem Rechner (z.B. Downloads-Ordner)

## CircuitPython flashen

### Schritt 1: BOOTSEL-Modus aktivieren

1. Halte die **BOOTSEL**-Taste auf dem Pico gedrückt
2. Schließe das USB-Kabel an (Taste weiter gedrückt halten)
3. Erst loslassen, wenn das Laufwerk `RPI-RP2` erscheint

Das Laufwerk `RPI-RP2` ist der Bootloader – hier kann Firmware eingespielt werden.

### Schritt 2: UF2-Datei kopieren

**Windows:**
- Öffne den Explorer
- Ziehe die `.uf2`-Datei auf das Laufwerk `RPI-RP2`

**macOS:**
- Öffne den Finder
- Ziehe die `.uf2`-Datei auf `RPI-RP2` unter "Orte"

Alternativ im Terminal:
```bash
cp ~/Downloads/adafruit-circuitpython-*.uf2 /Volumes/RPI-RP2/
```

**Linux:**
```bash
cp ~/Downloads/adafruit-circuitpython-*.uf2 /media/$USER/RPI-RP2/
# oder mit sudo, falls kein Zugriff:
sudo cp ~/Downloads/adafruit-circuitpython-*.uf2 /media/$USER/RPI-RP2/
```

### Schritt 3: Neustart abwarten

Der Pico startet automatisch neu. Das Laufwerk `RPI-RP2` verschwindet, kurz darauf erscheint `CIRCUITPY`. Das ist das Zeichen: CircuitPython läuft.

## Inhalt von CIRCUITPY

Nach der Installation enthält das Laufwerk:

```
CIRCUITPY/
├── code.py          # Dein Hauptprogramm (wird automatisch ausgeführt)
├── boot_out.txt     # Startprotokoll
└── lib/             # Hier kommen Bibliotheken rein
```

## REPL testen

Der REPL (Read-Eval-Print Loop) ermöglicht es, Python-Befehle direkt auf dem Pico auszuführen.

**Mit dem CircuitPython Web Editor ([code.circuitpython.org](https://code.circuitpython.org/)):**
- Seite in Chrome/Edge öffnen, Pico per USB verbinden
- "Connect" → Pico auswählen → serielles Terminal öffnet sich
- `Strg+C` drücken → `>>>` erscheint
- Testbefehl eingeben: `print("Hallo vom Pico!")`

**Mit Thonny ([thonny.org](https://thonny.org/)):**
- Thonny öffnen → Werkzeuge → Optionen → Interpreter: "CircuitPython" wählen
- Unten im Shell-Bereich erscheint der REPL
- Testbefehl eingeben: `print("Hallo vom Pico!")`

**Mit screen (macOS/Linux):**
```bash
screen /dev/tty.usbmodem* 115200    # macOS
screen /dev/ttyACM0 115200          # Linux
```
Beenden mit `Strg+A`, dann `K`, dann `Y`.

**Mit PuTTY (Windows):**
- Verbindungstyp: Serial
- COM-Port: wie im Gerätemanager angezeigt
- Baudrate: 115200

---

[← Zurück: Pico verbinden](01_verbindung.md) | [Weiter: Bibliotheken einrichten →](03_bibliotheken.md)
