import unittest

from multiplicacion import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 5), 25)
        self.assertEqual(multiplicar(-4, 3), -12)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(-5, -5), 25)

if __name__ == "__main__":
    unittest.main()