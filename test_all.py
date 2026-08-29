#!/usr/bin/env python3
"""
🧪 Gesamttest-Runner für alle Kapitel
===================================
Führe dieses Skript aus, um zu sehen, welche Kapitel du bereits erfolgreich gelöst hast:
    python3 test_all.py
"""

import sys
import unittest
from pathlib import Path

KAPITEL = [
    ("Kapitel 00: Python-Fehlersuche (Warm-up)", "00_fehlersuche_und_grundlagen"),
    ("Kapitel 01: Einstieg in Klassen", "01_einstieg_klassen"),
    ("Kapitel 02: Konstruktor & self", "02_init_und_self"),
    ("Kapitel 03: Methoden & Verhalten", "03_methoden_und_verhalten"),
    ("Kapitel 04: __str__ & Darstellung", "04_str_und_darstellung"),
    ("Kapitel 05: Objekte kombinieren", "05_objekte_kombinieren"),
    ("Kapitel 06: Abschlussprojekt Tamagotchi", "06_abschlussprojekt_tamagotchi"),
    ("Kapitel 07: Referenzen & Stammbäume", "07_referenzen_und_speicher"),
    ("Kapitel 08: Operator Overloading & Dunder", "08_operator_overloading_dunder"),
    ("Kapitel 09: Eigene Unit Tests & TDD", "09_eigene_unit_tests_schreiben"),
    ("Kapitel 10: Vererbung & super()", "10_vererbung_und_super"),
    ("Kapitel 11: Polymorphie & Interfaces", "11_polymorphie_und_interfaces"),
    ("Kapitel 12: Exceptions & Fehlerbehandlung", "12_exceptions_und_fehlerbehandlung"),
    ("Kapitel 13: Persistenz (JSON & CSV)", "13_persistenz_json_und_csv"),
    ("Kapitel 14: Desktop-GUIs mit Tkinter", "14_gui_mit_tkinter"),
]

def main():
    root = Path(__file__).parent.resolve()
    print("=" * 65)
    print("🎓 PYTHON OOP ÜBUNGSREIHE – GESAMTFORTSCHRITT")
    print("=" * 65)
    
    gesamt_bestanden = 0
    
    for titel, ordner in KAPITEL:
        kapitel_pfad = root / ordner
        if not kapitel_pfad.exists():
            continue
            
        sys.path.insert(0, str(kapitel_pfad))
        
        # Testsuite laden
        loader = unittest.TestLoader()
        suite = loader.discover(str(kapitel_pfad), pattern="test_aufgabe.py")
        
        # Leisen Runner ausführen
        runner = unittest.TextTestRunner(stream=open("/dev/null", "w"), verbosity=0)
        result = runner.run(suite)
        
        # Module für saubere Isolation entfernen
        if str(kapitel_pfad) in sys.path:
            sys.path.remove(str(kapitel_pfad))
        for m in list(sys.modules.keys()):
            if m in ("aufgabe", "test_aufgabe", "musterloesung"):
                del sys.modules[m]

        anzahl_tests = result.testsRun
        erfolgreich = result.wasSuccessful() and anzahl_tests > 0

        if erfolgreich:
            print(f"  ✅ {titel:45s} ({anzahl_tests}/{anzahl_tests} Tests OK)")
            gesamt_bestanden += 1
        else:
            fehlgeschlagen = len(result.failures) + len(result.errors)
            print(f"  ⏳ {titel:45s} (Noch offen / {fehlgeschlagen} Fehler)")

    print("=" * 65)
    print(f"Ergebnis: {gesamt_bestanden} von {len(KAPITEL)} Kapiteln vollständig gelöst!")
    if gesamt_bestanden == len(KAPITEL):
        print("🏆 PERFEKT! Du hast alle Aufgaben mit Bravour gemeistert! 🎉")
    else:
        print("💡 Öffne das nächste offene Kapitel und starte mit aufgabe.py!")
    print("=" * 65)


if __name__ == "__main__":
    main()
