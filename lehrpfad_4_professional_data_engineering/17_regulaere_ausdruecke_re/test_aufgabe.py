import unittest
import sys
from pathlib import Path

# Sicherstellen, dass das aktuelle Verzeichnis im Python-Pfad liegt
sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel17(unittest.TestCase):
    """
    Testsuite für Kapitel 17: Reguläre Ausdrücke (re) – Text-Mining & Validierung.
    """

    def setUp(self):
        self.ist_gueltige_email = getattr(aufgabe, "ist_gueltige_email", None)
        self.finde_telefonnummern = getattr(aufgabe, "finde_telefonnummern", None)
        self.extrahiere_hashtags = getattr(aufgabe, "extrahiere_hashtags", None)
        self.maskiere_iban = getattr(aufgabe, "maskiere_iban", None)
        self.parse_datum_iso = getattr(aufgabe, "parse_datum_iso", None)
        self.parse_log_zeile = getattr(aufgabe, "parse_log_zeile", None)

        self.assertIsNotNone(self.ist_gueltige_email, "Funktion 'ist_gueltige_email' nicht gefunden!")
        self.assertIsNotNone(self.finde_telefonnummern, "Funktion 'finde_telefonnummern' nicht gefunden!")
        self.assertIsNotNone(self.extrahiere_hashtags, "Funktion 'extrahiere_hashtags' nicht gefunden!")
        self.assertIsNotNone(self.maskiere_iban, "Funktion 'maskiere_iban' nicht gefunden!")
        self.assertIsNotNone(self.parse_datum_iso, "Funktion 'parse_datum_iso' nicht gefunden!")

    # ==========================================================================
    # 1. E-Mail Validierung
    # ==========================================================================
    def test_01_ist_gueltige_email(self):
        """Prüft E-Mail Validierung für Standard- und Grenzfälle."""
        # Gültige E-Mails
        gueltige = [
            "max.mustermann@schule.at",
            "anna_meier@firma.de",
            "dev_123+tag@gmail.com",
            "info@sub.domain.org",
            "contact@company.co.uk",
            "a@b.at",
            "test-user@domain.io"
        ]
        for mail in gueltige:
            self.assertTrue(self.ist_gueltige_email(mail), f"'{mail}' sollte als GÜLTIG erkannt werden!")

        # Ungültige E-Mails
        ungueltige = [
            "kein_at_zeichen.de",
            "@domain.com",
            "name@.com",
            "name@domain",
            "name@domain.c",         # TLD zu kurz (mind. 2 Zeichen)
            "name @domain.com",       # Leerzeichen im Benutzernamen
            "name@ domain.com",       # Leerzeichen in der Domain
            "name@domain .com",       # Leerzeichen vor TLD
            "name@@domain.com",       # Doppeltes @
            "",                       # Leerer String
            "name@domain..com"        # Doppelte Punkte
        ]
        for mail in ungueltige:
            self.assertFalse(self.ist_gueltige_email(mail), f"'{mail}' sollte als UNGÜLTIG erkannt werden!")

    # ==========================================================================
    # 2. Telefonnummern-Extraktion
    # ==========================================================================
    def test_02_finde_telefonnummern(self):
        """Prüft das Extrahieren von Telefonnummern in verschiedenen Formaten."""
        text = (
            "Hier sind unsere Kontakte: Büro 0171-1234567 oder Zentrale +49 171 1234567. "
            "In Österreich erreichst du uns unter +43 664 1234567. "
            "München: (089) 123456 und Berlin: 030/98765432. "
            "Keine Telefonnummer ist 123 oder das Jahr 2026."
        )
        gefunden = self.finde_telefonnummern(text)
        
        # Sollte alle 5 Telefonnummern finden
        self.assertIn("0171-1234567", gefunden)
        self.assertIn("+49 171 1234567", gefunden)
        self.assertIn("+43 664 1234567", gefunden)
        self.assertIn("(089) 123456", gefunden)
        self.assertIn("030/98765432", gefunden)
        
        # Grenzfall: Text ohne Nummern
        self.assertEqual(self.finde_telefonnummern("Hier gibt es keine Nummern!"), [])
        self.assertEqual(self.finde_telefonnummern(""), [])

    # ==========================================================================
    # 3. Hashtag-Extraktion
    # ==========================================================================
    def test_03_extrahiere_hashtags(self):
        """Prüft das Extrahieren von Hashtags inkl. Umlauten und Zahlen."""
        tweet = "Heute lernen wir #python und #data_engineering! Macht super #spaß und ist #süß. #2026 #AI_pro"
        hashtags = self.extrahiere_hashtags(tweet)
        
        erwartet = ["#python", "#data_engineering", "#spaß", "#süß", "#2026", "#AI_pro"]
        self.assertEqual(hashtags, erwartet)

        # Einzelne Rauten oder Rauten ohne Wortzeichen dürfen nicht matchen
        self.assertEqual(self.extrahiere_hashtags("Nur ein # oder #! oder #+#"), [])
        self.assertEqual(self.extrahiere_hashtags("Keine Hashtags vorhanden."), [])
        self.assertEqual(self.extrahiere_hashtags(""), [])

    # ==========================================================================
    # 4. IBAN-Maskierung
    # ==========================================================================
    def test_04_maskiere_iban(self):
        """Prüft die datenschutzkonforme Maskierung von IBANs."""
        # Deutsche IBAN (22 Zeichen -> 4 sichtbar + 18 Sternchen)
        text1 = "Konto: DE89370400440532013000 bitte prüfen."
        ergebnis1 = self.maskiere_iban(text1)
        self.assertEqual(ergebnis1, "Konto: DE89****************** bitte prüfen.")

        # Mehrere IBANs in einem Text
        text2 = "Überweise von AT611904300234573201 an DE1234567890 sofort."
        ergebnis2 = self.maskiere_iban(text2)
        # AT IBAN (20 Zeichen -> 4 sichtbar + 16 Sternchen)
        # DE IBAN (12 Zeichen -> 4 sichtbar + 8 Sternchen)
        self.assertEqual(ergebnis2, "Überweise von AT61**************** an DE12******** sofort.")

        # Text ohne IBAN bleibt unberührt
        text3 = "Keine Bankdaten hier vorhanden."
        self.assertEqual(self.maskiere_iban(text3), text3)
        self.assertEqual(self.maskiere_iban(""), "")

    # ==========================================================================
    # 5. ISO-Datum Parsing mit benannten Gruppen
    # ==========================================================================
    def test_05_parse_datum_iso(self):
        """Prüft das Parsen von ISO-Datumsstrings in ein Dict mit benannten Gruppen."""
        res1 = self.parse_datum_iso("2026-08-29")
        self.assertEqual(res1, {"jahr": "2026", "monat": "08", "tag": "29"})

        res2 = self.parse_datum_iso("1999-12-31")
        self.assertEqual(res2, {"jahr": "1999", "monat": "12", "tag": "31"})

        # Ungültige Formate müssen ValueError werfen
        with self.assertRaises(ValueError, msg="Deutsches Datumsformat muss ValueError auslösen!"):
            self.parse_datum_iso("29.08.2026")

        with self.assertRaises(ValueError, msg="Slash-Format muss ValueError auslösen!"):
            self.parse_datum_iso("2026/08/29")

        with self.assertRaises(ValueError, msg="Kurzes Jahr muss ValueError auslösen!"):
            self.parse_datum_iso("26-08-29")

        with self.assertRaises(ValueError, msg="Leerer String muss ValueError auslösen!"):
            self.parse_datum_iso("")

    # ==========================================================================
    # 6. Bonus: Logfile Parser
    # ==========================================================================
    def test_06_parse_log_zeile(self):
        """Prüft das Parsen von Server-Logzeilen (Bonus-Funktion)."""
        if self.parse_log_zeile is None:
            return  # Überspringen, falls Bonus nicht implementiert

        zeile = "[2026-08-29 14:32:00] [ERROR] [auth_service] Login fehlgeschlagen für user 'admin'"
        try:
            res = self.parse_log_zeile(zeile)
            if res is not None:
                self.assertEqual(res.get("timestamp"), "2026-08-29 14:32:00")
                self.assertEqual(res.get("level"), "ERROR")
                self.assertEqual(res.get("service"), "auth_service")
                self.assertEqual(res.get("message"), "Login fehlgeschlagen für user 'admin'")

                # Ungültige Zeile
                with self.assertRaises(ValueError):
                    self.parse_log_zeile("Keine gültige Logzeile")
        except NotImplementedError:
            pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
