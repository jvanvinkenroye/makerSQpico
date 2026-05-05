# Beispiel: Spacebar-Taster

Ein Taster an GP15 sendet beim Drücken eine Leertaste an den angeschlossenen Rechner.

## Hardware

| Bauteil | Anzahl |
|---------|--------|
| Raspberry Pi Pico | 1 |
| Taster (normally open) | 1 |
| Jumperkabel | 2 |

## Verdrahtung

```
Pico GP15 (Pin 20) ----[ Taster ]---- GND (Pin 18)
```

Kein externer Widerstand nötig – der interne Pull-up-Widerstand ist aktiviert.

## Abhängigkeiten

Die Bibliothek `adafruit_hid` muss in `CIRCUITPY/lib/` vorhanden sein.
Download: https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases

## Verwendung

`code.py` in das Stammverzeichnis von `CIRCUITPY/` kopieren. Der Pico startet automatisch neu.

## Erwartetes Verhalten

- Taster nicht gedrückt: nichts passiert
- Taster gedrückt: eine Leertaste wird an den Rechner gesendet
- Entprellung: 300 ms Pause nach jedem Tastendruck
