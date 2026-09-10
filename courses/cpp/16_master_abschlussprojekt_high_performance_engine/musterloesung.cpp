#include <iostream>
#include <vector>
#include <memory>

struct Partikel {
    double x, y;
    double vx, vy;

    Partikel(double x, double y, double vx, double vy) : x(x), y(y), vx(vx), vy(vy) {}

    void update(double dt) {
        x += vx * dt;
        y += vy * dt;
    }
};

class PhysikWelt {
private:
    std::vector<std::unique_ptr<Partikel>> partikel_liste;

public:
    void addPartikel(double x, double y, double vx, double vy) {
        partikel_liste.push_back(std::make_unique<Partikel>(x, y, vx, vy));
    }

    void schritt(double dt) {
        for (auto& p : partikel_liste) {
            p->update(dt);
        }
    }

    size_t getAnzahl() const { return partikel_liste.size(); }
};