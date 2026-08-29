"""
Kapitel 11: Polymorphie & Interfaces – Musterlösung 🎭📐
=========================================================
Schulabgleich: 25.1 Polymorphie
"""

import math
from abc import ABC, abstractmethod
from typing import List, Optional


class Form(ABC):
    """Abstrakte Basisklasse (Interface) für alle geometrischen Formen."""

    def __init__(self, farbe: str = "schwarz"):
        self.farbe: str = farbe

    @abstractmethod
    def flaeche(self) -> float:
        pass

    @abstractmethod
    def umfang(self) -> float:
        pass

    def info(self) -> str:
        return f"{self.__class__.__name__} ({self.farbe}) - Fläche: {self.flaeche():.2f}, Umfang: {self.umfang():.2f}"

    def __str__(self) -> str:
        return self.info()


class Rechteck(Form):
    """Rechteck-Form (erbt von Form)."""

    def __init__(self, breite: float, hoehe: float, farbe: str = "rot"):
        super().__init__(farbe)
        self.breite: float = float(breite)
        self.hoehe: float = float(hoehe)

    def flaeche(self) -> float:
        return self.breite * self.hoehe

    def umfang(self) -> float:
        return 2.0 * (self.breite + self.hoehe)

    def info(self) -> str:
        return f"Rechteck ({self.farbe}, {self.breite:.1f}x{self.hoehe:.1f}) - Fläche: {self.flaeche():.2f}, Umfang: {self.umfang():.2f}"


class Kreis(Form):
    """Kreis-Form (erbt von Form)."""

    def __init__(self, radius: float, farbe: str = "blau"):
        super().__init__(farbe)
        self.radius: float = float(radius)

    def flaeche(self) -> float:
        return math.pi * (self.radius ** 2)

    def umfang(self) -> float:
        return 2.0 * math.pi * self.radius

    def info(self) -> str:
        return f"Kreis ({self.farbe}, r={self.radius:.1f}) - Fläche: {self.flaeche():.2f}, Umfang: {self.umfang():.2f}"


class Dreieck(Form):
    """Rechtwinkliges Dreieck (erbt von Form) mit Katheten a und b."""

    def __init__(self, seite_a: float, seite_b: float, farbe: str = "gruen"):
        super().__init__(farbe)
        self.seite_a: float = float(seite_a)
        self.seite_b: float = float(seite_b)

    def hypotenuse(self) -> float:
        return math.sqrt(self.seite_a ** 2 + self.seite_b ** 2)

    def flaeche(self) -> float:
        return 0.5 * self.seite_a * self.seite_b

    def umfang(self) -> float:
        return self.seite_a + self.seite_b + self.hypotenuse()

    def info(self) -> str:
        return (
            f"Dreieck ({self.farbe}, a={self.seite_a:.1f}, b={self.seite_b:.1f}, "
            f"c={self.hypotenuse():.1f}) - Fläche: {self.flaeche():.2f}, Umfang: {self.umfang():.2f}"
        )


class Zeichenflaeche:
    """Manager-Klasse zur polymorphen Verwaltung beliebig vieler geometrischer Formen."""

    def __init__(self, name: str = "Meine Zeichenfläche"):
        self.name: str = name
        self.formen: List[Form] = []

    def hinzufuegen(self, form: Form) -> None:
        self.formen.append(form)

    def anzahl_formen(self) -> int:
        return len(self.formen)

    def gesamte_flaeche(self) -> float:
        return sum(f.flaeche() for f in self.formen)

    def gesamter_umfang(self) -> float:
        return sum(f.umfang() for f in self.formen)

    def formen_nach_farbe(self, farbe: str) -> List[Form]:
        return [f for f in self.formen if f.farbe.lower() == farbe.lower()]

    def groesste_form(self) -> Optional[Form]:
        if not self.formen:
            return None
        return max(self.formen, key=lambda f: f.flaeche())

    def report(self) -> List[str]:
        return [f.info() for f in self.formen]


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
