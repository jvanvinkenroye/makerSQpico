# Raspberry Pi Pico als HID-Gerät

Ein schrittweises Lernprojekt: Den Raspberry Pi Pico mit CircuitPython als USB-Tastatur (HID) nutzen – gesteuert über GPIO-Pins und physische Taster.

## Lernziele

- Raspberry Pi Pico mit einem Rechner verbinden
- CircuitPython installieren und erste Schritte im REPL
- GPIO-Pins als digitale Ausgänge und Eingänge konfigurieren
- Den Pico als USB-HID-Tastatur nutzen
- Eine physische Taste mit einer Tastatureingabe verknüpfen

## Benötigte Hardware

| Bauteil | Anzahl |
|---------|--------|
| Raspberry Pi Pico (RP2040) | 1 |
| Micro-USB-Kabel (Daten, kein Ladekabel) | 1 |
| Taster (Druckknopf) | 1 |
| Jumperkabel | 2 |
| Breadboard (optional) | 1 |

## Benötigte Software

- **Mu Editor** (empfohlen): [codewith.mu](https://codewith.mu/)
- Alternativ: VS Code mit CircuitPython-Erweiterung
- Dateimanager (Finder, Explorer, Nautilus)

## Download

[Repository als ZIP herunterladen](https://github.com/jvanvinkenroye/makerSQpico/archive/refs/heads/main.zip)

## Ablauf

1. [Pico mit dem Rechner verbinden](01_verbindung.md)
2. [CircuitPython installieren](02_circuitpython_install.md)
3. [Bibliotheken einrichten](03_bibliotheken.md)
4. [Erstes Programm – Blink](04_blink.md)
5. [Erste HID-Anwendung: Spacebar-Taster](05_hid_spacebar.md)
