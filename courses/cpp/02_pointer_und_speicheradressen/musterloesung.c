#include <stdio.h>
#include <stddef.h>

/* ==============================================================================
 * ⚙️ C 02: POINTER, SPEICHERADRESSEN & ZEIGERARITHMETIK – MUSTERLÖSUNG
 * ==============================================================================
 */

void tausche_werte(int* a, int* b) {
    if (a == NULL || b == NULL) {
        return;
    }
    int temp = *a;
    *a = *b;
    *b = temp;
}

void multipliziere_und_addiere(int a, int b, int* prod, int* sum) {
    if (prod != NULL) {
        *prod = a * b;
    }
    if (sum != NULL) {
        *sum = a + b;
    }
}

void finde_max_und_min(const int* arr, size_t size, int* out_min, int* out_max) {
    if (arr == NULL || out_min == NULL || out_max == NULL || size == 0) {
        return;
    }

    int min = *arr;
    int max = *arr;

    for (size_t i = 1; i < size; i++) {
        int current = *(arr + i);
        if (current < min) {
            min = current;
        }
        if (current > max) {
            max = current;
        }
    }

    *out_min = min;
    *out_max = max;
}

size_t pointer_schrittweite(int typ_id) {
    switch (typ_id) {
        case 1:
            return sizeof(char);
        case 2:
            return sizeof(int);
        case 3:
            return sizeof(double);
        default:
            return 0;
    }
}

int array_summe_zeigerarithmetik(const int* start, size_t count) {
    if (start == NULL || count == 0) {
        return 0;
    }

    int sum = 0;
    const int* end = start + count;
    for (const int* ptr = start; ptr < end; ptr++) {
        sum += *ptr;
    }
    return sum;
}

int main(void) {
    printf("=== C 02: Pointer & Zeigerarithmetik (Musterlösung) ===\n");
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
