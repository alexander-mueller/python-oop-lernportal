"""
Kapitel 12: Exceptions & Fehlerbehandlung 🛡️🛑
=============================================
Musterlösung für die Bankkonto- und Geldautomat-Simulation.
"""

from typing import Optional


# ==============================================================================
# 1. Eigene Exception-Hierarchie
# ==============================================================================
class BankFehler(Exception):
    """Basisklasse für alle Fehler im Bankkonto-System."""
    pass


class UngueltigePinError(BankFehler):
    """Wird geworfen, wenn die eingegebene PIN falsch ist."""
    pass


class KontoGesperrtError(BankFehler):
    """Wird geworfen, wenn das Konto gesperrt ist (oder nach 3 Fehlversuchen gesperrt wird)."""
    pass


class NichtGenugGuthabenError(BankFehler):
    """Wird geworfen, wenn das Guthaben für eine Abhebung nicht ausreicht."""
    pass


class UngueltigerBetragError(BankFehler):
    """Wird geworfen, wenn ein ungültiger (z.B. <= 0) Betrag übergeben wird."""
    pass


# ==============================================================================
# 2. Klasse Bankkonto
# ==============================================================================
class Bankkonto:
    def __init__(self, inhaber: str, pin: str, kontostand: float = 0.0):
        """Initialisiert ein Bankkonto mit Inhaber, PIN und Startguthaben."""
        if kontostand < 0:
            raise UngueltigerBetragError("Der Anfangskontostand darf nicht negativ sein!")
        self.inhaber: str = inhaber
        self.pin: str = pin
        self.kontostand: float = float(kontostand)
        self.gesperrt: bool = False
        self.fehlversuche: int = 0

    def pin_pruefen(self, eingegebene_pin: str) -> bool:
        """Prüft die PIN, zählt Fehlversuche und sperrt ggf. das Konto."""
        if self.gesperrt:
            raise KontoGesperrtError(f"Das Konto von {self.inhaber} ist gesperrt!")

        if eingegebene_pin == self.pin:
            self.fehlversuche = 0
            return True
        else:
            self.fehlversuche += 1
            if self.fehlversuche >= 3:
                self.gesperrt = True
                raise KontoGesperrtError("PIN 3-mal falsch eingegeben! Das Konto wurde aus Sicherheitsgründen gesperrt.")
            raise UngueltigePinError(f"Falsche PIN! Verbleibende Versuche: {3 - self.fehlversuche}")

    def einzahlen(self, betrag: float) -> float:
        """Zahlt Geld auf das Konto ein."""
        if self.gesperrt:
            raise KontoGesperrtError(f"Das Konto von {self.inhaber} ist gesperrt!")
        if betrag <= 0:
            raise UngueltigerBetragError("Einzahlungsbetrag muss größer als 0 sein!")
        self.kontostand += betrag
        return self.kontostand

    def abheben(self, betrag: float, pin: str) -> float:
        """Hebt Geld nach erfolgreicher PIN- und Guthabenprüfung ab."""
        # 1. PIN & Sperre prüfen (wirft automatisch passende Fehler)
        self.pin_pruefen(pin)

        # 2. Betrag prüfen
        if betrag <= 0:
            raise UngueltigerBetragError("Abhebebetrag muss größer als 0 sein!")

        # 3. Deckung prüfen
        if betrag > self.kontostand:
            raise NichtGenugGuthabenError(f"Nicht genug Guthaben! Verfügbar: {self.kontostand:.2f}€, Angefordert: {betrag:.2f}€")

        self.kontostand -= betrag
        return self.kontostand

    def sperren(self) -> None:
        """Sperrt das Konto manuell."""
        self.gesperrt = True

    def entsperren(self, admin_passwort: str) -> bool:
        """Entsperrt das Konto bei korrektem Admin-Passwort."""
        if admin_passwort == "ADMIN123":
            self.gesperrt = False
            self.fehlversuche = 0
            return True
        raise UngueltigePinError("Falsches Admin-Passwort zum Entsperren!")

    def __str__(self) -> str:
        """String-Repräsentation des Kontos."""
        status = "GESPERRT" if self.gesperrt else "AKTIV"
        return f"Bankkonto({self.inhaber}, Stand: {self.kontostand:.2f}€, Status: {status})"


# ==============================================================================
# 3. Geldautomat mit vollständiger try-except-else-finally-Struktur
# ==============================================================================
def geldautomat_abheben(konto: Bankkonto, betrag: float, pin: str) -> str:
    """Führt eine sichere Abhebung mit try-except-else-finally durch."""
    meldungen = []
    try:
        konto.abheben(betrag, pin)
    except UngueltigePinError as e:
        meldungen.append(f"PIN-Fehler: {e}")
    except KontoGesperrtError as e:
        meldungen.append(f"Sicherheits-Fehler: {e}")
    except NichtGenugGuthabenError as e:
        meldungen.append(f"Deckungs-Fehler: {e}")
    except UngueltigerBetragError as e:
        meldungen.append(f"Betrags-Fehler: {e}")
    except BankFehler as e:
        meldungen.append(f"Bank-Fehler: {e}")
    else:
        meldungen.append(f"Auszahlung erfolgreich: {betrag:.2f}€ ausgezahlt. Neuer Stand: {konto.kontostand:.2f}€")
    finally:
        meldungen.append("Bitte Karte entnehmen.")

    return " | ".join(meldungen)


if __name__ == "__main__":
    konto = Bankkonto("Anna", "1234", 250.0)
    print(konto)
    print(geldautomat_abheben(konto, 50.0, "1234"))
    print(geldautomat_abheben(konto, 50.0, "9999"))
    print(geldautomat_abheben(konto, 500.0, "1234"))
