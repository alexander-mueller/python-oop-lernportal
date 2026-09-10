#include <iostream>
#include <vector>
#include <cassert>
#include <cstddef>

extern "C" {
    void tausche_werte(int* a, int* b);
    void multipliziere_und_addiere(int a, int b, int* prod, int* sum);
    void finde_max_und_min(const int* arr, size_t size, int* out_min, int* out_max);
    size_t pointer_schrittweite(int typ_id);
    int array_summe_zeigerarithmetik(const int* start, size_t count);
}

// TEST: Teilziel 1 - tausche_werte
TEST(C02_Pointer, Teilziel1_TauscheWerte) {
    int x = 42;
    int y = 99;
    tausche_werte(&x, &y);
    assert(x == 99);
    assert(y == 42);

    // Nullpointer safety check
    tausche_werte(nullptr, &y);
    assert(y == 42);
    tausche_werte(&x, nullptr);
    assert(x == 99);
}

// TEST: Teilziel 2 - multipliziere_und_addiere
TEST(C02_Pointer, Teilziel2_MultipliziereUndAddiere) {
    int p = 0, s = 0;
    multipliziere_und_addiere(5, 8, &p, &s);
    assert(p == 40);
    assert(s == 13);

    multipliziere_und_addiere(-3, 7, &p, &s);
    assert(p == -21);
    assert(s == 4);

    // Partial null check
    multipliziere_und_addiere(4, 5, nullptr, &s);
    assert(s == 9);
}

// TEST: Teilziel 3 - finde_max_und_min
TEST(C02_Pointer, Teilziel3_FindeMaxUndMin) {
    int arr[] = {23, -5, 88, 12, -40, 60};
    int min_val = 0, max_val = 0;
    finde_max_und_min(arr, 6, &min_val, &max_val);
    assert(min_val == -40);
    assert(max_val == 88);

    int single[] = {100};
    finde_max_und_min(single, 1, &min_val, &max_val);
    assert(min_val == 100);
    assert(max_val == 100);
}

// TEST: Teilziel 4 - pointer_schrittweite
TEST(C02_Pointer, Teilziel4_PointerSchrittweite) {
    assert(pointer_schrittweite(1) == sizeof(char));
    assert(pointer_schrittweite(2) == sizeof(int));
    assert(pointer_schrittweite(3) == sizeof(double));
    assert(pointer_schrittweite(99) == 0);
}

// TEST: Teilziel 5 - array_summe_zeigerarithmetik
TEST(C02_Pointer, Teilziel5_ArraySummeZeigerarithmetik) {
    int arr[] = {1, 2, 3, 4, 5, 10};
    assert(array_summe_zeigerarithmetik(arr, 6) == 25);
    assert(array_summe_zeigerarithmetik(arr, 3) == 6);
    assert(array_summe_zeigerarithmetik(nullptr, 5) == 0);
    assert(array_summe_zeigerarithmetik(arr, 0) == 0);
}

int main() {
    std::cout << "Running GoogleTest Suite for C 02...\n";
    return 0;
}
