# C 03: Strings, Stack vs. Heap & Manuelle Speicherallokation 🧱

Willkommen zu **Modul 03** des C & C++ Systems Engineering Lehrpfads!

In diesem Modul lernst du die Verwaltung des Arbeitsspeichers auf Hardware-Ebene kennen: Null-terminierte Zeichenketten (`char[]`), die strikte Trennung von Stack und Heap sowie die C-Speicherfunktionen `malloc`, `calloc`, `realloc` und `free`.

---

## 💡 1. Das Wichtigste in Kürze

### C-Strings & das Null-Byte (`'\0'`)
In C sind Strings Arrays von Zeichen (`char`), die durch das Byte `0` (`'\0'`) abgeschlossen werden.
- Die Länge eines Strings ist die Anzahl der Zeichen **vor** dem `'\0'`.
- Ein Puffer für einen String der Länge `N` muss mindestens `N + 1` Bytes groß sein!

### Stack vs. Heap
- **Stack (Stapelspeicher)**: Sehr schneller Speicher für lokale Variablen und Funktionsaufruf-Frames. Automatisch freigegeben, sobald der Block `{}` verlassen wird. Begrenzte Größe.
- **Heap (Dynamischer Freispeicher)**: Großer Speicherbereich für Daten mit dynamischer oder langlebiger Existenz. Muss vom Programmierer manuell reserviert und freigegeben werden.

### Allokation & Freigabe
```c
#include <stdlib.h>
#include <string.h>

// 1. Allokation
int* data = (int*)malloc(5 * sizeof(int));
if (data == NULL) { /* Out of Memory Fehlerbehandlung */ }

// 2. Verwendung
for (size_t i = 0; i < 5; i++) {
    data[i] = (int)(i * 10);
}

// 3. Vergrößerung
int* expanded = (int*)realloc(data, 10 * sizeof(int));
if (expanded != NULL) {
    data = expanded;
}

// 4. Sichere Freigabe
free(data);
data = NULL; // Verhindert Dangling-Pointer-Fehler
```

---

## 🎯 Aufgaben in `aufgabe.c`

1. **TODO 1 (`c_string_laenge`)**: Zähle die Zeichen eines `const char*` bis zum Null-Terminator `'\0'`.
2. **TODO 2 (`c_string_umkehren`)**: Kehre einen C-String in-place um (z. B. `"hello"` -> `"olleh"`).
3. **TODO 3 (`erstelle_dynamisches_array`)**: Allokiere mit `malloc` ein `int`-Array der Größe `anzahl` auf dem Heap und fülle es mit `initial_wert`.
4. **TODO 4 (`dupliziere_string`)**: Allokiere `strlen(src) + 1` Bytes auf dem Heap und kopiere den String zeichenweise oder mit `memcpy`/`strcpy`.
5. **TODO 5 (`vergroessere_array`)**: Erweitere ein bestehendes dynamisches Array mit `realloc` und initialisiere die neuen Elemente mit `fuell_wert`.
6. **TODO 6 (`gebe_speicher_frei`)**: Gib den Speicher über einen Zeiger-auf-Zeiger (`void** ptr_ref`) frei und setze `*ptr_ref = NULL`.

---

## 🧪 Tests ausführen

Die Tests prüfen String-Algorithmen, dynamische Allokationen sowie die Vermeidung von Memory Leaks.
