#include <iostream>
#include <string>

namespace Mathe {
    void swap(int& a, int& b) {
        int temp = a;
        a = b;
        b = temp;
    }
}