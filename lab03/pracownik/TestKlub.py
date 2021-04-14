import unittest
import Klasy
import os


class TestKlub(unittest.TestCase):
    def setUp(self):
        self.Klub = Klasy.KlubPilkarski()

    def test_Trener(self):
        self.assertFalse(self.Klub.has_trener)

    def test_TrenerAdd(self):
        self.Klub.AddTrener()
        self.assertTrue(self.Klub.has_trener)

    def test_TrenerRemove(self):
        self.Klub.RemoveTrener()
        self.assertFalse(self.Klub.has_trener)

    def test_CreateTxt(self):
        self.Klub.CreateTxt()
        f = open("Kluby.txt", "r")
        x = f.read()
        self.assertIn(f.read(), "Manchester City, Bayern")
        f.close()


"""
    def tearDown(self):
        os.remove("Kluby.txt")
"""


if __name__ == '__main__':
    unittest.main()
