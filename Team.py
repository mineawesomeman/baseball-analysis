class Team:
    players = None
    games = None
    name = ""
    city = ""
    ID = ""
    league = ""

    def __init__(self, name, city, ID, league):
        self.name = name
        self.city = city
        self.ID = ID
        self.league = league
        self.players = {}
        self.games = {}

    def __str__(self):
        return self.city + " " + self.name + " (" + self.ID + ")"

    def addPlayer(self, player):
        self.players[player.ID] = player

    def addGame(self, game):
        self.games[game.ID] = game
