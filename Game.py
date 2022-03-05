class Game:
    info = None
    homeplayers = None
    visitplayers = None
    plays = None
    ID = ""
    home_score = 0
    away_score = 0

    def __init__(self, ID):
        self.ID = ID
        self.info = {}
        self.homeplayers = {}
        self.visitplayers = {}
        self.plays = []

    def addInfo(self, key, data):
        self.info[key] = data

    def getInfo(self, key):
        return self.info[key]

    def removeInfo(self, key):
        return self.info.pop(key)

    def addPlayer(self, player, isHome=True):
        if isHome:
            self.homeplayers[player.ID] = player
        else:
            self.visitplayers[player.ID] = player

    def homeScored(self, runs):
        self.home_score += runs

    def awayScored(self, runs):
        self.away_score += runs

    def addPlay(self, play):
        self.plays.append(play)
