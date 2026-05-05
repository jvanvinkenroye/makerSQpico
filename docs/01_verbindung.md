# Schritt 1: Pico mit dem Rechner verbinden

## Was ist der Raspberry Pi Pico?

Der Raspberry Pi Pico ist ein Mikrocontroller-Board von der Raspberry Pi Foundation. Anders als ein Raspberry Pi (Einplatinencomputer) läuft auf dem Pico kein Betriebssystem – er führt ein einzelnes Programm direkt auf der Hardware aus.

Über seinen Micro-USB-Anschluss kann der Pico:
- mit Strom versorgt werden
- als USB-Gerät mit dem Rechner kommunizieren (Massenspeicher, serielles Terminal, HID)

## Pico-Varianten im Überblick

Es gibt mehrere Varianten des Pico. Für dieses Projekt eignen sich alle – der Code funktioniert auf allen gleich.

| Variante | Chip | Besonderheit | Pinout |
|----------|------|--------------|--------|
| **Pico** | RP2040 | Basismodell | [Pinout (PDF)](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf) |
| **Pico H** | RP2040 | Pico mit vorgelöteten Stiftleisten | [Pinout (PDF)](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf) |
| **Pico W** | RP2040 | + WLAN & Bluetooth | [Pinout (PDF)](https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf) |
| **Pico WH** | RP2040 | Pico W mit vorgelöteten Stiftleisten | [Pinout (PDF)](https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf) |
| **Pico 2** | RP2350 | Nachfolger mit mehr Leistung | [Pinout (PDF)](https://datasheets.raspberrypi.com/pico/Pico-2-Pinout.pdf) |
| **Pico 2W** | RP2350 | Pico 2 + WLAN & Bluetooth | [Pinout (PDF)](https://datasheets.raspberrypi.com/pico2w/Pico-2-W-Pinout.pdf) |

> **Hinweis:** Für den nächsten Schritt (CircuitPython installieren) braucht jede Variante eine **eigene UF2-Datei** – welche das ist, steht in [Schritt 2](02_circuitpython_install.md).

### H-Varianten (mit Stiftleisten)

Pico H und Pico WH kommen mit bereits aufgelöteten Stiftleisten – ideal für Breadboards, da kein Löten nötig ist. GPIO-Nummern und Code sind identisch zur Basisvariante.

### W-Varianten (mit WLAN)

Der Pico W hat denselben GPIO-Aufbau wie der Pico, aber einen leicht anderen Pinout (der WLAN-Chip belegt intern einige Pins). Für dieses Projekt spielt das keine Rolle – alle genutzten Pins (GP7, GP8, GP9, GP15, GP19–GP21) sind auf allen Varianten identisch verfügbar.

### Pico 2 (RP2350)

Der Pico 2 ist der Nachfolger mit schnellerem Prozessor und mehr RAM. Das Pinout ist **kompatibel** zum Pico – gleiche physische Anordnung, gleiche GP-Nummern. Die CircuitPython-UF2-Datei ist jedoch eine andere.

## Wichtig: Das richtige Kabel

Viele Micro-USB-Kabel sind reine Ladekabel ohne Datenleitungen. Stelle sicher, dass das Kabel Daten überträgt – am einfachsten prüfen: schließt du den Pico an, muss ein Laufwerk im Dateimanager erscheinen.

## Verbindung herstellen

1. Micro-USB-Stecker in den Pico stecken
2. USB-A-Stecker in den Rechner stecken

Nach der ersten Verbindung (ohne CircuitPython) erscheint das Laufwerk `RPI-RP2` (Pico/Pico W) bzw. `RP2350` (Pico 2/Pico 2W) – das ist der Bootloader-Modus. Sobald CircuitPython installiert ist, erscheint stattdessen `CIRCUITPY`.

## Betriebssystem-Hinweise

### Windows

- Das Laufwerk erscheint automatisch im Explorer (z.B. als `D:` oder `E:`)
- Kein Treiber notwendig (ab Windows 10)
- Den seriellen Port (REPL) findet man im Gerätemanager unter "Anschlüsse (COM & LPT)" als `COM3`, `COM4` o.ä.

### macOS

- Das Laufwerk erscheint automatisch unter `/Volumes/CIRCUITPY` und im Finder
- Kein Treiber notwendig
- Den seriellen Port findet man als `/dev/tty.usbmodem*` (im Terminal: `ls /dev/tty.usbmodem*`)

### Linux

- Das Laufwerk erscheint unter `/media/$USER/CIRCUITPY` (GNOME/KDE) oder `/run/media/$USER/CIRCUITPY`
- Kein Treiber notwendig
- Den seriellen Port findet man als `/dev/ttyACM0`

**Linux: Zugriff auf den seriellen Port freischalten**

Standardmäßig darf nur `root` auf `/dev/ttyACM0` zugreifen. Einmalig ausführen:

```bash
sudo usermod -a -G dialout $USER
```

Danach ausloggen und wieder einloggen. Alternativ einmalig mit `sudo`:

```bash
sudo screen /dev/ttyACM0 115200
```

---

[Weiter: CircuitPython installieren →](02_circuitpython_install.md)
