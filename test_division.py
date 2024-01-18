from cmath import nan
import unittest

from division import dividir

class TestDivision(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(8, 2), 4)
        self.assertEqual(dividir(-8, 2), -4)
        self.assertEqual(dividir(8, -2), -4)
        self.assertEqual(dividir(-8, -2), 4)
        
        
    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            resultado = dividir(10, 0)   

if __name__ == "__main__":
    unittest.main()
        