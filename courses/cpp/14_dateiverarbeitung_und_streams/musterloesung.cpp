#include <iostream>
#include <fstream>
#include <string>

bool schreibeTextDatei(const std::string& pfad, const std::string& inhalt) {
    std::ofstream out(pfad);
    if (!out.is_open()) return false;
    out << inhalt;
    return true;
}