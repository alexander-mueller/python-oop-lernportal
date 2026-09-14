# -*- coding: utf-8 -*-
"""
Testsuite für Projekt: Betriebliche Projektarbeit (40h) & Fachgespräch
"""
import unittest
import aufgabe

class TestFIDP(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(True, "Grundlegende Prüfung bestanden.")

if __name__ == '__main__':
    unittest.main()
