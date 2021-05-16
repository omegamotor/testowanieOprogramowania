import unittest
from game_main import game


class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = game(1)

    def test_throw_three_times(self):
        self.score = 0
        for i in range(3):
            self.score = self.score + self.game

        self.assertEqual(3, self.score)

    def test_strike(self):
        self.score = 0
        self.tryouts = [10,6,3]

        for i in self.tryouts:
            self.score = self.score + game(i)

        self.assertEqual(19, self.score)





if __name__ == '__main__':
    unittest.main()
