#include <stdio.h>
#include <stddef.h>

/* ==============================================================================
 * ⚙️ C 01: C-SYNTAX, DATENTYPEN, FORMAT-SPECIFIER & STANDARD I/O
 * ==============================================================================
 */

/**
 * 🎯 TEILZIEL 1 (TODO 1): Berechne den genauen Mittelwert als double.
 * Falls anzahl <= 0 ist, soll 0.0 zurückgegeben werden.
 * Achte darauf, summe explizit zu (double) zu casten, um Ganzzahldivision zu vermeiden!
 */
double berechne_sensor_mittelwert(int summe, int anzahl) {
    // TODO: Implementieren
    return 0.0;
}

/**
 * 🎯 TEILZIEL 2 (TODO 2): Formatiere den Messpunkt sicher in den übergebenen Puffer.
 * Format: "Sensor #<id>: <temperatur auf 2 Nachkommastellen> <einheit>"
 * Beispiel: formatiere_messpunkt(buf, sizeof(buf), 5, 23.456, 'C') -> "Sensor #5: 23.46 C"
 * Verwende snprintf(buffer, buf_size, ...) zur Vermeidung von Buffer-Overflows!
 */
void formatiere_messpunkt(char* buffer, size_t buf_size, int sensor_id, double temperatur, char einheit) {
    // TODO: snprintf verwenden
}

/**
 * 🎯 TEILZIEL 3 (TODO 3): Prüfe, ob der übergebene Messwert innerhalb der Grenzwerte liegt.
 * Gibt 1 (wahr) zurück, wenn min_val <= wert <= max_val ist, andernfalls 0 (falsch).
 */
int pruefe_datenbereich(int wert, int min_val, int max_val) {
    // TODO: Bereichsprüfung implementieren
    return 0;
}

/**
 * 🎯 TEILZIEL 4 (TODO 4): Rechne Temperatur von Celsius in Fahrenheit um.
 * Formel: (celsius * 9.0 / 5.0) + 32.0
 */
double konvertiere_celsius_zu_fahrenheit(double celsius) {
    // TODO: Formel berechnen und zurückgeben
    return 0.0;
}

/**
 * 🎯 TEILZIEL 5 (TODO 5): Ermittle die Größe von Datentypen anhand eines Typ-Codes:
 * 1: sizeof(char)
 * 2: sizeof(int)
 * 3: sizeof(double)
 * 4: sizeof(long long)
 * Jeder andere Code: 0
 */
size_t ermittle_typ_groesse(int typ_code) {
    // TODO: switch/case oder if mit sizeof() umsetzen
    return 0;
}

int main(void) {
    printf("=== C 01: Systems Datentypen & I/O ===\n");
    printf("Mittelwert: %.2f\n", berechne_sensor_mittelwert(150, 4));

    char buf[64];
    formatiere_messpunkt(buf, sizeof(buf), 1, 21.879, 'C');
    printf("%s\n", buf);

    printf("Bereich 15 in [10, 20]: %d\n", pruefe_datenbereich(15, 10, 20));
    printf("20 C in Fahrenheit: %.2f F\n", konvertiere_celsius_zu_fahrenheit(20.0));
    printf("Groesse int (Code 2): %zu Bytes\n", ermittle_typ_groesse(2));
    return 0;
}
