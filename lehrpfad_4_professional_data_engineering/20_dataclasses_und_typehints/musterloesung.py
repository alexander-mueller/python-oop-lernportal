"""
Kapitel 20: Dataclasses, Type Hints & Decorators (Moderne Python-Architektur) 🏷️✨
==================================================================================
Musterlösung für moderne Python-Architektur mit Dataclasses, Typisierung und Decorators.
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
    """
    name: str
    preis: float
    kategorie: str = "Allgemein"

    def __post_init__(self) -> None:
        if not self.name or not str(self.name).strip():
            raise ValueError("Artikelname darf nicht leer sein!")
        if float(self.preis) < 0.0:
            raise ValueError("Preis darf nicht negativ sein!")

    def berechne_bruttopreis(self, mwst_satz: float = 0.19) -> float:
        """
        Berechnet den Bruttopreis inklusive Mehrwertsteuer, gerundet auf 2 Nachkommastellen.
        """
        if float(mwst_satz) < 0.0:
            raise ValueError("Mehrwertsteuersatz darf nicht negativ sein!")
        return round(float(self.preis) * (1.0 + float(mwst_satz)), 2)

    @classmethod
    def aus_csv_zeile(cls, csv_zeile: str) -> "Artikel":
        """
        Erstellt ein Artikel-Objekt aus einer CSV-Zeile wie 'Laptop;999.99;Elektronik'.
        """
        teile = [t.strip() for t in csv_zeile.split(";")]
        if len(teile) < 2:
            raise ValueError("CSV-Zeile muss mindestens Name und Preis enthalten!")
        
        name = teile[0]
        preis = float(teile[1])
        kategorie = teile[2] if len(teile) > 2 and teile[2] else "Allgemein"
        return cls(name=name, preis=preis, kategorie=kategorie)

    @staticmethod
    def ist_gueltiger_preis(preis: Any) -> bool:
        """
        Prüft statisch, ob ein Preis gültig (numerisch und >= 0) ist.
        """
        if isinstance(preis, (int, float)) and not isinstance(preis, bool):
            return preis >= 0.0
        return False


@dataclass
class Warenkorb:
    """
    Ein digitaler Warenkorb, der Artikel sammelt und verwaltet.
    """
    kunde: str
    artikel_liste: List[Artikel] = field(default_factory=list)

    def artikel_hinzufuegen(self, *artikel: Artikel) -> None:
        """
        Fügt beliebig viele Artikel (*args) zum Warenkorb hinzu.
        """
        for a in artikel:
            if not isinstance(a, Artikel):
                raise TypeError(f"Erwartete Artikel-Instanz, erhielt: {type(a).__name__}")
            self.artikel_liste.append(a)

    def artikel_entfernen(self, artikel_name: str) -> bool:
        """
        Entfernt den ersten Artikel mit dem passenden Namen (Groß-/Kleinschreibung ignorieren).
        """
        such_name = artikel_name.strip().lower()
        for a in self.artikel_liste:
            if a.name.strip().lower() == such_name:
                self.artikel_liste.remove(a)
                return True
        return False

    def gesamtsumme(self, brutto: bool = False, mwst_satz: float = 0.19) -> float:
        """
        Berechnet die Gesamtsumme aller Artikel im Warenkorb.
        """
        if not self.artikel_liste:
            return 0.0

        if brutto:
            summe = sum(a.berechne_bruttopreis(mwst_satz) for a in self.artikel_liste)
        else:
            summe = sum(a.preis for a in self.artikel_liste)

        return round(summe, 2)

    def __len__(self) -> int:
        return len(self.artikel_liste)


# ==============================================================================
# TEIL 2: EIGENE DECORATORS SCHREIBEN
# ==============================================================================

def aufruf_zaehler(func: Callable) -> Callable:
    """
    Ein Decorator, der zählt, wie oft eine dekorierte Funktion aufgerufen wurde.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.aufrufe += 1
        return func(*args, **kwargs)

    wrapper.aufrufe = 0
    return wrapper


def zeitmessung(func: Callable) -> Callable:
    """
    Ein Decorator, der die Ausführungszeit einer Funktion misst.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        ergebnis = func(*args, **kwargs)
        dauer = time.perf_counter() - start
        wrapper.letzte_dauer = dauer
        return ergebnis

    wrapper.letzte_dauer = 0.0
    return wrapper


# ==============================================================================
# TEIL 3: FORTGESCHRITTENE TYPE HINTS (UNION, DICT, TYPED DATA)
# ==============================================================================

def formatiere_benutzer(daten: Dict[str, Union[str, int, bool]]) -> str:
    """
    Formatiert ein Benutzer-Dictionary mit verschiedenen Datentypen zu einem
    lesbaren Status-String.
    """
    if "username" not in daten and "name" not in daten:
        raise KeyError("Benutzerdaten müssen 'username' oder 'name' enthalten!")

    username_val = daten.get("username", daten.get("name"))
    if not username_val or not str(username_val).strip():
        raise ValueError("Benutzername darf nicht leer sein!")

    username = str(username_val).strip()

    alter_val = daten.get("alter")
    alter_str = str(alter_val) if alter_val is not None else "Unbekannt"

    ist_admin = daten.get("ist_admin", False)
    rolle = "Administrator" if ist_admin else "Standardbenutzer"

    return f"Benutzer: {username} | Alter: {alter_str} | Rolle: {rolle}"


# ==============================================================================
# DEMONSTRATION & MAIN
# ==============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("🏷️ KAPITEL 20: MUSTERLÖSUNG – DATACLASSES & DECORATORS")
    print("=" * 70)

    # 1. Dataclass Artikel testen
    laptop = Artikel(name="ThinkPad X1", preis=1499.00, kategorie="Elektronik")
    print(f"\n📦 Artikel Dataclass:\n   {laptop}")
    print(f"   Bruttopreis (19%): {laptop.berechne_bruttopreis(0.19):.2f} €")

    # 2. CSV Fabrikmethode
    maus = Artikel.aus_csv_zeile("Logitech MX Master;99.90;Zubehoer")
    print(f"   Aus CSV erstellt: {maus}")

    # 3. Warenkorb testen
    korb = Warenkorb(kunde="Max Mustermann")
    korb.artikel_hinzufuegen(laptop, maus, Artikel("Kaffeebecher", 12.50, "Haushalt"))
    print(f"\n🛒 Warenkorb für {korb.kunde} ({len(korb)} Artikel):")
    print(f"   Nettosumme:  {korb.gesamtsumme():.2f} €")
    print(f"   Bruttosumme: {korb.gesamtsumme(brutto=True):.2f} €")

    # 4. Aufruf-Zähler Decorator
    @aufruf_zaehler
    def sage_hallo(name: str) -> str:
        return f"Hallo, {name}!"

    print("\n🔢 Aufruf-Zähler Decorator Test:")
    print(sage_hallo("Alice"))
    print(sage_hallo("Bob"))
    print(sage_hallo("Charlie"))
    print(f"   Anzahl Aufrufe: {sage_hallo.aufrufe}")

    # 5. Typsicherer Benutzer-Formatierer
    user = {"username": "CoderGirl99", "alter": 24, "ist_admin": True}
    print(f"\n👤 Benutzerdaten:\n   {formatiere_benutzer(user)}")

    print("\n" + "=" * 70)
    print("✅ Musterlösung erfolgreich ausgeführt!")
    print("=" * 70)
