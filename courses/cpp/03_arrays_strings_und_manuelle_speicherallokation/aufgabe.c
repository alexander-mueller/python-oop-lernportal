#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 🎯 TEILZIEL 1 (TODO 1): Dynamischen int-Array auf dem Heap allozieren
int* erstelle_dynamisches_array(size_t groesse) {
    int* arr = (int*)malloc(groesse * sizeof(int));
    return arr;
}

// 🎯 TEILZIEL 2 (TODO 2): Speicher freigeben
void speicher_freigeben(void* ptr) {
    if (ptr != NULL) {
        free(ptr);
    }
}