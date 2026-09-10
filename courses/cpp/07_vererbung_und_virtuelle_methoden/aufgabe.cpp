#include <iostream>
#include <string>

class Form {
public:
    virtual ~Form() = default;
    virtual double flaeche() const = 0;
};

class Rechteck : public Form {
private:
    double breite;
    double hoehe;

public:
    Rechteck(double b, double h) : breite(b), hoehe(h) {}
    double flaeche() const override { return breite * hoehe; }
};