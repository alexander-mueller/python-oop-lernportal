"""
Kapitel 12: Exceptions & Fehlerbehandlung 🛡️🛑
=============================================
Schulabgleich: 26.0 Exceptions & Fehlerklassen

Aufgabe:
Erstelle ein sicheres Bankkonto- & Geldautomat-System mit benutzerdefinierten
Exceptions und sauberer Fehlerbehandlung über try-except-else-finally.
"""

from typing import Optional


# ==============================================================================
# TODO 1: Eigene Exception-Klassen definieren
# ==============================================================================
# Erstelle eine Basis-Exception-Klasse 'BankFehler', die von 'Exception' erbt.
# Erstelle dann 4 abgeleitete Exception-Klassen, die alle von 'BankFehler' erben:
#   1. UngueltigePinError
#   2. KontoGesperrtError
#   3. NichtGenugGuthabenError
#   4. UngueltigerBetragError
# ==============================================================================

class BankFehler(Exception):
    pass


class UngueltigePinError(BankFehler):
    pass


class KontoGesperrtError(BankFehler):
    pass


class NichtGenugGuthabenError(BankFehler):
    pass


class UngueltigerBetragError(BankFehler):
    pass


# ==============================================================================
# TODO 2: Klasse Bankkonto
# ==============================================================================
class Bankkonto:
    def __init__(self, inhaber: str, pin: str, kontostand: float = 0.0):
        """
        Initialisiert ein Bankkonto.
        Attribute:
            - self.inhaber: str = inhaber
            - self.pin: str = pin
            - self.kontostand: float = float(kontostand)
            - self.gesperrt: bool = False (Standardwert)
            - self.fehlversuche: int = 0 (Zählt falsche PIN-Eingaben)
        
        WICHTIG:
            - Falls kontostand < 0 ist, wirf UngueltigerBetragError!
        """
        # TODO: Implementieren
        pass

    def pin_pruefen(self, eingegebene_pin: str) -> bool:
        """
        Prüft die eingegebene PIN.
        
        Ablauf:
        1. Wenn self.gesperrt True ist:
           -> Wirf sofort KontoGesperrtError("Konto ist gesperrt!")
        2. Wenn eingegebene_pin == self.pin:
           -> Setze self.fehlversuche = 0 zurück
           -> Gib True zurück
        3. Wenn eingegebene_pin != self.pin:
           -> Erhöhe self.fehlversuche um 1
           -> Wenn self.fehlversuche >= 3:
                - Setze self.gesperrt = True
                - Wirf KontoGesperrtError("PIN 3-mal falsch. Konto wurde gesperrt!")
           -> Andernfalls:
                - Wirf UngueltigePinError(f"Falsche PIN! Noch {3 - self.fehlversuche} Versuche.")
        """
        # TODO: Implementieren
        pass

    def einzahlen(self, betrag: float) -> float:
        """
        Zahlt einen Betrag auf das Konto ein.
        
        Regeln:
        1. Wenn self.gesperrt:
           -> Wirf KontoGesperrtError
        2. Wenn betrag <= 0:
           -> Wirf UngueltigerBetragError
        3. Erhöhe self.kontostand um betrag und gib den neuen kontostand zurück.
        """
        # TODO: Implementieren
        pass

    def abheben(self, betrag: float, pin: str) -> float:
        """
        Hebt Geld vom Konto ab.
        
        Regeln:
        1. Prüfe zuerst die PIN mit self.pin_pruefen(pin)
           (wirft bei falscher PIN oder Sperre automatisch die passende Exception)
        2. Wenn betrag <= 0:
           -> Wirf UngueltigerBetragError
        3. Wenn betrag > self.kontostand:
           -> Wirf NichtGenugGuthabenError
        4. Ziehe betrag von self.kontostand ab und gib den neuen kontostand zurück.
        """
        # TODO: Implementieren
        pass

    def sperren(self) -> None:
        """Sperrt das Konto manuell."""
        self.gesperrt = True

    def entsperren(self, admin_passwort: str) -> bool:
        """
        Entsperrt das Konto, wenn admin_passwort == 'ADMIN123' ist.
        Setzt self.gesperrt = False und self.fehlversuche = 0.
        Falls das Passwort falsch ist, wirf UngueltigePinError.
        """
        # TODO: Implementieren
        pass

    def __str__(self) -> str:
        """
        Gibt einen Status-String zurück:
        z.B. "Bankkonto(Max, Stand: 150.00€, Status: AKTIV)"
        bzw. "Bankkonto(Max, Stand: 150.00€, Status: GESPERRT)"
        """
        # TODO: Implementieren
        pass


# ==============================================================================
# TODO 3: Geldautomat-Auszahlung mit try - except - else - finally
# ==============================================================================
def geldautomat_abheben(konto: Bankkonto, betrag: float, pin: str) -> str:
    """
    Führt eine Abhebung an einem Geldautomaten durch und fängt alle Fehler sauber ab.
    
    Verwende die vollständige try-except-else-finally-Struktur:
    
    Ablauf:
    1. Erstelle eine leere Liste 'meldungen = []'
    2. try:
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
    
    3. Gib die Meldungen mit ' | '.join(meldungen) als einzelnen String zurück.
    """
    # TODO: Implementieren
    pass


# ==============================================================================
# Kleiner Test zum Ausprobieren im Terminal:
# (python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    konto = Bankkonto("Anna", "1234", 250.0)
    print("Konto erstellt:", konto)

    print("\n--- Test 1: Erfolgreiche Abhebung ---")
    resultat = geldautomat_abheben(konto, 50.0, "1234")
    print(resultat)

    print("\n--- Test 2: Falsche PIN ---")
    resultat = geldautomat_abheben(konto, 50.0, "9999")
    print(resultat)

    print("\n--- Test 3: Zu viel abheben ---")
    resultat = geldautomat_abheben(konto, 500.0, "1234")
    print(resultat)
