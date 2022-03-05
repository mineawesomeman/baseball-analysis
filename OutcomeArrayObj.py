class OutcomeArrayObj:
    oType = 0 # 1 for a player 2 for a base
    number = 0 # either player number or base number
    outCredit = True # if the player is credited with an out

    def __init__(self, oType, number, outCredit=True):
        self.oType = oType
        self.number = number
        self.outCredit = outCredit
