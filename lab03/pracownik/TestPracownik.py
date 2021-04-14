import unittest
import Klasy


class TestPracownik(unittest.TestCase):
    def setUp(self):
        self.Pracownik = Klasy.Pracownik()

    def test_Email(self):
        self.assertIn(self.Pracownik.Email(), "Jan.Kowalski@testemail.com")

    def test_Fullname(self):
        self.assertIn(self.Pracownik.Fullname(), "Jan Kowalski")

    def test_Job_raise(self):
        self.assertEqual(self.Pracownik.Job_raise(), 4000)



if __name__ == '__main__':
    unittest.main()






















