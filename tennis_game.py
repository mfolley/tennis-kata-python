class Player:
    def __init__(self, points=0):
        self.points = points
        self.name = ""

    def with_points(self, points):
        self.points = points
        return self

    def called(self, name):
        self.name = name
        return self


class TennisGame:
    score_map = {3: 'forty', 2: 'thirty', 1: 'fifteen', 0: 'love'}

    def __init__(self, player1=Player(), player2=Player()):
        self.player1 = player1
        self.player2 = player2

    def with_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        return self

    @property
    def score(self):
        if self.player1.points >= 4 or self.player2.points >= 4:
            players = [self.player1, self.player2]
            for player in players:
                [other_player] = [p for p in players if p != player]
                if player.points > other_player.points:
                    if player.points - other_player.points >= 2:
                        return player.name + " wins"
                    return "advantage " + player.name
        if self.player1.points == self.player2.points:
            if self.player1.points >= 3:
                return "deuce"
            return TennisGame.score_map[self.player1.points] + "-" + "all"
        return TennisGame.score_map[self.player1.points] + "-" + TennisGame.score_map[self.player2.points]
