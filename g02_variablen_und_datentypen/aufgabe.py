"""
Grundlagen 02: Variablen & Datentypen – Aufgabenblatt
======================================================

In diesem Kapitel lernst du, wie Variablen als benannte Speicherboxen
funktionieren, welche 4 Basisdatentypen Python besitzt und wie du Typen
umwandelst (Type Casting).

Bearbeite die Aufgaben Schritt für Schritt von TODO 1 bis TODO 4.
Wenn du fertig bist, überprüfe deine Lösung im Terminal mit:
    python3 test_aufgabe.py
"""

# ==============================================================================
# TODO 1: Schreibe die Funktion 'bestimme_typ_name(wert)'
#
# Die Funktion bekommt einen beliebigen Wert übergeben und soll als String
# den deutschen Namen des Datentyps zurückgeben:
#   - Wenn 'wert' ein bool ist (True/False):    -> "Wahrheitswert"
#   - Wenn 'wert' ein int ist (z.B. 42):         -> "Ganzzahl"
#   - Wenn 'wert' ein float ist (z.B. 3.14):     -> "Kommazahl"
#   - Wenn 'wert' ein str ist (z.B. "Hallo"):    -> "Text"
#   - Bei allen anderen Typen:                  -> "Unbekannt"
#
# WICHTIGER HINWEIS:
# In Python ist 'bool' eine Unterklasse von 'int' (isinstance(True, int) ist True!).
# Prüfe daher 'bool' ZUERST vor 'int' oder verwende 'type(wert) is bool'!
#
# Beispiele:
#   bestimme_typ_name(42)       -> "Ganzzahl"
#   bestimme_typ_name(3.14)     -> "Kommazahl"
#   bestimme_typ_name("Python") -> "Text"
#   bestimme_typ_name(True)     -> "Wahrheitswert"
# ==============================================================================

def bestimme_typ_name(wert) -> str:
    # Schreibe hier deinen Code für TODO 1:
    pass


# ==============================================================================
# TODO 2: Schreibe die Funktion 'summe_aus_texten(text_a, text_b)'
#
# Oft kommen Benutzereingaben (z.B. von input()) als Text (str) an.
# Wenn man "10" + "20" rechnet, entsteht fälschlicherweise "1020" (Textverkettung).
#
# Deine Aufgabe:
# Wandle beide Parameter 'text_a' und 'text_b' mit 'int()' in echte Ganzzahlen um,
# addiere sie mathematisch und gib das Ergebnis (als int) zurück!
#
# Beispiele:
#   summe_aus_texten("10", "20") -> 30  (nicht "1020"!)
#   summe_aus_texten("5", "7")   -> 12
# ==============================================================================

def summe_aus_texten(text_a: str, text_b: str) -> int:
    # Schreibe hier deinen Code für TODO 2:
    pass


# ==============================================================================
# TODO 3: Schreibe die Funktion 'formatiere_preis(preis_float)'
#
# Die Funktion bekommt einen Preis als float (Kommazahl) übergeben und soll
# einen formatierten String mit genau 2 Nachkommastellen und dem Euro-Zeichen '€'
# zurückgeben.
#
# Format: "{preis:.2f} €"
#
# Beispiele:
#   formatiere_preis(19.99) -> "19.99 €"
#   formatiere_preis(5.0)   -> "5.00 €"
#   formatiere_preis(0.0)   -> "0.00 €"
# ==============================================================================

def formatiere_preis(preis_float: float) -> str:
    # Schreibe hier deinen Code für TODO 3:
    pass


# ==============================================================================
# TODO 4: Schreibe die Funktion 'ist_volljaehrig(alter)'
#
# Die Funktion bekommt ein Alter als Ganzzahl übergeben.
# Sie soll 'True' zurückgeben, wenn 'alter' größer oder gleich 18 ist,
# andernfalls 'False'.
#
# Tipp:
# Ein Vergleichsoperator wie 'alter >= 18' liefert bereits direkt einen bool!
#
# Beispiele:
#   ist_volljaehrig(18) -> True
#   ist_volljaehrig(21) -> True
#   ist_volljaehrig(17) -> False
# ==============================================================================

def ist_volljaehrig(alter: int) -> bool:
    # Schreibe hier deinen Code für TODO 4:
    pass


# ==============================================================================
# Hauptprogramm zum Ausprobieren:
# (Führe diese Datei direkt aus mit: python3 aufgabe.py)
# ==============================================================================
if __name__ == "__main__":
    print("=" * 55)
    print("📦 VARIABLEN & DATENTYPEN – TEST-AUSGABE")
    print("=" * 55)

    print("Typ von 42:          ", bestimme_typ_name(42))
    print("Typ von 3.14:        ", bestimme_typ_name(3.14))
    print("Typ von 'Hallo':     ", bestimme_typ_name("Hallo"))
    print("Typ von True:        ", bestimme_typ_name(True))

    print("\nSumme aus '10' + '20':", summe_aus_texten("10", "20"))
    print("Preis formatiert (19.9):", formatiere_preis(19.9))
    print("Ist 17 volljährig?   ", ist_volljaehrig(17))
    print("Ist 18 volljährig?   ", ist_volljaehrig(18))

    print("\n💡 Führe 'python3 test_aufgabe.py' aus, um deine Lösungen zu prüfen!")
