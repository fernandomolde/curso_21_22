import unittest
from unittest.case import TestCase
import ej_02_punto 

class TestPunto(unittest.TestCase):
    def test_constructor_0_0_devuelve_0_0(self):
        p = ej_02_punto.Punto(0,0)
        self.assertEqual(p.x,0)
        self.assertEqual(p.y,0)

    def test_x_no_int_da_error(self):
        p = ej_02_punto.Punto('p','o')
        self.assertEqual(p.x,0)
        self.assertEqual(p.y,0)
    
    def test_x_y_no_int_da_error(self):
        p = ej_02_punto.Punto((1+2j),'o')
        self.assertEqual(p.x,0)
        self.assertEqual(p.y,0)

    def test_x_y_float_no_int_da_error(self):
        p = ej_02_punto.Punto(1,2,3,4)
        self.assertEqual(p.x,1,2)
        self.assertEqual(p.y,3,4)
    


class TestRectangulo(unittest,TestCase):
    def test_es_un_rectangulo(self):
        p1 = ej_02_punto.Punto(4,2)
        p2 = ej_02_punto.Punto(3,-1)
        r = ej_02_punto.Rectangulo(p1,p2)
        self.assertEqual(r.v1,ej_02_punto.Punto(4,2))
        self.assertEqual(r.v2,ej_02_punto.Punto(3,-1))
        self.assertEqual(r.v3,ej_02_punto.Punto(4,-1))
        self.assertEqual(r.v4,ej_02_punto.Punto(3,2))