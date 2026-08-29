"""
Kapitel 20: Dataclasses, Type Hints & Decorators (Moderne Python-Architektur) 🏷️✨
==================================================================================
Lerne moderne Python-Architekturmuster für typsicheren, sauberen Code:
1. @dataclass (Automatische Konstruktoren, __repr__, __eq__, field(default_factory=...))
2. Fortgeschrittene Type Hints (Optional, Union, Callable, Dict, List)
3. Eigene Decorators schreiben (@functools.wraps, Wrapper-Funktionen)
4. Standard-Decorators (@property, @classmethod, @staticmethod)

Didaktische Analogie:
- "Gussform / Fertighaus" (@dataclass): Spart seitenlangen Boilerplate-Code für __init__, __repr__ etc.
- "Geschenkverpackung / Schutzhülle" (Decorator): Erweitert Funktionen um Logging, Zähler oder Zeitmessung, ohne ihren Code zu ändern.
"""

import time
import functools
from dataclasses import dataclass, field
from typing import Optional, Union, Callable, List, Dict, Any


# ==============================================================================
# TEIL 1: DATACLASSES FÜR TYPSICHERE DATENMODELLE
# ==============================================================================

@dataclass
class Artikel:
    """
    Ein Artikel im Online-Shop als moderne Dataclass.

    Attribute:
        name (str): Artikelbezeichnung (darf nicht leer sein).
        preis (float): Nettopreis in Euro (muss >= 0 sein).
        kategorie (str): Warengruppe (Standard: 'Allgemein').
    """
    name: str
    preis: float
    kategorie: str = "Allgemein"

    def __post_init__(self) -> None:
        """
        Wird automatisch direkt nach dem generierten __init__ aufgerufen.
        Validiere hier die Daten!
        """
        # ======================================================================
        # 🎯 TEILZIEL 1 (TODO 1): Validierung in __post_init__
        # 1. Wenn name leer oder nur Leerzeichen ist, löse ValueError aus.
        # 2. Wenn preis < 0 ist, löse ValueError aus.
        # ======================================================================
        pass

    def berechne_bruttopreis(self, mwst_satz: float = 0.19) -> float:
        """
        Berechnet den Bruttopreis inklusive Mehrwertsteuer, gerundet auf 2 Nachkommastellen.

        Parameter:
            mwst_satz (float): Mehrwertsteuersatz als Dezimalzahl (z.B. 0.19 für 19%).

        Exceptions:
            ValueError: Falls mwst_satz < 0 ist.

        Beispiele:
            Artikel("Buch", 10.0).berechne_bruttopreis(0.07) -> 10.7
            Artikel("Maus", 20.0).berechne_bruttopreis(0.19) -> 23.8
        """
        # ======================================================================
        # 🎯 TEILZIEL 2 (TODO 2): Implementiere berechne_bruttopreis
        # 1. Validiere: mwst_satz darf nicht negativ (< 0) sein.
        # 2. Berechne: preis * (1.0 + mwst_satz)
        # 3. Runde auf 2 Dezimalstellen mit round(..., 2) und gib den Wert zurück.
        # ======================================================================
        pass

    @classmethod
    def aus_csv_zeile(cls, csv_zeile: str) -> "Artikel":
        """
        Erstellt ein Artikel-Objekt aus einer CSV-Zeile wie 'Laptop;999.99;Elektronik'.
        """
        # ======================================================================
        # 🎯 TEILZIEL 3 (TODO 3): Implementiere die @classmethod aus_csv_zeile
        # 1. Trenne die csv_zeile an Semikolons (csv_zeile.split(';')).
        # 2. Entpacke name, preis (als float) und optional kategorie.
        # 3. Erzeuge und gib eine neue Instanz mit cls(...) zurück.
        # ======================================================================
        pass

    @staticmethod
    def ist_gueltiger_preis(preis: float) -> bool:
        """
        Prüft statisch, ob ein Preis gültig (numerisch und >= 0) ist.
        """
        # ======================================================================
        # 🎯 TEILZIEL 4 (TODO 4): Implementiere die @staticmethod ist_gueltiger_preis
        # 1. Gib True zurück, wenn preis ein int oder float ist und preis >= 0.0.
        # ======================================================================
        pass


@dataclass
class Warenkorb:
    """
    Ein digitaler Warenkorb, der Artikel sammelt und verwaltet.

    Attribute:
        kunde (str): Name des Kunden.
        artikel_liste (list[Artikel]): Liste der Artikel (nutze field(default_factory=list)!).
    """
    kunde: str
    artikel_liste: List[Artikel] = field(default_factory=list)

    def artikel_hinzufuegen(self, *artikel: Artikel) -> None:
        """
        Fügt beliebig viele Artikel (*args) zum Warenkorb hinzu.

        Exceptions:
            TypeError: Falls ein Element kein Artikel-Objekt ist.
        """
        # ======================================================================
        # 🎯 TEILZIEL 5 (TODO 5): Implementiere artikel_hinzufuegen
        # 1. Iteriere über alle übergebenen Artikel.
        # 2. Prüfe mit isinstance(a, Artikel), ob der Typ stimmt (sonst TypeError).
        # 3. Hänge das Element an self.artikel_liste an.
        # ======================================================================
        pass

    def artikel_entfernen(self, artikel_name: str) -> bool:
        """
        Entfernt den ersten Artikel mit dem passenden Namen (Groß-/Kleinschreibung ignorieren).
        Gibt True zurück, wenn der Artikel gefunden und entfernt wurde, sonst False.
        """
        # ======================================================================
        # 🎯 TEILZIEL 6 (TODO 6): Implementiere artikel_entfernen
        # 1. Durchsuche self.artikel_liste nach einem Artikel mit a.name.lower() == artikel_name.lower().
        # 2. Entferne ihn mit self.artikel_liste.remove(a) und gib True zurück.
        # 3. Wenn nicht gefunden, gib False zurück.
        # ======================================================================
        pass

    def gesamtsumme(self, brutto: bool = False, mwst_satz: float = 0.19) -> float:
        """
        Berechnet die Gesamtsumme aller Artikel im Warenkorb.

        Parameter:
            brutto (bool): Wenn True, wird der Bruttopreis mit mwst_satz summiert.
            mwst_satz (float): Der MwSt-Satz bei Bruttoberechnung.

        Rückgabe:
            float: Die auf 2 Stellen gerundete Gesamtsumme.
        """
        # ======================================================================
        # 🎯 TEILZIEL 7 (TODO 7): Implementiere gesamtsumme
        # 1. Wenn brutto == True: Summiere a.berechne_bruttopreis(mwst_satz) für alle Artikel.
        # 2. Wenn brutto == False: Summiere a.preis für alle Artikel.
        # 3. Runde auf 2 Nachkommastellen und gib den Wert zurück (bei leerem Korb 0.0).
        # ======================================================================
        pass

    def __len__(self) -> int:
        """Gibt die Anzahl der Artikel im Warenkorb zurück."""
        return len(self.artikel_liste)


# ==============================================================================
# TEIL 2: EIGENE DECORATORS SCHREIBEN
# ==============================================================================

def aufruf_zaehler(func: Callable) -> Callable:
    """
    Ein Decorator, der zählt, wie oft eine dekorierte Funktion aufgerufen wurde.
    Der Zähler wird als Attribut 'aufrufe' an der Wrapper-Funktion hinterlegt.

    Beispiel:
        @aufruf_zaehler
        def gruss(name):
            return f"Hallo {name}"

        gruss("Anna")
        gruss.aufrufe  # -> 1
        gruss("Ben")
        gruss.aufrufe  # -> 2
    """
    # ==========================================================================
    # 🎯 TEILZIEL 8 (TODO 8): Implementiere den Decorator aufruf_zaehler
    # 1. Definiere die innere Funktion wrapper(*args, **kwargs).
    # 2. Nutze @functools.wraps(func) über der wrapper-Funktion.
    # 3. Erhöhe wrapper.aufrufe um 1.
    # 4. Führe func(*args, **kwargs) aus und gib das Ergebnis zurück.
    # 5. Initialisiere wrapper.aufrufe = 0 vor der Rückgabe von wrapper.
    # ==========================================================================
    pass


def zeitmessung(func: Callable) -> Callable:
    """
    Ein Decorator, der die Ausführungszeit einer Funktion misst und die Dauer
    als Attribut 'letzte_dauer' (in Sekunden) an der Wrapper-Funktion speichert.
    """
    # ==========================================================================
    # 🎯 TEILZIEL 9 (TODO 9): Implementiere den Decorator zeitmessung
    # 1. Definiere wrapper(*args, **kwargs) mit @functools.wraps(func).
    # 2. Miss die Startzeit mit time.perf_counter().
    # 3. Führe das Original func(*args, **kwargs) aus.
    # 4. Berechne dauer = time.perf_counter() - start_zeit.
    # 5. Speichere wrapper.letzte_dauer = dauer.
    # 6. Gib das Funktionsergebnis zurück.
    # 7. Initialisiere wrapper.letzte_dauer = 0.0 vor der Rückgabe von wrapper.
    # ==========================================================================
    pass


# ==============================================================================
# TEIL 3: FORTGESCHRITTENE TYPE HINTS (UNION, DICT, TYPED DATA)
# ==============================================================================

def formatiere_benutzer(daten: Dict[str, Union[str, int, bool]]) -> str:
    """
    Formatiert ein Benutzer-Dictionary mit verschiedenen Datentypen zu einem
    lesbaren Status-String.

    Erwartete Schlüssel im Dict:
        - "username" (str, Pflicht): Der Benutzername.
        - "alter" (int, optional): Alter in Jahren.
        - "ist_admin" (bool, optional): Ob der Benutzer Administratorrechte besitzt.

    Rückgabe:
        str: Formatierter String, z.B.
             "Benutzer: Alice | Alter: 28 | Rolle: Administrator" oder
             "Benutzer: Bob | Alter: Unbekannt | Rolle: Standardbenutzer"

    Exceptions:
        KeyError: Falls der Pflichtschlüssel "username" fehlt.
        ValueError: Falls "username" ein leerer String ist.
    """
    # ==========================================================================
    # 🎯 TEILZIEL 10 (TODO 10): Implementiere formatiere_benutzer
    # 1. Prüfe, ob "username" in daten enthalten ist (wenn nicht -> KeyError).
    # 2. Prüfe, ob daten["username"] ein nicht-leerer String ist (wenn nicht -> ValueError).
    # 3. Lese das Alter: Wenn vorhanden, nutze den Wert, sonst "Unbekannt".
    # 4. Lese "ist_admin": Wenn True, rolle = "Administrator", sonst "Standardbenutzer".
    # 5. Gib den String im Format:
    #    "Benutzer: {username} | Alter: {alter} | Rolle: {rolle}" zurück.
    # ==========================================================================
    pass


# ==============================================================================
# DEMONSTRATION & MAIN
# ==============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("🏷️ KAPITEL 20: DATACLASSES, TYPE HINTS & DECORATORS")
    print("=" * 70)

    # 1. Dataclass Artikel testen
    laptop = Artikel(name="ThinkPad X1", preis=1499.00, kategorie="Elektronik")
    print(f"\n📦 Artikel Dataclass:\n   {laptop}")
    print(f"   Bruttopreis (19%): {laptop.berechne_bruttopreis(0.19):.2f} €")

    # 2. Warenkorb testen
    korb = Warenkorb(kunde="Max Mustermann")
    korb.artikel_hinzufuegen(
        laptop,
        Artikel("USB-C Hub", 39.90, "Zubehoer"),
        Artikel("Kaffeebecher", 12.50, "Haushalt")
    )
    print(f"\n🛒 Warenkorb für {korb.kunde} ({len(korb)} Artikel):")
    print(f"   Nettosumme:  {korb.gesamtsumme():.2f} €")
    print(f"   Bruttosumme: {korb.gesamtsumme(brutto=True):.2f} €")

    # 3. Aufruf-Zähler Decorator
    @aufruf_zaehler
    def sage_hallo(name: str) -> str:
        return f"Hallo, {name}!"

    print("\n🔢 Aufruf-Zähler Decorator Test:")
    print(sage_hallo("Alice"))
    print(sage_hallo("Bob"))
    print(f"   Anzahl Aufrufe: {sage_hallo.aufrufe}")

    # 4. Typsicherer Benutzer-Formatierer
    user = {"username": "CoderGirl99", "alter": 24, "ist_admin": True}
    print(f"\n👤 Benutzerdaten:\n   {formatiere_benutzer(user)}")

    print("\n" + "=" * 70)
    print("💡 Starte die Tests mit: python3 test_aufgabe.py")
    print("=" * 70)
