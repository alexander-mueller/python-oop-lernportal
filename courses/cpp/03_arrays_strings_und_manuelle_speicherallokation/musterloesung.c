#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int* erstelle_dynamisches_array(size_t groesse) {
    int* arr = (int*)malloc(groesse * sizeof(int));
    return arr;
}

void speicher_freigeben(void* ptr) {
    if (ptr != NULL) {
        free(ptr);
    }
}