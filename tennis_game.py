class TennisGame:
    score_map = {3: 'forty', 2: 'thirty', 1: 'fifteen', 0: 'love'}

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

    def score(self):
        if self.player1.points >= 5 and self.player1.points - self.player2.points >= 2:
            return "player1 wins"
        if self.player2.points >= 5 and self.player2.points - self.player1.points >= 2:
            return "player2 wins"
        if self.player1.points >= 4 and self.player1.points > self.player2.points:
            return "advantage player1"
        if self.player2.points >= 4 and self.player2.points > self.player1.points:
            return "advantage player2"
        if self.player1.points == self.player2.points:
            if self.player1.points >= 3:
                return "deuce"
            return TennisGame.score_map[self.player1.points] + "-" + "all"
        return TennisGame.score_map[self.player1.points] + "-" + TennisGame.score_map[self.player2.points]


class Player:
    def __init__(self):
        self.points = 0

    def wins_point(self):
        self.points += 1
