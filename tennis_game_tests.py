import unittest
from tennis_game import TennisGame


class TestTennisGame(unittest.TestCase):
    def player_wins_points(self, player, points):
        for i in range(points):
            player.wins_point()

    def test_returns_fifteen_love_when_score_1_0(self):
        # arrange
        tennis_game = TennisGame()
        # act
        tennis_game.player1.wins_point()
        # assert
        self.assertEqual("fifteen-love", tennis_game.score())

    def test_returns_fifteen_all_when_score_1_1(self):
        # arrange
        tennis_game = TennisGame()
        # act
        tennis_game.player1.wins_point()
        tennis_game.player2.wins_point()
        # assert
        self.assertEqual("fifteen-all", tennis_game.score())

    def test_returns_love_fifteen_when_score_0_1(self):
        # arrange
        tennis_game = TennisGame()
        # act
        tennis_game.player2.wins_point()
        # assert
        self.assertEqual("love-fifteen", tennis_game.score())

    def test_returns_thirty_fifteen_when_score_2_1(self):
        # arrange
        tennis_game = TennisGame()
        # act
        self.player_wins_points(tennis_game.player1, 2)
        tennis_game.player2.wins_point()
        # assert
        self.assertEqual("thirty-fifteen", tennis_game.score())

    def test_returns_thirty_forty_when_score_2_3(self):
        # arrange
        tennis_game = TennisGame()
        # act
        self.player_wins_points(tennis_game.player1, 2)
        self.player_wins_points(tennis_game.player2, 3)
        # assert
        self.assertEqual("thirty-forty", tennis_game.score())

    def test_returns_deuce_when_score_3_3(self):
        # arrange
        tennis_game = TennisGame()
        # act
        self.player_wins_points(tennis_game.player1, 3)
        self.player_wins_points(tennis_game.player2, 3)
        # assert
        self.assertEqual("deuce", tennis_game.score())

    def test_returns_advantage_player1_when_score_4_3(self):
        # arrange
        tennis_game = TennisGame()
        # act
        self.player_wins_points(tennis_game.player1, 4)
        self.player_wins_points(tennis_game.player2, 3)
        # assert
        self.assertEqual("advantage player1", tennis_game.score())

    def test_returns_advantage_player2_when_score_3_4(self):
        # arrange
        tennis_game = TennisGame()
        # act
        self.player_wins_points(tennis_game.player1, 3)
        self.player_wins_points(tennis_game.player2, 4)
        # assert
        self.assertEqual("advantage player2", tennis_game.score())

    def test_returns_advantage_player1_when_score_5_4(self):
        # arrange
        tennis_game = TennisGame()
        # act
        self.player_wins_points(tennis_game.player1, 5)
        self.player_wins_points(tennis_game.player2, 4)
        # assert
        self.assertEqual("advantage player1", tennis_game.score())

    def test_returns_advantage_player2_when_score_5_6(self):
        # arrange
        tennis_game = TennisGame()
        # act
        self.player_wins_points(tennis_game.player1, 5)
        self.player_wins_points(tennis_game.player2, 6)
        # assert
        self.assertEqual("advantage player2", tennis_game.score())

    def test_returns_player1_wins_when_score_5_3(self):
        # arrange
        tennis_game = TennisGame()
        # act
        self.player_wins_points(tennis_game.player1, 5)
        self.player_wins_points(tennis_game.player2, 3)
        # assert
        self.assertEqual("player1 wins", tennis_game.score())

    def test_returns_player2_wins_when_score_9_11(self):
        # arrange
        tennis_game = TennisGame()
        # act
        self.player_wins_points(tennis_game.player1, 9)
        self.player_wins_points(tennis_game.player2, 11)
        # assert
        self.assertEqual("player2 wins", tennis_game.score())

    def test_returns_deuce_score_16_16(self):
        # arrange
        tennis_game = TennisGame()
        # act
        self.player_wins_points(tennis_game.player1, 16)
        self.player_wins_points(tennis_game.player2, 16)
        # assert
        self.assertEqual("deuce", tennis_game.score())

if __name__ == '__main__':
    unittest.main()
