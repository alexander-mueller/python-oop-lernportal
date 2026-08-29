import io
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import aufgabe
except ImportError as e:
    raise ImportError(f"Konnte 'aufgabe.py' nicht importieren: {e}")


class TestKapitel09Meta(unittest.TestCase):
    """
    Metatest-Suite: Prüft, ob die Schülerin saubere, wirksame Unit Tests geschrieben hat.
    """

    def setUp(self):
        self.TestTaschenrechner = getattr(aufgabe, "TestTaschenrechner", None)
        self.TestBankkonto = getattr(aufgabe, "TestBankkonto", None)
        self.assertIsNotNone(self.TestTaschenrechner, "Klasse 'TestTaschenrechner' nicht in aufgabe.py gefunden!")
        self.assertIsNotNone(self.TestBankkonto, "Klasse 'TestBankkonto' nicht in aufgabe.py gefunden!")
        self.assertTrue(issubclass(self.TestTaschenrechner, unittest.TestCase))
        self.assertTrue(issubclass(self.TestBankkonto, unittest.TestCase))

    def _run_test_case(self, test_class, test_method_name):
        """Hilfsfunktion: Führt eine einzelne Testmethode aus und gibt das TestResult zurück."""
        suite = unittest.TestSuite()
        suite.addTest(test_class(test_method_name))
        stream = io.StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=0)
        return runner.run(suite)

    def test_01_alle_testmethoden_vorhanden(self):
        """Prüft, ob alle 8 geforderten Testmethoden existieren."""
        erwartete_calc_tests = [
            "test_01_grundrechenarten",
            "test_02_division_und_kommazahlen",
            "test_03_division_durch_null_exception",
            "test_04_wurzel_negativ_exception",
            "test_05_speicher_funktionen",
        ]
        for name in erwartete_calc_tests:
            self.assertTrue(
                hasattr(self.TestTaschenrechner, name),
                f"Methode '{name}' fehlt in TestTaschenrechner!"
            )

        erwartete_konto_tests = [
            "test_06_einzahlen_und_abheben",
            "test_07_abheben_ueber_limit_exception",
            "test_08_ueberweisung",
        ]
        for name in erwartete_konto_tests:
            self.assertTrue(
                hasattr(self.TestBankkonto, name),
                f"Methode '{name}' fehlt in TestBankkonto!"
            )

    def test_02_tests_bestehen_auf_korrektem_code(self):
        """Prüft, ob alle Tests auf dem korrekten Code erfolgreich durchlaufen."""
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        suite.addTests(loader.loadTestsFromTestCase(self.TestTaschenrechner))
        suite.addTests(loader.loadTestsFromTestCase(self.TestBankkonto))

        stream = io.StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=0)
        result = runner.run(suite)

        self.assertGreaterEqual(result.testsRun, 8, "Es müssen mindestens 8 Tests ausgeführt werden!")
        self.assertEqual(
            len(result.failures), 0,
            f"Deine Tests sind auf korrektem Code fehlgeschlagen:\n{stream.getvalue()}"
        )
        self.assertEqual(
            len(result.errors), 0,
            f"Deine Tests haben Fehler/Abstürze verursacht:\n{stream.getvalue()}"
        )

    def test_03_entlarvt_rechenfehler(self):
        """Mutationstest: Prüft, ob test_01 fehlerhafte Addition entlarvt."""
        OriginalCalc = aufgabe.Taschenrechner
        class BuggyCalc(OriginalCalc):
            def add(self, a, b):
                return a + b + 99  # Absichtlicher Bug

        try:
            aufgabe.Taschenrechner = BuggyCalc
            result = self._run_test_case(self.TestTaschenrechner, "test_01_grundrechenarten")
            self.assertFalse(
                result.wasSuccessful(),
                "test_01_grundrechenarten muss fehlschlagen, wenn add() ein falsches Ergebnis liefert! Hast du self.assertEqual verwendet?"
            )
        finally:
            aufgabe.Taschenrechner = OriginalCalc

    def test_04_entlarvt_fehlende_nulldivision_exception(self):
        """Mutationstest: Prüft, ob test_03 fehlende ZeroDivisionError Exception entlarvt."""
        OriginalCalc = aufgabe.Taschenrechner
        class BuggyCalc(OriginalCalc):
            def div(self, a, b):
                if b == 0:
                    return 0.0  # Fehler: Wirft KEINE Exception
                return a / b

        try:
            aufgabe.Taschenrechner = BuggyCalc
            result = self._run_test_case(self.TestTaschenrechner, "test_03_division_durch_null_exception")
            self.assertFalse(
                result.wasSuccessful(),
                "test_03_division_durch_null_exception muss fehlschlagen, wenn div(10, 0) keine Exception wirft! Nutze 'with self.assertRaises(ZeroDivisionError):'."
            )
        finally:
            aufgabe.Taschenrechner = OriginalCalc

    def test_05_entlarvt_fehlende_wurzel_exception(self):
        """Mutationstest: Prüft, ob test_04 fehlende ValueError Exception entlarvt."""
        OriginalCalc = aufgabe.Taschenrechner
        class BuggyCalc(OriginalCalc):
            def wurzel(self, a):
                if a < 0:
                    return 0.0  # Fehler: Wirft KEINE Exception
                return super().wurzel(a)

        try:
            aufgabe.Taschenrechner = BuggyCalc
            result = self._run_test_case(self.TestTaschenrechner, "test_04_wurzel_negativ_exception")
            self.assertFalse(
                result.wasSuccessful(),
                "test_04_wurzel_negativ_exception muss fehlschlagen, wenn wurzel(-9) keinen ValueError wirft!"
            )
        finally:
            aufgabe.Taschenrechner = OriginalCalc

    def test_06_entlarvt_fehlende_ueberziehung_exception(self):
        """Mutationstest: Prüft, ob test_07 unbefugte Überziehung entlarvt."""
        OriginalKonto = aufgabe.Bankkonto
        class BuggyKonto(OriginalKonto):
            def abheben(self, betrag):
                # Fehler: Erlaubt Überziehung ohne ValueError
                self.kontostand -= betrag

        try:
            aufgabe.Bankkonto = BuggyKonto
            result = self._run_test_case(self.TestBankkonto, "test_07_abheben_ueber_limit_exception")
            self.assertFalse(
                result.wasSuccessful(),
                "test_07_abheben_ueber_limit_exception muss fehlschlagen, wenn abheben() ohne Prüfung das Konto überzieht!"
            )
        finally:
            aufgabe.Bankkonto = OriginalKonto

    def test_07_entlarvt_fehlerhafte_ueberweisung(self):
        """Mutationstest: Prüft, ob test_08 fehlerhafte Überweisung entlarvt."""
        OriginalKonto = aufgabe.Bankkonto
        class BuggyKonto(OriginalKonto):
            def ueberweisen(self, ziel_konto, betrag):
                self.abheben(betrag)
                # Fehler: Zielkonto erhält kein Geld!

        try:
            aufgabe.Bankkonto = BuggyKonto
            result = self._run_test_case(self.TestBankkonto, "test_08_ueberweisung")
            self.assertFalse(
                result.wasSuccessful(),
                "test_08_ueberweisung muss fehlschlagen, wenn bei der Überweisung das Zielkonto nicht gutgeschrieben wird!"
            )
        finally:
            aufgabe.Bankkonto = OriginalKonto


if __name__ == "__main__":
    res = unittest.main(verbosity=2, exit=False)
    try:
        from pathlib import Path
        root_dir = Path(__file__).parent.parent.parent.resolve()
        sys.path.insert(0, str(root_dir))
        from gamification import report_single_chapter_result
        rel_pfad = f"{Path(__file__).parent.parent.name}/{Path(__file__).parent.name}"
        report_single_chapter_result(rel_pfad, res.result.wasSuccessful(), res.result.testsRun)
    except Exception:
        pass
    sys.exit(0 if res.result.wasSuccessful() else 1)