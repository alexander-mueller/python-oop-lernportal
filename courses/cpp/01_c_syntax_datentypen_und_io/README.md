# C 01: C-Syntax, Datentypen, Format-Specifier & Standard I/O ⚙️

Willkommen zum ersten Modul des **C & C++ Systems Engineering** Lehrpfads!

In diesem Kapitel legst du das hardwarenahe Fundament: Du lernst den C-Kompilationszyklus kennen, verstehst die exakten Byte-Größen primitiver Datentypen im Arbeitsspeicher, führst typsichere Berechnungen ohne Rundungsverlust durch und nutzt `snprintf` für manipulationssichere Textformatierung.

---

## 💡 1. Das Wichtigste in Kürze

### Das Kompilationsmodell (Von `.c` zur ELF-Binary)
1. **Präprozessor (`cpp`)**: Behandelt Direktiven wie `#include <stdio.h>` und `#define MAX 100`.
2. **Compiler (`gcc/clang -S`)**: Übersetzt den C-Code in maschinenspezifischen Assembler-Code.
3. **Assembler (`as`)**: Erzeugt binäre Objektdateien (`.o`), die Maschinencode enthalten.
4. **Linker (`ld`)**: Bindet externe Symbole aus Bibliotheken (z. B. `libc`) ein und baut die finale Binärdatei.

### Primitive Typen & Speicherbreiten
- `char`: 1 Byte (8 Bit), Wertebereich `-128` bis `127` oder `0` bis `255` (`unsigned`).
- `int`: 4 Bytes (32 Bit), Standard-Ganzzahltyp in modernen 32/64-Bit Architekturen.
- `float`: 4 Bytes, IEEE 754 Fließkommazahl (~6 Dezimalstellen Genauigkeit).
- `double`: 8 Bytes, doppelte Genauigkeit (~15 Dezimalstellen).
- `size_t`: 8 Bytes (auf x86_64), unvorzeichenbehafteter Ganzzahltyp für Puffer- und Arraygrößen.

### Format-Specifier im Überblick
- `%d` / `%i`: Signed `int`
- `%u`: Unsigned `int`
- `%.2f`: `double` oder `float`, gerundet auf 2 Dezimalstellen
- `%c`: Einzelnes ASCII-Zeichen
- `%s`: Null-terminierter C-String (`char*`)
- `%zu`: `size_t`
- `%p`: Hexadezimale Speicheradresse eines Zeigers

```c
#include <stdio.h>

int main(void) {
    int sensor_id = 7;
    double messwert = 18.7351;
    
    // Ausgabe: "Sensor [007] misst 18.74 Grad"
    printf("Sensor [%03d] misst %.2f Grad\n", sensor_id, messwert);
    return 0;
}
```

---

## 🎯 Aufgaben in `aufgabe.c`

1. **TODO 1 (`berechne_sensor_mittelwert`)**: Berechne den genauen Mittelwert als `double`. Bei `anzahl <= 0` soll `0.0` zurückgegeben werden. Achte auf expliziten Cast `(double)summe / anzahl`.
2. **TODO 2 (`formatiere_messpunkt`)**: Formatiere einen Puffer mit `snprintf(buffer, buf_size, "Sensor #%d: %.2f %c", sensor_id, temperatur, einheit)`.
3. **TODO 3 (`pruefe_datenbereich`)**: Prüfe, ob ein Wert im geschlossenen Intervall `[min_val, max_val]` liegt (`1` für Ja, `0` für Nein).
4. **TODO 4 (`konvertiere_celsius_zu_fahrenheit`)**: Rechne Temperatur nach der Formel `(celsius * 9.0 / 5.0) + 32.0` um.
5. **TODO 5 (`ermittle_typ_groesse`)**: Ermittle mit `sizeof()` die Größe: `1 -> sizeof(char)`, `2 -> sizeof(int)`, `3 -> sizeof(double)`, `4 -> sizeof(long long)`, sonst `0`.

---

## 🧪 Tests ausführen

Die Tests prüfen deine C-Funktionen über automatisierte Test-Assertions:
```bash
# In der Monaco Web-IDE: Klicke auf 'Testen & Prüfen'
```
