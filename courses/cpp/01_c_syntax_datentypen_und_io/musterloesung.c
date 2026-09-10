#include <stdio.h>
#include <stddef.h>

/* ==============================================================================
 * ⚙️ C 01: C-SYNTAX, DATENTYPEN & I/O – MUSTERLÖSUNG
 * ==============================================================================
 */

double berechne_sensor_mittelwert(int summe, int anzahl) {
    if (anzahl <= 0) {
        return 0.0;
    }
    return (double)summe / (double)anzahl;
}

void formatiere_messpunkt(char* buffer, size_t buf_size, int sensor_id, double temperatur, char einheit) {
    if (buffer == NULL || buf_size == 0) {
        return;
    }
    snprintf(buffer, buf_size, "Sensor #%d: %.2f %c", sensor_id, temperatur, einheit);
}

int pruefe_datenbereich(int wert, int min_val, int max_val) {
    if (wert >= min_val && wert <= max_val) {
        return 1;
    }
    return 0;
}

double konvertiere_celsius_zu_fahrenheit(double celsius) {
    return (celsius * 9.0 / 5.0) + 32.0;
}

size_t ermittle_typ_groesse(int typ_code) {
    switch (typ_code) {
        case 1:
            return sizeof(char);
        case 2:
            return sizeof(int);
        case 3:
            return sizeof(double);
        case 4:
            return sizeof(long long);
        default:
            return 0;
    }
}

int main(void) {
    printf("=== C 01: Systems Datentypen & I/O (Musterlösung) ===\n");
    printf("Mittelwert: %.2f\n", berechne_sensor_mittelwert(150, 4));

    char buf[64];
    formatiere_messpunkt(buf, sizeof(buf), 1, 21.879, 'C');
    printf("%s\n", buf);

    printf("Bereich 15 in [10, 20]: %d\n", pruefe_datenbereich(15, 10, 20));
    printf("20 C in Fahrenheit: %.2f F\n", konvertiere_celsius_zu_fahrenheit(20.0));
    printf("Groesse int (Code 2): %zu Bytes\n", ermittle_typ_groesse(2));
    return 0;
}
