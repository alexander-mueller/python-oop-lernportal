"""
Kapitel 10: Vererbung (Inheritance) & super() 🧬🚗
===================================================
Schulabgleich: 25.0 Vererbung

Aufgabe:
Erstelle eine Hierarchie von Fahrzeugen für eine moderne Fahrzeugflotte.
Nutze Vererbung (DRY-Prinzip) und super().__init__(), um gemeinsame Attribute
und Methoden von der Basisklasse 'Fahrzeug' an 'Auto', 'ElektroAuto' und 'Lkw' zu vererben.
"""

from typing import List, Optional


class Fahrzeug:
    """
    Basisklasse für alle Fahrzeuge.
    
    Attribute:
        marke (str): Hersteller (z.B. "BMW", "Tesla", "MAN")
        modell (str): Modellbezeichnung (z.B. "i4", "Model 3", "TGX")
        baujahr (int): Baujahr des Fahrzeugs (z.B. 2022)
        grundpreis (float): Ursprünglicher Neupreis in Euro
        kilometerstand (float): Bereits gefahrene Kilometer (Startwert: 0.0)
    """

    # ==========================================================================
    # 🎯 TEILZIEL 1 (TODO 1): Konstruktor __init__ der Basisklasse
    # Parameter: marke (str), modell (str), baujahr (int), grundpreis (float)
    # Attribute:
    #   - self.marke: str
    #   - self.modell: str
    #   - self.baujahr: int
    #   - self.grundpreis: float (als float konvertieren)
    #   - self.kilometerstand: float (Startwert: 0.0)
    # ==========================================================================
    def __init__(self, marke: str, modell: str, baujahr: int, grundpreis: float):
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 2 (TODO 2): Methode fahren(self, km: float) -> None
    # Erhöht den Kilometerstand um 'km', wenn km > 0 ist.
    # Bei km <= 0 passiert nichts.
    # ==========================================================================
    def fahren(self, km: float) -> None:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 3 (TODO 3): Methode berechne_restwert(self, aktuelles_jahr: int) -> float
    # Berechnet den aktuellen Restwert des Fahrzeugs:
    # 1. Alter = max(0, aktuelles_jahr - self.baujahr)
    # 2. Wertverlust = self.grundpreis * 0.05 * Alter (5% Wertverlust pro Jahr)
    # 3. Restwert = self.grundpreis - Wertverlust
    # 4. Mindestrestwert ist 10% des Grundpreises: max(self.grundpreis * 0.10, Restwert)
    # Rückgabe: Restwert als float
    # ==========================================================================
    def berechne_restwert(self, aktuelles_jahr: int) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 4 (TODO 4): Methode info(self) -> str
    # Gibt einen formatierten Infostring zurück:
    # Format: "{marke} {modell} ({baujahr}) - {kilometerstand:.1f} km"
    # Beispiel: "BMW 320d (2020) - 45000.0 km"
    # ==========================================================================
    def info(self) -> str:
        pass

    def __str__(self) -> str:
        return self.info()


class Auto(Fahrzeug):
    """
    Abgeleitete Klasse für PKWs (erbt von Fahrzeug).
    
    Zusätzliche Attribute:
        sitzplaetze (int): Anzahl der Sitze (Standardwert: 5)
        anzahl_tueren (int): Anzahl der Türen (Standardwert: 5)
    """

    # ==========================================================================
    # 🎯 TEILZIEL 5 (TODO 5): Konstruktor __init__ von Auto
    # Parameter: marke (str), modell (str), baujahr (int), grundpreis (float),
    #            sitzplaetze (int = 5), anzahl_tueren (int = 5)
    # 1. Rufe den Konstruktor der Elternklasse mit super().__init__(...) auf!
    # 2. Setze self.sitzplaetze und self.anzahl_tueren
    # ==========================================================================
    def __init__(
        self,
        marke: str,
        modell: str,
        baujahr: int,
        grundpreis: float,
        sitzplaetze: int = 5,
        anzahl_tueren: int = 5,
    ):
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 6 (TODO 6): Methode hupen(self) -> str
    # Gibt einen Hup-Laut mit Marke und Modell zurück:
    # Format: "Hup hup! Platz da für den {marke} {modell}!"
    # Beispiel: "Hup hup! Platz da für den VW Golf!"
    # ==========================================================================
    def hupen(self) -> str:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 7 (TODO 7): Methode info(self) -> str (Method Overriding / Erweitern)
    # Rufe super().info() auf und hänge " | {sitzplaetze} Sitze, {anzahl_tueren} Türen" an.
    # Format: "{super().info()} | {self.sitzplaetze} Sitze, {self.anzahl_tueren} Türen"
    # Beispiel: "VW Golf (2021) - 12000.0 km | 5 Sitze, 5 Türen"
    # ==========================================================================
    def info(self) -> str:
        pass


class ElektroAuto(Auto):
    """
    Abgeleitete Klasse für Elektroautos (Mehrstufige Vererbung: erbt von Auto).
    
    Zusätzliche Attribute:
        batterie_kapazitaet_kwh (float): Maximale Akkukapazität in Kilowattstunden
        batterie_ladestand_kwh (float): Aktueller Ladestand (Startwert: voll = batterie_kapazitaet_kwh)
        verbrauch_pro_100km (float): Verbrauch in kWh auf 100 km (Standardwert: 18.0)
    """

    # ==========================================================================
    # 🎯 TEILZIEL 8 (TODO 8): Konstruktor __init__ von ElektroAuto
    # Parameter: marke (str), modell (str), baujahr (int), grundpreis (float),
    #            batterie_kapazitaet_kwh (float), sitzplaetze (int = 5),
    #            anzahl_tueren (int = 5), verbrauch_pro_100km (float = 18.0)
    # 1. Rufe super().__init__(marke, modell, baujahr, grundpreis, sitzplaetze, anzahl_tueren) auf.
    # 2. Setze self.batterie_kapazitaet_kwh = float(batterie_kapazitaet_kwh)
    # 3. Setze self.batterie_ladestand_kwh = float(batterie_kapazitaet_kwh)  (Akku ist anfangs voll)
    # 4. Setze self.verbrauch_pro_100km = float(verbrauch_pro_100km)
    # ==========================================================================
    def __init__(
        self,
        marke: str,
        modell: str,
        baujahr: int,
        grundpreis: float,
        batterie_kapazitaet_kwh: float,
        sitzplaetze: int = 5,
        anzahl_tueren: int = 5,
        verbrauch_pro_100km: float = 18.0,
    ):
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 9 (TODO 9): Methode reichweite(self) -> float
    # Berechnet die verbleibende Reichweite in Kilometern:
    # Formel: (aktueller_ladestand / verbrauch_pro_100km) * 100
    # Wenn verbrauch_pro_100km <= 0: 0.0 zurückgeben.
    # ==========================================================================
    def reichweite(self) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 10 (TODO 10): Methode fahren(self, km: float) -> bool (Überschreiben mit Logik)
    # 1. Wenn km <= 0: False zurückgeben.
    # 2. Berechne den benötigten Strom: benoetigt = (km / 100.0) * self.verbrauch_pro_100km
    # 3. Wenn self.batterie_ladestand_kwh >= benoetigt:
    #       - Ziehe den Verbrauch vom Ladestand ab: self.batterie_ladestand_kwh -= benoetigt
    #       - Rufe super().fahren(km) auf (damit der Kilometerstand erhöht wird!)
    #       - return True
    # 4. Wenn der Akku NICHT reicht:
    #       - Fahre nicht (keine Änderung an Kilometerstand oder Akku)
    #       - return False
    # ==========================================================================
    def fahren(self, km: float) -> bool:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 11 (TODO 11): Methode aufladen(self, kwh: float) -> float
    # Lädt den Akku auf, aber maximal bis batterie_kapazitaet_kwh!
    # 1. Wenn kwh <= 0: return 0.0
    # 2. Berechne den freien Platz im Akku: batterie_kapazitaet_kwh - batterie_ladestand_kwh
    # 3. Tatsächlich geladene Menge = min(freier_platz, kwh)
    # 4. Erhöhe batterie_ladestand_kwh um die geladene Menge
    # 5. Gib die tatsächlich geladene Menge (float) zurück.
    # ==========================================================================
    def aufladen(self, kwh: float) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 12 (TODO 12): Methode info(self) -> str
    # Format: "{super().info()} | Akku: {batterie_ladestand_kwh:.1f}/{batterie_kapazitaet_kwh:.1f} kWh ({reichweite():.1f} km Reichweite)"
    # Beispiel: "Tesla Model 3 (2023) - 5000.0 km | 5 Sitze, 5 Türen | Akku: 60.0/60.0 kWh (333.3 km Reichweite)"
    # ==========================================================================
    def info(self) -> str:
        pass


class Lkw(Fahrzeug):
    """
    Abgeleitete Klasse für Lastkraftwagen (erbt direkt von Fahrzeug).
    
    Zusätzliche Attribute:
        max_zuladung_kg (float): Maximale Frachtkapazität in kg
        aktuelle_ladung_kg (float): Aktuell geladene Fracht (Startwert: 0.0)
    """

    # ==========================================================================
    # 🎯 TEILZIEL 13 (TODO 13): Konstruktor __init__ von Lkw
    # Parameter: marke (str), modell (str), baujahr (int), grundpreis (float),
    #            max_zuladung_kg (float)
    # 1. Rufe super().__init__(marke, modell, baujahr, grundpreis) auf.
    # 2. Setze self.max_zuladung_kg = float(max_zuladung_kg)
    # 3. Setze self.aktuelle_ladung_kg = 0.0
    # ==========================================================================
    def __init__(
        self,
        marke: str,
        modell: str,
        baujahr: int,
        grundpreis: float,
        max_zuladung_kg: float,
    ):
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 14 (TODO 14): Methode beladen(self, kg: float) -> bool
    # 1. Wenn kg > 0 und self.aktuelle_ladung_kg + kg <= self.max_zuladung_kg:
    #       - Erhöhe self.aktuelle_ladung_kg um kg
    #       - return True
    # 2. Sonst (Überladung oder ungültiges Gewicht): return False
    # ==========================================================================
    def beladen(self, kg: float) -> bool:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 15 (TODO 15): Methode entladen(self, kg: float) -> float
    # Entlädt maximal die vorhandene Ladung.
    # 1. Wenn kg <= 0: return 0.0
    # 2. tatsaechlich = min(self.aktuelle_ladung_kg, kg)
    # 3. self.aktuelle_ladung_kg -= tatsaechlich
    # 4. return tatsaechlich
    # ==========================================================================
    def entladen(self, kg: float) -> float:
        pass

    # ==========================================================================
    # 🎯 TEILZIEL 16 (TODO 16): Methode info(self) -> str
    # Format: "{super().info()} | Ladung: {aktuelle_ladung_kg:.1f}/{max_zuladung_kg:.1f} kg"
    # Beispiel: "MAN TGX (2019) - 150000.0 km | Ladung: 8500.0/18000.0 kg"
    # ==========================================================================
    def info(self) -> str:
        pass


# ==============================================================================
# Terminal-Test zum Ausprobieren: (python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("--- 🚗 Auto testen ---")
    golf = Auto("VW", "Golf 8", 2021, 28000.0, sitzplaetze=5, anzahl_tueren=5)
    golf.fahren(150.0)
    print(golf.info())
    print(golf.hupen())
    print(f"Restwert im Jahr 2026: {golf.berechne_restwert(2026):.2f} €")

    print("\n--- ⚡ ElektroAuto testen ---")
    tesla = ElektroAuto("Tesla", "Model Y", 2023, 45000.0, batterie_kapazitaet_kwh=75.0, verbrauch_pro_100km=16.5)
    print(tesla.info())
    print(f"Start-Reichweite: {tesla.reichweite():.1f} km")
    
    erfolg = tesla.fahren(200.0)
    print(f"Fahrt 200 km erfolgreich? {erfolg}")
    print(tesla.info())
    
    geladen = tesla.aufladen(50.0)
    print(f"Aufgeladen: {geladen:.1f} kWh")
    print(tesla.info())

    print("\n--- 🚛 LKW testen ---")
    lkw = Lkw("Mercedes-Benz", "Actros", 2020, 110000.0, max_zuladung_kg=24000.0)
    lkw.beladen(15000.0)
    lkw.fahren(400.0)
    print(lkw.info())
    entladen = lkw.entladen(5000.0)
    print(f"Entladen: {entladen:.1f} kg -> Neue Ladung: {lkw.aktuelle_ladung_kg:.1f} kg")
