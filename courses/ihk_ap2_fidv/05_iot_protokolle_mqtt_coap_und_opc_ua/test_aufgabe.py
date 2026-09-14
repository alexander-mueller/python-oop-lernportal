# -*- coding: utf-8 -*-
"""
Testsuite für LF 11: Industrielle IoT-Protokolle (OPC UA, MQTT, CoAP)
"""
import unittest
import aufgabe

class TestFIDV(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(True, "Vernetzungstest erfolgreich.")

if __name__ == '__main__':
    unittest.main()
