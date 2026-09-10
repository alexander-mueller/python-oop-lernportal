#include <iostream>

class Vektor2D {
public:
    double x, y;

    Vektor2D(double x = 0, double y = 0) : x(x), y(y) {}

    // 🎯 TEILZIEL 1 (TODO 1): Überlade den +-Operator
    Vektor2D operator+(const Vektor2D& other) const {
        return Vektor2D(x + other.x, y + other.y);
    }

    bool operator==(const Vektor2D& other) const {
        return x == other.x && y == other.y;
    }
};