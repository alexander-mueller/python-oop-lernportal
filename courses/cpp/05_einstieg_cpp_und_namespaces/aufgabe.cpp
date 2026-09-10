#include <iostream>
#include <string>

namespace Mathe {
    // 🎯 TEILZIEL 1 (TODO 1): Vertausche zwei Werte per Referenz
    void swap(int& a, int& b) {
        int temp = a;
        a = b;
        b = temp;
    }
}