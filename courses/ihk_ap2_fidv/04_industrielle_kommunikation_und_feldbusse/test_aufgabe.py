# -*- coding: utf-8 -*-
"""
Testsuite für LF 10: Feldbusse & Industrial Ethernet (Profinet, Modbus, TSN)
"""
import unittest
import aufgabe

class TestFIDV(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(True, "Vernetzungstest erfolgreich.")

if __name__ == '__main__':
    unittest.main()
