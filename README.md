# Raspberry Pi Pico als HID-Gerät

Ein schrittweises Lernprojekt: Den Raspberry Pi Pico mit CircuitPython als USB-Tastatur (HID) nutzen – gesteuert über GPIO-Pins und physische Taster.

## Lernziele

- Raspberry Pi Pico mit einem Rechner verbinden
- CircuitPython installieren und erste Schritte im REPL
- GPIO-Pins als digitale Ausgänge und Eingänge konfigurieren
- Den Pico als USB-HID-Tastatur nutzen
- Eine physische Taste mit einer Tastatureingabe verknüpfen
- Ein vollständiges Macro-Keyboard (Streaming Deck) bauen

## Benötigte Hardware

| Bauteil | Anzahl |
|---------|--------|
| Raspberry Pi Pico (RP2040) | 1 |
| Micro-USB-Kabel (Daten, kein Ladekabel) | 1 |
| Taster (Druckknopf) | 1–6 |
| Jumperkabel | 2–12 |
| Breadboard (optional) | 1 |

## Benötigte Software

- **CircuitPython Web Editor** (empfohlen, kein Download): [code.circuitpython.org](https://code.circuitpython.org/)
- **Thonny** (Desktop-Alternative): [thonny.org](https://thonny.org/)
- Alternativ: VS Code mit der Erweiterung "CircuitPython"
- Dateimanager (Finder, Explorer, Nautilus)

## Schritte

1. [Pico mit dem Rechner verbinden](docs/01_verbindung.md)
2. [CircuitPython installieren](docs/02_circuitpython_install.md)
3. [Bibliotheken einrichten](docs/03_bibliotheken.md)
4. [Erstes Programm – Blink](docs/04_blink.md)
5. [Erste HID-Anwendung: Spacebar-Taster](docs/05_hid_spacebar.md)
6. [Streaming Deck – 6-Tasten-Macro-Keyboard](docs/06_streaming_deck.md)

## Beispiele

- [`examples/00_blink/`](examples/00_blink/) – onboard LED blinken
- [`examples/01_spacebar/`](examples/01_spacebar/) – Taster sendet Leertaste
- [`examples/02_streaming_deck/`](examples/02_streaming_deck/) – 6-Tasten-Macro-Keyboard
