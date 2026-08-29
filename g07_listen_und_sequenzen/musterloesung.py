"""
Kapitel G07: Listen & Sequenzen – Musterlösung
===============================================
"""


def liste_umdrehen(liste: list) -> list:
    """Gibt eine neue umgedrehte Liste zurück."""
    return liste[::-1]


def filtere_positive_zahlen(zahlen: list[float]) -> list[float]:
    """Filtert alle Zahlen > 0 heraus."""
    return [z for z in zahlen if z > 0]


def entferne_element(liste: list, element) -> bool:
    """Entfernt ein Element sicher, falls es existiert."""
    if element in liste:
        liste.remove(element)
        return True
    return False


def mittlere_elemente(liste: list) -> list:
    """Gibt alle Elemente ohne erstes und letztes Element zurück."""
    if len(liste) <= 2:
        return []
    return liste[1:-1]


def noten_durchschnitt_ohne_ausreisser(noten: list[float]) -> float:
    """Entfernt Minimum und Maximum und berechnet den arithmetischen Mittelwert."""
    if len(noten) < 3:
        return 0.0
    kopie = list(noten)
    kopie.remove(min(kopie))
    kopie.remove(max(kopie))
    return sum(kopie) / len(kopie)


if __name__ == "__main__":
    test_liste = [10, 20, 30, 40, 50]
    print("Original:", test_liste)
    print("Umgedreht:", liste_umdrehen(test_liste))

    zahlen = [-5, 12, 0, -3, 42, 7]
    print("Positive Zahlen:", filtere_positive_zahlen(zahlen))

    tiere = ["Hund", "Katze", "Maus"]
    erfolg = entferne_element(tiere, "Katze")
    print(f"Katze entfernt? {erfolg} -> Rest: {tiere}")

    print("Mittlere Elemente:", mittlere_elemente([1, 2, 3, 4, 5]))

    noten = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(f"Notenschnitt ohne Ausreißer von {noten}: {noten_durchschnitt_ohne_ausreisser(noten)}")
