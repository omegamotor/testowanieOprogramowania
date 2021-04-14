import unittest
from main import Portfel

class PortfelTestCase(unittest.TestCase):
    def setUp(self):
        self.portfel = Portfel(0)

    def test_domyslna_wartosc(self):
        self.assertEqual(0, self.portfel.ileMam())

    def test_dodawanie_srodkow(self):
        self.portfel = Portfel(0)
        self.portfel.dodaj(10)
        self.portfel.dodaj(15)
        self.assertEqual(25, self.portfel.ileMam())

    def test_odejmowanie_srodkow(self):
        self.portfel = Portfel(0)
        self.portfel.dodaj(100)
        self.portfel.wydaj(65)
        self.assertEqual(35, self.portfel.ileMam())

if __name__ == '__main__':
    unittest.main()
