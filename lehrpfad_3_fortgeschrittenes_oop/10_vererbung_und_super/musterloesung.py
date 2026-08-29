"""
Kapitel 10: Vererbung & super() – Musterlösung 🧬🚗
===================================================
Schulabgleich: 25.0 Vererbung
"""

from typing import List, Optional


class Fahrzeug:
    """Basisklasse für alle Fahrzeuge."""

    def __init__(self, marke: str, modell: str, baujahr: int, grundpreis: float):
        self.marke: str = marke
        self.modell: str = modell
        self.baujahr: int = int(baujahr)
        self.grundpreis: float = float(grundpreis)
        self.kilometerstand: float = 0.0

    def fahren(self, km: float) -> None:
        if km > 0:
            self.kilometerstand += float(km)

    def berechne_restwert(self, aktuelles_jahr: int) -> float:
        alter = max(0, aktuelles_jahr - self.baujahr)
        wertverlust = self.grundpreis * 0.05 * alter
        restwert = self.grundpreis - wertverlust
        return max(self.grundpreis * 0.10, restwert)

    def info(self) -> str:
        return f"{self.marke} {self.modell} ({self.baujahr}) - {self.kilometerstand:.1f} km"

    def __str__(self) -> str:
        return self.info()


class Auto(Fahrzeug):
    """Abgeleitete Klasse für PKWs (erbt von Fahrzeug)."""

    def __init__(
        self,
        marke: str,
        modell: str,
        baujahr: int,
        grundpreis: float,
        sitzplaetze: int = 5,
        anzahl_tueren: int = 5,
    ):
        super().__init__(marke, modell, baujahr, grundpreis)
        self.sitzplaetze: int = int(sitzplaetze)
        self.anzahl_tueren: int = int(anzahl_tueren)

    def hupen(self) -> str:
        return f"Hup hup! Platz da für den {self.marke} {self.modell}!"

    def info(self) -> str:
        return f"{super().info()} | {self.sitzplaetze} Sitze, {self.anzahl_tueren} Türen"


class ElektroAuto(Auto):
    """Abgeleitete Klasse für Elektroautos (erbt von Auto)."""

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
        super().__init__(marke, modell, baujahr, grundpreis, sitzplaetze, anzahl_tueren)
        self.batterie_kapazitaet_kwh: float = float(batterie_kapazitaet_kwh)
        self.batterie_ladestand_kwh: float = float(batterie_kapazitaet_kwh)
        self.verbrauch_pro_100km: float = float(verbrauch_pro_100km)

    def reichweite(self) -> float:
        if self.verbrauch_pro_100km <= 0:
            return 0.0
        return (self.batterie_ladestand_kwh / self.verbrauch_pro_100km) * 100.0

    def fahren(self, km: float) -> bool:
        if km <= 0:
            return False
        benoetigt = (km / 100.0) * self.verbrauch_pro_100km
        if self.batterie_ladestand_kwh >= benoetigt:
            self.batterie_ladestand_kwh -= benoetigt
            super().fahren(km)
            return True
        return False

    def aufladen(self, kwh: float) -> float:
        if kwh <= 0:
            return 0.0
        freier_platz = self.batterie_kapazitaet_kwh - self.batterie_ladestand_kwh
        tatsaechlich = min(freier_platz, float(kwh))
        self.batterie_ladestand_kwh += tatsaechlich
        return tatsaechlich

    def info(self) -> str:
        return (
            f"{super().info()} | Akku: {self.batterie_ladestand_kwh:.1f}/"
            f"{self.batterie_kapazitaet_kwh:.1f} kWh ({self.reichweite():.1f} km Reichweite)"
        )


class Lkw(Fahrzeug):
    """Abgeleitete Klasse für Lastkraftwagen (erbt von Fahrzeug)."""

    def __init__(
        self,
        marke: str,
        modell: str,
        baujahr: int,
        grundpreis: float,
        max_zuladung_kg: float,
    ):
        super().__init__(marke, modell, baujahr, grundpreis)
        self.max_zuladung_kg: float = float(max_zuladung_kg)
        self.aktuelle_ladung_kg: float = 0.0

    def beladen(self, kg: float) -> bool:
        if kg > 0 and (self.aktuelle_ladung_kg + kg <= self.max_zuladung_kg):
            self.aktuelle_ladung_kg += float(kg)
            return True
        return False

    def entladen(self, kg: float) -> float:
        if kg <= 0:
            return 0.0
        tatsaechlich = min(self.aktuelle_ladung_kg, float(kg))
        self.aktuelle_ladung_kg -= tatsaechlich
        return tatsaechlich

    def info(self) -> str:
        return f"{super().info()} | Ladung: {self.aktuelle_ladung_kg:.1f}/{self.max_zuladung_kg:.1f} kg"


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
