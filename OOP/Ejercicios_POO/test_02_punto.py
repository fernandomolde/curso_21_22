from typing import Union
import unittest
import Ej_02_punto

class TestPunto(unittest.TestCase):
    def test_constructor_0_0_devuelve_0_0(self):
        p = Ej_02_punto.Punto(0,0)
        self.assertEqual(p.x,0)
        self.assertEqual(p.y,0)