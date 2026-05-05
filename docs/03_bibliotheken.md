# Schritt 3: Bibliotheken einrichten

## Was sind CircuitPython-Bibliotheken?

CircuitPython-Bibliotheken sind Python-Dateien oder -Ordner, die auf das `lib/`-Verzeichnis des Pico kopiert werden. Sie erweitern den Funktionsumfang, z.B. um HID-Unterstützung.

Für unser Projekt benötigen wir die Bibliothek **`adafruit_hid`**.

## CircuitPython Bundle herunterladen

Adafruit stellt alle Bibliotheken gebündelt zur Verfügung:

1. Öffne die [Adafruit CircuitPython Bundle Releases](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases)
2. Lade die neueste `adafruit-circuitpython-bundle-9.x-mpy-*.zip` herunter
   (Versionsnummer muss zur installierten CircuitPython-Version passen – `9.x` für CircuitPython 9)
3. Entpacke das ZIP-Archiv

## adafruit_hid installieren

Im entpackten Bundle-Ordner befindet sich ein `lib/`-Unterordner. Darin liegt der Ordner `adafruit_hid`.

Diesen Ordner vollständig auf den Pico kopieren:

**Windows (Explorer):**
- Öffne den Bundle-Ordner → `lib/` → kopiere `adafruit_hid`
- Füge ihn in `CIRCUITPY/lib/` ein

**macOS/Linux (Terminal):**
```bash
cp -r ~/Downloads/adafruit-circuitpython-bundle-*/lib/adafruit_hid /Volumes/CIRCUITPY/lib/
# Linux:
cp -r ~/Downloads/adafruit-circuitpython-bundle-*/lib/adafruit_hid /media/$USER/CIRCUITPY/lib/
```

Danach sollte die Struktur auf dem Pico so aussehen:
```
CIRCUITPY/
├── code.py
└── lib/
    └── adafruit_hid/
        ├── __init__.py
        ├── keyboard.py
        ├── keycode.py
        └── ...
```

## Editor einrichten

### CircuitPython Web Editor (empfohlen, kein Download)

Der offizielle Editor von Adafruit läuft direkt im Browser – kein Download nötig.

[code.circuitpython.org](https://code.circuitpython.org/) → funktioniert in Chrome, Edge und Firefox

- Pico per USB verbinden, "Connect" klicken
- Dateien direkt bearbeiten und speichern
- Eingebautes serielles Terminal (REPL)
- Autovervollständigung für CircuitPython-Module

### Thonny (Desktop-Alternative)

Thonny ist eine einfache Python-IDE mit nativer CircuitPython-Unterstützung.

[Thonny herunterladen](https://thonny.org/)

Nach dem Öffnen:
1. Werkzeuge → Optionen → Interpreter: "CircuitPython" wählen
2. Dateien auf dem `CIRCUITPY`-Laufwerk direkt öffnen und speichern
3. REPL ist im Shell-Bereich unten verfügbar

### VS Code (für Fortgeschrittene)

1. [VS Code herunterladen](https://code.visualstudio.com/)
2. Erweiterung "CircuitPython" installieren
3. `CIRCUITPY` als Arbeitsordner öffnen

Beim Speichern einer Datei auf dem `CIRCUITPY`-Laufwerk startet der Pico automatisch neu und führt den neuen Code aus.

---

[← Zurück: CircuitPython installieren](02_circuitpython_install.md) | [Weiter: Erstes Programm – Blink →](04_blink.md)
