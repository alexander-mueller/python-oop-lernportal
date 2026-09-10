#include <stdio.h>
#include <stddef.h>

/* ==============================================================================
 * ⚙️ C 02: POINTER, SPEICHERADRESSEN (&/*) & ZEIGERARITHMETIK
 * ==============================================================================
 */

/**
 * 🎯 TEILZIEL 1 (TODO 1): Vertausche die Werte an den Speicheradressen von a und b.
 * Falls a oder b NULL ist, soll die Funktion sofort abbrechen (Guard Clause).
 */
void tausche_werte(int* a, int* b) {
    // TODO: Werte an den Adressen a und b mit Hilfsvariable vertauschen
}

/**
 * 🎯 TEILZIEL 2 (TODO 2): Berechne Produkt und Summe und gib sie über Zeiger zurück.
 * Schreibe: *prod = a * b und *sum = a + b (sofern Zeiger nicht NULL sind).
 */
void multipliziere_und_addiere(int a, int b, int* prod, int* sum) {
    // TODO: Implementieren
}

/**
 * 🎯 TEILZIEL 3 (TODO 3): Finde das kleinste und größte Element im Array.
 * Schreibe das Minimum in *out_min und das Maximum in *out_max.
 * Falls arr == NULL, out_min == NULL, out_max == NULL oder size == 0 ist: tue nichts.
 */
void finde_max_und_min(const int* arr, size_t size, int* out_min, int* out_max) {
    // TODO: Array durchlaufen und Min/Max ermitteln
}

/**
 * 🎯 TEILZIEL 4 (TODO 4): Gib die Schrittweite (in Bytes) zurück, um die ein Zeiger
 * bei ptr + 1 im Speicher weiterwandert:
 * 1: sizeof(char)   (1 Byte)
 * 2: sizeof(int)    (4 Bytes)
 * 3: sizeof(double) (8 Bytes)
 * sonst: 0
 */
size_t pointer_schrittweite(int typ_id) {
    // TODO: Schrittweite zurückgeben
    return 0;
}

/**
 * 🎯 TEILZIEL 5 (TODO 5): Summiere das Array AUSSCHLIESSLICH mit Zeigerarithmetik!
 * Verwende keine Index-Klammern arr[i].
 * Nutze stattdessen:
 * const int* ptr = start;
 * const int* end = start + count;
 * Laufe mit ptr++ bis end und addiere *ptr.
 * Falls start == NULL oder count == 0: gib 0 zurück.
 */
int array_summe_zeigerarithmetik(const int* start, size_t count) {
    // TODO: Mit Zeigerarithmetik summieren
    return 0;
}

int main(void) {
    printf("=== C 02: Pointer & Zeigerarithmetik ===\n");
    int x = 10, y = 20;
    tausche_werte(&x, &y);
    printf("Nach Tausch: x=%d, y=%d\n", x, y);

    int p = 0, s = 0;
    multipliziere_und_addiere(6, 7, &p, &s);
    printf("6 * 7 = %d | 6 + 7 = %d\n", p, s);

    int numbers[] = {12, 45, 7, 89, 23};
    int min_val = 0, max_val = 0;
    finde_max_und_min(numbers, 5, &min_val, &max_val);
    printf("Min: %d, Max: %d\n", min_val, max_val);

    printf("Summe (Zeigerarithmetik): %d\n", array_summe_zeigerarithmetik(numbers, 5));
    return 0;
}
