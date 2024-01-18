import unittest

from resta import restar

class TestRestar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(4, 1), 3)
        self.assertEqual(restar(-2, -3), 1)
        self.assertEqual(restar(3, 0), 3)
        self.assertEqual(restar(-3, 2), -5)
        self.assertEqual(restar(3, -2), 5)

if __name__ == '__main__':
    unittest.main()