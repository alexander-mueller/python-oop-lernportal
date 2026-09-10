#include <iostream>
#include <string>

class BankAccount {
private:
    std::string inhaber;
    double saldo;

public:
    BankAccount(std::string inhaber, double startSaldo) : inhaber(inhaber), saldo(startSaldo) {}

    void einzahlen(double betrag) {
        if (betrag > 0) saldo += betrag;
    }

    double getSaldo() const { return saldo; }
    std::string getInhaber() const { return inhaber; }
};