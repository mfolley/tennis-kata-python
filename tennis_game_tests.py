import unittest
from tennis_game import TennisGame, Player


class TestTennisGame(unittest.TestCase):
    def test_returns_fifteen_love_when_score_1_0(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(1),
                Player().called("Roger").with_points(0)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("fifteen-love", actual_score)

    def test_returns_fifteen_all_when_score_1_1(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(1),
                Player().called("Roger").with_points(1)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("fifteen-all", actual_score)

    def test_returns_love_fifteen_when_score_0_1(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(0),
                Player().called("Roger").with_points(1)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("love-fifteen", actual_score)

    def test_returns_thirty_fifteen_when_score_2_1(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(2),
                Player().called("Roger").with_points(1)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("thirty-fifteen", actual_score)

    def test_returns_thirty_forty_when_score_2_3(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(2),
                Player().called("Roger").with_points(3)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("thirty-forty", actual_score)

    def test_returns_deuce_when_score_3_3(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(3),
                Player().called("Roger").with_points(3)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("deuce", actual_score)

    def test_returns_advantage_player1_when_score_4_3(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(4),
                Player().called("Roger").with_points(3)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("advantage Rafael", actual_score)

    def test_returns_advantage_player2_when_score_3_4(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(3),
                Player().called("Roger").with_points(4)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("advantage Roger", actual_score)

    def test_returns_advantage_player1_when_score_5_4(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(5),
                Player().called("Roger").with_points(4)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("advantage Rafael", actual_score)

    def test_returns_advantage_player2_when_score_5_6(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(5),
                Player().called("Roger").with_points(6)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("advantage Roger", actual_score)

    def test_returns_player1_wins_when_score_4_2(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(4),
                Player().called("Roger").with_points(2)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("Rafael wins", actual_score)

    def test_returns_player2_wins_when_score_9_11(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(9),
                Player().called("Roger").with_points(11)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("Roger wins", actual_score)

    def test_returns_deuce_score_score_16_16(self):
        # arrange
        tennis_game = TennisGame().with_players(
                Player().called("Rafael").with_points(16),
                Player().called("Roger").with_points(16)
        )
        # act
        actual_score = tennis_game.score
        # assert
        self.assertEqual("deuce", actual_score)


if __name__ == '__main__':
    unittest.main()
