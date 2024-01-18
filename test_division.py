from cmath import nan
import unittest

from division import dividir

class TestDivision(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(8, 2), 4)
        self.assertEqual(dividir(-8, 2), -4)
        self.assertEqual(dividir(8, -2), -4)
        self.assertEqual(dividir(-8, -2), 4)
        self.assertEqual(dividir(8, 0), ZeroDivisionError)

if __name__ == "__main__":
    unittest.main()
        