"""
Kapitel 11: Polymorphie & Interfaces 🎭📐
=========================================
Schulabgleich: 25.1 Polymorphie

Aufgabe:
Erstelle ein geometrisches Grafik- & Zeichenflächen-System mit Polymorphie.
Alle Formen (Rechteck, Kreis, Dreieck) besitzen dieselben Methoden (flaeche, umfang, info),
berechnen ihre Ergebnisse jedoch auf ihre jeweils eigene Weise.
Die Klasse 'Zeichenflaeche' kann beliebige Formen verwalten, ohne wissen zu müssen,
um welche konkrete Form es sich handelt!
"""

import math
from abc import ABC, abstractmethod
from typing import List, Optional


class Form(ABC):
    """
    Abstrakte Basisklasse (Interface) für alle geometrischen Formen.
    
    Attribute:
        farbe (str): Die Zeichenfarbe der Form (z.B. "rot", "blau", "gruen")
    """

    # ==========================================================================
    # 🎯 TEILZIEL 1 (TODO 1): Konstruktor __init__ der Basisklasse Form
    # Parameter: farbe (str = "schwarz")
    # Setze self.farbe = farbe
    # ==========================================================================
    def __init__(self, farbe: str = "schwarz"):
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 2 (TODO 2): Abstrakte Methode flaeche(self) -> float
    # Deklariere die Methode mit @abstractmethod.
    # Da es eine abstrakte Methode ist, enthält der Rumpf nur 'pass'.
    # ==========================================================================
    @abstractmethod
    def flaeche(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 3 (TODO 3): Abstrakte Methode umfang(self) -> float
    # Deklariere die Methode mit @abstractmethod.
    # Rumpf: 'pass'
    # ==========================================================================
    @abstractmethod
    def umfang(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 4 (TODO 4): Methode info(self) -> str
    # Gibt einen allgemeinen Infostring zurück:
    # Format: "{Klassenname} ({farbe}) - Fläche: {flaeche():.2f}, Umfang: {umfang():.2f}"
    # Tipp: self.__class__.__name__ liefert den Namen der jeweiligen Kindklasse!
    # Beispiel: "Form (schwarz) - Fläche: 0.00, Umfang: 0.00"
    # ==========================================================================
    def info(self) -> str:
        pass

    def __str__(self) -> str:
        return self.info()


class Rechteck(Form):
    """
    Rechteck-Form (erbt von Form).
    
    Attribute:
        breite (float): Breite des Rechtecks
        hoehe (float): Höhe des Rechtecks
        farbe (str): Farbe (Standardwert: "rot")
    """

    # ==========================================================================
    # 🎯 TEILZIEL 5 (TODO 5): Konstruktor __init__ von Rechteck
    # Parameter: breite (float), hoehe (float), farbe (str = "rot")
    # 1. Rufe super().__init__(farbe) auf.
    # 2. Setze self.breite = float(breite)
    # 3. Setze self.hoehe = float(hoehe)
    # ==========================================================================
    def __init__(self, breite: float, hoehe: float, farbe: str = "rot"):
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 6 (TODO 6): Methode flaeche(self) -> float (Überschreiben)
    # Formel: breite * hoehe
    # ==========================================================================
    def flaeche(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 7 (TODO 7): Methode umfang(self) -> float (Überschreiben)
    # Formel: 2 * (breite + hoehe)
    # ==========================================================================
    def umfang(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 8 (TODO 8): Methode info(self) -> str (Überschreiben)
    # Format: "Rechteck ({farbe}, {breite:.1f}x{hoehe:.1f}) - Fläche: {flaeche():.2f}, Umfang: {umfang():.2f}"
    # Beispiel: "Rechteck (rot, 4.0x5.0) - Fläche: 20.00, Umfang: 18.00"
    # ==========================================================================
    def info(self) -> str:
        pass


class Kreis(Form):
    """
    Kreis-Form (erbt von Form).
    
    Attribute:
        radius (float): Radius des Kreises
        farbe (str): Farbe (Standardwert: "blau")
    """

    # ==========================================================================
    # 🎯 TEILZIEL 9 (TODO 9): Konstruktor __init__ von Kreis
    # Parameter: radius (float), farbe (str = "blau")
    # 1. Rufe super().__init__(farbe) auf.
    # 2. Setze self.radius = float(radius)
    # ==========================================================================
    def __init__(self, radius: float, farbe: str = "blau"):
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 10 (TODO 10): Methode flaeche(self) -> float (Überschreiben)
    # Formel: math.pi * (radius ** 2)
    # ==========================================================================
    def flaeche(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 11 (TODO 11): Methode umfang(self) -> float (Überschreiben)
    # Formel: 2 * math.pi * radius
    # ==========================================================================
    def umfang(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 12 (TODO 12): Methode info(self) -> str (Überschreiben)
    # Format: "Kreis ({farbe}, r={radius:.1f}) - Fläche: {flaeche():.2f}, Umfang: {umfang():.2f}"
    # Beispiel: "Kreis (blau, r=3.0) - Fläche: 28.27, Umfang: 18.85"
    # ==========================================================================
    def info(self) -> str:
        pass


class Dreieck(Form):
    """
    Rechtwinkliges Dreieck (erbt von Form) mit Katheten a und b.
    
    Attribute:
        seite_a (float): Länge der ersten Kathete (Grundseite)
        seite_b (float): Länge der zweiten Kathete (Höhe)
        farbe (str): Farbe (Standardwert: "gruen")
    """

    # ==========================================================================
    # 🎯 TEILZIEL 13 (TODO 13): Konstruktor __init__ von Dreieck
    # Parameter: seite_a (float), seite_b (float), farbe (str = "gruen")
    # 1. Rufe super().__init__(farbe) auf.
    # 2. Setze self.seite_a = float(seite_a)
    # 3. Setze self.seite_b = float(seite_b)
    # ==========================================================================
    def __init__(self, seite_a: float, seite_b: float, farbe: str = "gruen"):
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 14 (TODO 14): Methode hypotenuse(self) -> float
    # Berechnet die dritte Seite c mit dem Satz des Pythagoras:
    # Formel: math.sqrt(seite_a**2 + seite_b**2)
    # ==========================================================================
    def hypotenuse(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 15 (TODO 15): Methode flaeche(self) -> float (Überschreiben)
    # Formel: 0.5 * seite_a * seite_b
    # ==========================================================================
    def flaeche(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 16 (TODO 16): Methode umfang(self) -> float (Überschreiben)
    # Formel: seite_a + seite_b + self.hypotenuse()
    # ==========================================================================
    def umfang(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 17 (TODO 17): Methode info(self) -> str (Überschreiben)
    # Format: "Dreieck ({farbe}, a={seite_a:.1f}, b={seite_b:.1f}, c={hypotenuse():.1f}) - Fläche: {flaeche():.2f}, Umfang: {umfang():.2f}"
    # Beispiel: "Dreieck (gruen, a=3.0, b=4.0, c=5.0) - Fläche: 6.00, Umfang: 12.00"
    # ==========================================================================
    def info(self) -> str:
        pass


class Zeichenflaeche:
    """
    Manager-Klasse zur polymorphen Verwaltung beliebig vieler geometrischer Formen.
    
    Attribute:
        name (str): Name der Zeichenfläche
        formen (list[Form]): Liste aller hinzugefügten Formen
    """

    # ==========================================================================
    # 🎯 TEILZIEL 18 (TODO 18): Konstruktor __init__ von Zeichenflaeche
    # Parameter: name (str = "Meine Zeichenfläche")
    # Attribute:
    #   - self.name: str = name
    #   - self.formen: list[Form] = [] (Startwert: leere Liste)
    # ==========================================================================
    def __init__(self, name: str = "Meine Zeichenfläche"):
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 19 (TODO 19): Methode hinzufuegen(self, form: Form) -> None
    # Fügt die übergebene Form zur Liste self.formen hinzu.
    # ==========================================================================
    def hinzufuegen(self, form: Form) -> None:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 20 (TODO 20): Methode anzahl_formen(self) -> int
    # Gibt die Anzahl der aktuell enthaltenen Formen zurück.
    # ==========================================================================
    def anzahl_formen(self) -> int:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 21 (TODO 21): Methode gesamte_flaeche(self) -> float (Polymorphie in Aktion!)
    # Berechnet die Summe aller Flächen der enthaltenen Formen.
    # Nutze eine Schleife oder sum(...), um form.flaeche() für jede Form aufzurufen.
    # Wenn self.formen leer ist: 0.0 zurückgeben.
    # ==========================================================================
    def gesamte_flaeche(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 22 (TODO 22): Methode gesamter_umfang(self) -> float (Polymorphie in Aktion!)
    # Berechnet die Summe aller Umfänge der enthaltenen Formen.
    # Nutze form.umfang() für jedes Objekt in self.formen.
    # Wenn self.formen leer ist: 0.0 zurückgeben.
    # ==========================================================================
    def gesamter_umfang(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 23 (TODO 23): Methode formen_nach_farbe(self, farbe: str) -> list[Form]
    # Filtert alle Formen heraus, die die angegebene Farbe haben.
    # WICHTIG: Groß-/Kleinschreibung ignorieren (z.B. mit farbe.lower())!
    # ==========================================================================
    def formen_nach_farbe(self, farbe: str) -> List[Form]:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 24 (TODO 24): Methode groesste_form(self) -> Form | None
    # Findet die Form mit dem größten Flächeninhalt (form.flaeche()).
    # Wenn die Liste leer ist: return None
    # Tipp: Nutze max(self.formen, key=lambda f: f.flaeche())
    # ==========================================================================
    def groesste_form(self) -> Optional[Form]:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 25 (TODO 25): Methode report(self) -> list[str]
    # Gibt eine Liste der info()-Texte aller enthaltenen Formen zurück.
    # ==========================================================================
    def report(self) -> List[str]:
        pass


# ==============================================================================
# Terminal-Test zum Ausprobieren: (python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("--- 🎭 Polymorphie Demo: Geometrische Formen ---")
    
    r = Rechteck(4.0, 5.0, farbe="rot")
    k = Kreis(3.0, farbe="blau")
    d = Dreieck(3.0, 4.0, farbe="gruen")

    # Polymorphe Liste durchlaufen:
    formen_liste: List[Form] = [r, k, d]
    
    for form in formen_liste:
        print(form.info())

    print("\n--- 🖼️ Zeichenfläche Manager ---")
    leinwand = Zeichenflaeche("Mathe-Poster")
    leinwand.hinzufuegen(r)
    leinwand.hinzufuegen(k)
    leinwand.hinzufuegen(d)
    leinwand.hinzufuegen(Kreis(1.5, farbe="rot"))

    print(f"Anzahl Formen: {leinwand.anzahl_formen()}")
    print(f"Gesamtfläche: {leinwand.gesamte_flaeche():.2f} cm²")
    print(f"Gesamtumfang: {leinwand.gesamter_umfang():.2f} cm")
    
    rote_formen = leinwand.formen_nach_farbe("rot")
    print(f"Rote Formen ({len(rote_formen)}): {[f.info() for f in rote_formen]}")
    
    groesste = leinwand.groesste_form()
    print(f"Größte Form: {groesste.info() if groesste else 'keine'}")
