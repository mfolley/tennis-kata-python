import unittest
from tennis_game import TennisGame


class TestTennisGame(unittest.TestCase):
    def test_prints_fifteen_love_when_score_1_0(self):
        tennis_game = TennisGame()
        self.assertEqual(tennis_game.score(), "fifteen-love")


if __name__ == '__main__':
    unittest.main()
