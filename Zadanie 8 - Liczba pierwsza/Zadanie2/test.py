import unittest
from pierwsza import LiczbaPierwsza


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.LiczbaPierwsza = LiczbaPierwsza()

    def test_liczba_pierwsza(self):
        assert self.LiczbaPierwsza.pierwsza(2)

    def test_suma_liczb(self):
        liczby = [3, 11, 15, 18, 20]
        assert self.LiczbaPierwsza.suma_liczb_pierwszych(liczby) == 14


if __name__ == '__main__':
    unittest.main()
