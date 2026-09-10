# C 02: Pointer, Speicheradressen & Zeigerarithmetik 🧠

Willkommen zu **Modul 02** des C & C++ Systems Lehrpfads!

In diesem Modul meisterst du das absolute Kernkonzept hardwarenaher Programmierung: **Pointer (Zeiger)**. Du lernst, wie der physische Arbeitsspeicher adressiert wird, wie du Daten über Speicheradressen liest und modifizierst, wie Zeigerarithmetik funktioniert und wie C Pass-by-Reference realisiert.

---

## 💡 1. Das Wichtigste in Kürze

### Die zwei magischen Operatoren: `&` und `*`
- **Adressoperator `&` (Referenzieren)**: Gibt die Speicheradresse einer Variablen zurück (z. B. `&x`).
- **Dereferenzierungsoperator `*` (Indirektion)**: Greift auf den Wert an der im Zeiger gespeicherten Adresse zu (z. B. `*ptr = 100;`).

```c
int count = 10;
int* pCount = &count; // pCount zeigt auf die Adresse von count

printf("Wert von count: %d\n", count);      // 10
printf("Adresse von count: %p\n", (void*)pCount); // z.B. 0x7ffd54a0
printf("Dereferenzierter Wert: %d\n", *pCount); // 10

*pCount = 25; // Ändert den Wert von count auf 25!
```

### Zeigerarithmetik (Pointer Arithmetic)
In C skaliert die Zeigerarithmetik automatisch mit dem zugrundeliegenden Datentyp `T`:
- `int* ptr`: `ptr + 1` springt um `4 Bytes` (`sizeof(int)`) weiter.
- `double* ptr`: `ptr + 1` springt um `8 Bytes` (`sizeof(double)`) weiter.
- `char* ptr`: `ptr + 1` springt um `1 Byte` (`sizeof(char)`) weiter.

### Pass-by-Reference in C
C kennt ausschließlich *Pass-by-Value* (Kopieren von Werten beim Funktionsaufruf). Um den Originalwert in der aufrufenden Funktion zu verändern oder mehrere Werte zurückzugeben, übergibt man Zeiger auf die Variablen:

```c
void reset(int* p) {
    if (p != NULL) {
        *p = 0;
    }
}
```

---

## 🎯 Aufgaben in `aufgabe.c`

1. **TODO 1 (`tausche_werte`)**: Vertausche die Werte zweier `int`-Variablen an den Adressen `a` und `b`. Prüfe auf `NULL`.
2. **TODO 2 (`multipliziere_und_addiere`)**: Berechne Produkt und Summe zweier Ganzzahlen und schreibe sie in die Zeiger `prod` und `sum`.
3. **TODO 3 (`finde_max_und_min`)**: Finde das Minimum und Maximum in einem Array über Pointerzugriff.
4. **TODO 4 (`pointer_schrittweite`)**: Gib die Schrittweite eines Zeigertyps in Bytes zurück (`1 -> sizeof(char)`, `2 -> sizeof(int)`, `3 -> sizeof(double)`).
5. **TODO 5 (`array_summe_zeigerarithmetik`)**: Berechne die Summe eines Arrays ausschließlich über Zeiger-Inkrementierung (`const int* ptr = start; ptr < start + count; ptr++`).

---

## 🧪 Tests ausführen

Die Tests validieren Speichermanipulation und Zeigerarithmetik auf Byte-Ebene.
