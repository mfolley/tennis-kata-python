class Player:
    def __init__(self, name="anonymous_player", points=0):
        self.name = name
        self.points = points

    def with_points(self, points):
        self.points = points
        return self

    def called(self, name):
        self.name = name
        return self


class TennisGame:
    score_map = {3: 'forty', 2: 'thirty', 1: 'fifteen', 0: 'love'}

    def __init__(self, player1=Player(), player2=Player()):
        self.players = (player1, player2)

    def with_players(self, player1, player2):
        self.players = (player1, player2)
        return self

    @property
    def score(self):
        for player in self.players:
            if player.points >= 4:
                [other_player] = [p for p in self.players if p != player]
                if player.points > other_player.points:
                    if player.points - other_player.points >= 2:
                        return player.name + " wins"
                    return "advantage " + player.name
        if self.players[0].points == self.players[1].points:
            if self.players[0].points >= 3:
                return "deuce"
            return TennisGame.score_map[self.players[0].points] + "-" + "all"
        return TennisGame.score_map[self.players[0].points] + "-" + TennisGame.score_map[self.players[1].points]
