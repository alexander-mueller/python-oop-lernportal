#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <cassert>

// Include or declare C functions
extern "C" {
    double berechne_sensor_mittelwert(int summe, int anzahl);
    void formatiere_messpunkt(char* buffer, size_t buf_size, int sensor_id, double temperatur, char einheit);
    int pruefe_datenbereich(int wert, int min_val, int max_val);
    double konvertiere_celsius_zu_fahrenheit(double celsius);
    size_t ermittle_typ_groesse(int typ_code);
}

// TEST: Teilziel 1 - berechne_sensor_mittelwert
TEST(C01_SyntaxIO, Teilziel1_MittelwertBerechnung) {
    double res1 = berechne_sensor_mittelwert(150, 4);
    assert(std::abs(res1 - 37.5) < 0.0001);

    double res2 = berechne_sensor_mittelwert(10, 3);
    assert(std::abs(res2 - 3.333333) < 0.001);

    double res3 = berechne_sensor_mittelwert(50, 0);
    assert(res3 == 0.0);

    double res4 = berechne_sensor_mittelwert(50, -2);
    assert(res4 == 0.0);
}

// TEST: Teilziel 2 - formatiere_messpunkt
TEST(C01_SyntaxIO, Teilziel2_FormatiereMesspunkt) {
    char buf[64];
    std::memset(buf, 0, sizeof(buf));
    formatiere_messpunkt(buf, sizeof(buf), 5, 23.456, 'C');
    assert(std::string(buf) == "Sensor #5: 23.46 C");

    formatiere_messpunkt(buf, sizeof(buf), 102, 98.601, 'F');
    assert(std::string(buf) == "Sensor #102: 98.60 F");
}

// TEST: Teilziel 3 - pruefe_datenbereich
TEST(C01_SyntaxIO, Teilziel3_PruefeDatenbereich) {
    assert(pruefe_datenbereich(15, 10, 20) == 1);
    assert(pruefe_datenbereich(10, 10, 20) == 1);
    assert(pruefe_datenbereich(20, 10, 20) == 1);
    assert(pruefe_datenbereich(9, 10, 20) == 0);
    assert(pruefe_datenbereich(21, 10, 20) == 0);
}

// TEST: Teilziel 4 - konvertiere_celsius_zu_fahrenheit
TEST(C01_SyntaxIO, Teilziel4_CelsiusZuFahrenheit) {
    assert(std::abs(konvertiere_celsius_zu_fahrenheit(0.0) - 32.0) < 0.0001);
    assert(std::abs(konvertiere_celsius_zu_fahrenheit(100.0) - 212.0) < 0.0001);
    assert(std::abs(konvertiere_celsius_zu_fahrenheit(-40.0) - (-40.0)) < 0.0001);
}

// TEST: Teilziel 5 - ermittle_typ_groesse
TEST(C01_SyntaxIO, Teilziel5_ErmittleTypGroesse) {
    assert(ermittle_typ_groesse(1) == sizeof(char));
    assert(ermittle_typ_groesse(2) == sizeof(int));
    assert(ermittle_typ_groesse(3) == sizeof(double));
    assert(ermittle_typ_groesse(4) == sizeof(long long));
    assert(ermittle_typ_groesse(99) == 0);
}

int main() {
    std::cout << "Running GoogleTest Suite for C 01...\n";
    return 0;
}
