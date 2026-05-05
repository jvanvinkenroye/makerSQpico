# Beispiel: Streaming Deck

6-Tasten-Macro-Keyboard: Jeder Taster sendet eine Tastenkombination (Ctrl+F7 bis Ctrl+F12).

## Hardware

| Bauteil | Anzahl |
|---------|--------|
| Raspberry Pi Pico | 1 |
| Taster (normally open) | 6 |
| Jumperkabel | 12 |
| Breadboard oder Gehäuse (Lasercutter) | 1 |

## Verdrahtung

| Taste | Pico-Pin | GPIO |
|-------|----------|------|
| 1 | Pin 12 | GP9 |
| 2 | Pin 11 | GP8 |
| 3 | Pin 10 | GP7 |
| 4 | Pin 25 | GP19 |
| 5 | Pin 26 | GP20 |
| 6 | Pin 27 | GP21 |

Alle Taster: eine Seite an den jeweiligen GPIO-Pin, andere Seite an **3,3 V** (nicht GND).
Pull-Down-Widerstand ist intern aktiv – `btn.value` ist `True` wenn gedrückt.

## Tastenbelegung

| Taste | Tastenkombination |
|-------|------------------|
| 1 | Ctrl + F7 |
| 2 | Ctrl + F8 |
| 3 | Ctrl + F9 |
| 4 | Ctrl + F10 |
| 5 | Ctrl + F11 |
| 6 | Ctrl + F12 |
