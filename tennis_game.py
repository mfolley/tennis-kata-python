class Player:
    def __init__(self, points=0):
        self.points = points


class TennisGame:
    score_map = {3: 'forty', 2: 'thirty', 1: 'fifteen', 0: 'love'}

    def __init__(self, player1=Player(), player2=Player()):
        self.player1 = player1
        self.player2 = player2

    def score(self):
        if self.player1.points >= 4 and self.player1.points - self.player2.points >= 2:
            return "player1 wins"
        if self.player2.points >= 4 and self.player2.points - self.player1.points >= 2:
            return "player2 wins"
        if self.player1.points >= 3 and self.player1.points > self.player2.points:
            return "advantage player1"
        if self.player2.points >= 3 and self.player2.points > self.player1.points:
            return "advantage player2"
        if self.player1.points == self.player2.points:
            if self.player1.points >= 3:
                return "deuce"
            return TennisGame.score_map[self.player1.points] + "-" + "all"
        return TennisGame.score_map[self.player1.points] + "-" + TennisGame.score_map[self.player2.points]
