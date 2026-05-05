# Schritt 1: Pico mit dem Rechner verbinden

## Was ist der Raspberry Pi Pico?

Der Raspberry Pi Pico ist ein Mikrocontroller-Board mit dem RP2040-Chip. Anders als ein Raspberry Pi (Einplatinencomputer) läuft auf dem Pico kein Betriebssystem – er führt ein einzelnes Programm direkt auf der Hardware aus.

Über seinen Micro-USB-Anschluss kann der Pico:
- mit Strom versorgt werden
- als USB-Gerät mit dem Rechner kommunizieren (Massenspeicher, serielles Terminal, HID)

## Wichtig: Das richtige Kabel

Viele Micro-USB-Kabel sind reine Ladekabel ohne Datenleitungen. Stelle sicher, dass das Kabel Daten überträgt – am einfachsten prüfen: schließt du den Pico an, muss ein Laufwerk im Dateimanager erscheinen.

## Verbindung herstellen

1. Micro-USB-Stecker in den Pico stecken
2. USB-A-Stecker in den Rechner stecken

Nach der ersten Verbindung (ohne CircuitPython) erscheint das Laufwerk `RPI-RP2` – das ist der Bootloader-Modus. Sobald CircuitPython installiert ist, erscheint stattdessen `CIRCUITPY`.

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

## Pinout des Pico

Das offizielle Pinout-Diagramm mit allen GPIO-Nummern:
[Pico R3 Pinout (PDF)](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)

Die Pin-Nummern im Code entsprechen den **GP**-Nummern auf dem Board (z.B. `GP15` = Pin 20 am Stecker).

---

[Weiter: CircuitPython installieren →](02_circuitpython_install.md)
