"""
Kapitel G07: Listen & Sequenzen in Python (Schulabgleich 09.0 & 11.0)
====================================================================

In dieser Aufgabe vertiefst du dein Wissen über Python-Listen, Indexierung,
Slicing, Listen-Methoden und nützliche eingebaute Funktionen.
"""


def liste_umdrehen(liste: list) -> list:
    """
    TODO 1: Gibt eine NEUE Liste zurück, deren Elemente in umgekehrter
    Reihenfolge angeordnet sind. Die Original-Liste darf nicht verändert werden!

    Beispiel:
        liste_umdrehen([1, 2, 3, 4]) -> [4, 3, 2, 1]
        liste_umdrehen(["A", "B", "C"]) -> ["C", "B", "A"]

    Tipp:
        Verwende Slicing mit Schrittweite -1: `liste[::-1]`
        oder erstelle eine Kopie und wende `.reverse()` an.
    """
    # 🎯 TEILZIEL 1: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


def filtere_positive_zahlen(zahlen: list[float]) -> list[float]:
    """
    TODO 2: Gibt eine neue Liste zurück, die nur die echten positiven Zahlen
    (Zahl > 0) aus der übergebenen Liste enthält. 0 und negative Zahlen werden ignoriert.

    Beispiel:
        filtere_positive_zahlen([-3, 5, 0, 12, -1, 8.5]) -> [5, 12, 8.5]

    Tipp:
        Erstelle eine leere Ergebnisliste `positiv = []` und iteriere mit einer
        for-Schleife über alle Zahlen. Wenn `z > 0`, füge sie mit `.append(z)` hinzu.
    """
    # 🎯 TEILZIEL 2: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


def entferne_element(liste: list, element) -> bool:
    """
    TODO 3: Entfernt das erste Vorkommen von 'element' aus der übergebenen 'liste'.
    - Wenn das Element in der Liste vorkommt: Entferne es und gib True zurück.
    - Wenn das Element NICHT in der Liste ist: Ändere die Liste nicht und gib False zurück.

    WICHTIG: Die Funktion darf keinen Fehler (ValueError) werfen!

    Beispiel:
        namen = ["Anna", "Ben", "Clara"]
        entferne_element(namen, "Ben") -> True  (namen ist jetzt ["Anna", "Clara"])
        entferne_element(namen, "David") -> False (namen bleibt ["Anna", "Clara"])

    Tipp:
        Prüfe zuerst mit `if element in liste:`, bevor du `liste.remove(element)` aufrufst.
    """
    # 🎯 TEILZIEL 3: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


def mittlere_elemente(liste: list) -> list:
    """
    TODO 4: Gibt einen Teil der Liste zurück, der weder das erste (Index 0)
    noch das letzte (Index -1) Element enthält.
    - Wenn die Liste 2 oder weniger Elemente hat, gib eine leere Liste [] zurück.

    Beispiel:
        mittlere_elemente([10, 20, 30, 40, 50]) -> [20, 30, 40]
        mittlere_elemente(["Start", "Mitte", "Ende"]) -> ["Mitte"]
        mittlere_elemente([1, 2]) -> []
        mittlere_elemente([]) -> []

    Tipp:
        Nutze Slicing: `liste[1:-1]`. Wenn `len(liste) <= 2`, gib `[]` zurück.
    """
    # 🎯 TEILZIEL 4: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


def noten_durchschnitt_ohne_ausreisser(noten: list[float]) -> float:
    """
    TODO 5: Berechnet den Notendurchschnitt, nachdem die beste (niedrigste Zahl)
    und die schlechteste Note (höchste Zahl) entfernt wurden.
    - Bei weniger als 3 Noten kann kein sinnvoller bereinigter Schnitt berechnet werden;
      gib in diesem Fall 0.0 zurück.
    - Die übergebene Liste 'noten' darf nicht dauerhaft verändert werden!

    Beispiel:
        noten_durchschnitt_ohne_ausreisser([1.0, 2.0, 3.0, 4.0, 5.0])
        -> Beste Note: 1.0, Schlechteste Note: 5.0 werden entfernt.
        -> Verbleibende Noten: [2.0, 3.0, 4.0]
        -> Durchschnitt: (2.0 + 3.0 + 4.0) / 3 = 3.0

    Tipp:
        1. Wenn `len(noten) < 3`: `return 0.0`
        2. Erstelle eine Kopie der Liste: `kopie = list(noten)`
        3. Finde Minimum mit `min(kopie)` und Maximum mit `max(kopie)`.
        4. Entferne je ein Exemplar mit `kopie.remove(...)`.
        5. Berechne den Schnitt mit `sum(kopie) / len(kopie)` und gib ihn zurück.
    """
    # 🎯 TEILZIEL 5: Implementiere die Logik Schritt für Schritt:
    # 💡 Tipp: Beachte Datentypen und das abschließende return!
    pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# (Führe die Datei aus mit: python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("--- Teste deine Listen-Funktionen ---")

    test_liste = [10, 20, 30, 40, 50]
    print("Original:", test_liste)
    print("Umgedreht (TODO 1):", liste_umdrehen(test_liste))

    zahlen = [-5, 12, 0, -3, 42, 7]
    print("Positive Zahlen (TODO 2):", filtere_positive_zahlen(zahlen))

    tiere = ["Hund", "Katze", "Maus"]
    erfolg = entferne_element(tiere, "Katze")
    print(f"Katze entfernt (TODO 3)? {erfolg} -> Rest: {tiere}")
    erfolg_fehlt = entferne_element(tiere, "Elefant")
    print(f"Elefant entfernt (TODO 3)? {erfolg_fehlt} -> Rest: {tiere}")

    print("Mittlere Elemente von [1, 2, 3, 4, 5] (TODO 4):", mittlere_elemente([1, 2, 3, 4, 5]))

    noten = [1.0, 2.0, 3.0, 4.0, 5.0]
    schnitt = noten_durchschnitt_ohne_ausreisser(noten)
    print(f"Bereinigter Notenschnitt von {noten} (TODO 5): {schnitt}")
