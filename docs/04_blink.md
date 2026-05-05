# Schritt 4: Erstes Programm – Blink

Bevor wir Hardware anschließen, testen wir, ob CircuitPython korrekt läuft. Das klassische "Hello World" für Mikrocontroller ist ein blinkendes Licht.

Der Raspberry Pi Pico hat eine grüne LED direkt auf dem Board – kein externes Bauteil nötig.

## Code auf den Pico laden

Die fertige Datei liegt im Repo unter [`examples/00_blink/code.py`](https://github.com/jvanvinkenroye/makerSQpico/blob/main/examples/00_blink/code.py).

Kopiere sie als `code.py` auf das `CIRCUITPY`-Laufwerk:

**Windows:** Datei im Explorer auf `CIRCUITPY` kopieren (bestehende `code.py` ersetzen)

**macOS:**
```bash
cp examples/00_blink/code.py /Volumes/CIRCUITPY/code.py
```

**Linux:**
```bash
cp examples/00_blink/code.py /media/$USER/CIRCUITPY/code.py
```

Der Pico startet automatisch neu sobald die Datei gespeichert ist.

## Code

```python title="examples/00_blink/code.py"
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
```

## Code-Erklärung

```python
import board
import digitalio
import time
```

- `board` – Zugriff auf die benannten Pins des Pico
- `digitalio` – digitale Ein- und Ausgabe
- `time` – Zeitfunktionen (`sleep`)

```python
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
```

`board.LED` ist der interne Name für den LED-Pin auf dem Pico. Er wird als Ausgang konfiguriert – d.h. wir steuern ihn, lesen ihn nicht.

```python
while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
```

- `led.value = True` schaltet die LED ein
- `led.value = False` schaltet sie aus
- `time.sleep(0.5)` wartet 0,5 Sekunden

`while True` lässt das Programm dauerhaft laufen – ohne das würde der Code einmalig durchlaufen und der Pico nichts mehr tun.

## Erwartetes Verhalten

Die grüne LED auf dem Pico blinkt gleichmäßig: 0,5 s an, 0,5 s aus.

## Variationen ausprobieren

Ändere die `sleep`-Werte und speichere die Datei – der Pico lädt den Code automatisch neu:

```python
# Schnelles Blinken
time.sleep(0.1)

# Langsames Blinken
time.sleep(2.0)

# Ungleichmäßig: kurz an, lang aus
led.value = True
time.sleep(0.1)
led.value = False
time.sleep(0.9)
```

## Fehlersuche

**LED blinkt nicht:**
- Prüfen ob `code.py` tatsächlich auf `CIRCUITPY/` (nicht in einen Unterordner) kopiert wurde
- REPL öffnen und auf Syntaxfehler prüfen (Fehlermeldungen erscheinen im seriellen Terminal)
- USB-Verbindung prüfen

**Fehlermeldung im REPL:**
- `IndentationError`: Einrückung im Code prüfen (4 Leerzeichen, keine Tabs)
- `NameError`: Tippfehler bei einem Variablennamen

---

Weiter: [Erste HID-Anwendung: Spacebar-Taster](05_hid_spacebar.md)
