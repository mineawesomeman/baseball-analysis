class Player:
    first_name = ""
    last_name = ""
    ID = ""
    team = None
    position = ""
    throws_lefty = False
    bats_lefty = False
    games = {}

    def __init__(self, ID, first_name, last_name, team, position, t_l=False, h_l=False):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.team = team
        self.position = position
        self.throws_lefty = t_l
        self.hits_lefty = h_l

    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + self.ID + ")"

    def addGame(self, game):
        self.games[game.ID] = game
