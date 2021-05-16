import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_Add(self):
        self.assertEqual(main.add(15, 15), 30)

    def test_Subtract(self):
        self.assertEqual(main.subtract(20, 4), 16)

    def test_Multiply(self):
        self.assertEqual(main.multiply(2, 6), 12)

    def test_Divide(self):
        self.assertEqual(main.divide(4, 2), 2)
        self.assertRaises(ZeroDivisionError, main.divide, 2, 0)

    def test_Exponentiation(self):
        self.assertEqual(main.exponentiation(2), 4)

    def test_SquareRoot(self):
        self.assertEqual(main.squareRoot(4), 2)

    def test_Percent(self):
        self.assertEqual(main.percent(5, 4), 1)
        self.assertRaises(ZeroDivisionError, main.percent, 4, 0)


if __name__ == '__main__':
    unittest.main()

