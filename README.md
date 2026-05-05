# Raspberry Pi Pico als HID-Gerät

Ein schrittweises Lernprojekt: Den Raspberry Pi Pico mit CircuitPython als USB-Tastatur (HID) nutzen – gesteuert über GPIO-Pins und physische Taster.

## Lernziele

- Raspberry Pi Pico mit einem Rechner verbinden
- CircuitPython installieren und erste Schritte im REPL
- GPIO-Pins als digitale Eingänge konfigurieren
- Den Pico als USB-HID-Tastatur nutzen
- Eine physische Taste mit einer Tastatureingabe verknüpfen

## Benötigte Hardware

| Bauteil | Anzahl |
|---------|--------|
| Raspberry Pi Pico (RP2040) | 1 |
| Micro-USB-Kabel (Daten, kein Ladekabel) | 1 |
| Taster (Druckknopf) | 1 |
| Jumperkabel (female-to-male) | 2 |
| Breadboard (optional) | 1 |

## Benötigte Software

- **Mu Editor** (empfohlen, einsteigertauglich): https://codewith.mu/
- Alternativ: VS Code mit der Erweiterung "CircuitPython"
- Dateimanager (Finder, Explorer, Nautilus)

## Schritte

1. [Pico mit dem Rechner verbinden](docs/01_verbindung.md)
2. [CircuitPython installieren](docs/02_circuitpython_install.md)
3. [Bibliotheken einrichten](docs/03_bibliotheken.md)
4. [Erste HID-Anwendung: Spacebar-Taster](docs/04_hid_spacebar.md)

## Beispiele

- [`examples/01_spacebar/`](examples/01_spacebar/) – Taster sendet Leertaste
