import unittest
import temp


class TestCalculator(unittest.TestCase):

    def test_celsiusOnFah(self):
        self.assertEqual(temp.celsiusOnFah(5), 41)

    def test_fahrenheitOnCel(self):
        self.assertEqual(temp.fahrenheitOnCel(5), -15)

    def test_celsiusOnKel(self):
        self.assertEqual(temp.celsiusOnKel(3), 276.15)


if __name__ == '__main__':
    unittest.main()