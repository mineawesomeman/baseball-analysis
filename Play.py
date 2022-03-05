import math
import Pitch
import Game
import OutcomeArrayObj as oaj
import EventModifier as em


class Play:
    game = None
    pitcher = None
    batter = None
    bases_before_bat = None
    home_score = 0
    visit_score = 0
    inning = 0
    topInning = True
    balls = 0
    strikes = 0
    pitches_string = ""
    pitches = None
    outcome_string = ""
    outcome = 0
    outcome_array = None
    outcome_location = None
    outcome_modifiers = None
    bases_after = None
    pitching_events = None

    def __init__(self, game=None, pitcher=None, batter=None, bases_before_bat=None, home_score=0, visit_score=0,
                 inning=0, topInning=True, ballsStrike=00, pitches_string="", outcome_string="", pitching_events=None):
        if pitching_events is not None:
            self.pitching_events = pitching_events
        else:
            self.pitching_events = []
        if bases_before_bat is not None:
            self.bases_before_bat = bases_before_bat
        else:
            self.bases_before_bat = []

        self.pitches = []
        self.outcome_modifiers = []
        self.bases_after = []
        self.outcome_array = []

        self.game = game
        self.pitcher = pitcher
        self.batter = batter
        self.home_score = home_score
        self.visit_score = visit_score
        self.inning = inning
        self.topInning = topInning
        self.balls = math.floor(ballsStrike / 10)
        self.strikes = math.floor(ballsStrike % 10)
        self.pitches_string = pitches_string
        self.outcome_string = outcome_string
        self.readPitches()
        self.readOutcome()

    def readPitches(self):
        prev_pitch = None
        for c in self.pitches_string:
            if c == '+' or c == '*' or c == '>':
                if prev_pitch is not None:
                    prev_pitch.addModifier(c)
            else:
                newPitch = Pitch.Pitch(c)
                self.pitches.append(newPitch)
                prev_pitch = newPitch

    def readOutcome(self, start=0):
        strLoc = start
        if self.checkDigit(strLoc):
            self.outcome = 1
            strLoc = self.playerString(strLoc)
        elif self.outcome_string[strLoc:strLoc+3] == 'C/E':
            self.outcome = 2
            strLoc += self.playerString(strLoc + 3)
        elif self.outcome_string[strLoc:strLoc+1] == 'S':
            self.outcome = 3
            strLoc = self.playerString(strLoc + 1)
        elif self.outcome_string[strLoc:strLoc+1] == 'D':
            self.outcome = 4
            strLoc = self.playerString(strLoc + 1)
        elif self.outcome_string[strLoc:strLoc+1] == 'T':
            self.outcome = 5
            strLoc = self.playerString(strLoc + 1)
        elif self.outcome_string[strLoc:strLoc+3] == 'DGR':
            self.outcome = 6
            strLoc += 3
        elif self.outcome_string[strLoc:strLoc+1] == 'E':
            self.outcome = 7
            strLoc = self.playerString(strLoc + 1)
        elif self.outcome_string[strLoc:strLoc+2] == 'FC':
            self.outcome = 8
            strLoc = self.playerString(strLoc + 2)
        elif self.outcome_string[strLoc:strLoc+3] == 'FLE':
            self.outcome = 9
            strLoc = self.playerString(strLoc + 3)
        elif self.outcome_string[strLoc:strLoc+2] == 'HR':
            self.outcome = 10
            strLoc = self.playerString(strLoc + 2)
        elif self.outcome_string[strLoc:strLoc+2] == 'HP':
            self.outcome = 11
            strLoc += 2
        elif self.outcome_string[strLoc:strLoc+1] == 'H':
            self.outcome = 10
            strLoc = self.playerString(strLoc + 1)
        elif self.outcome_string[strLoc:strLoc+1] == 'K':
            self.outcome = 12
            strLoc += 1
        elif self.outcome_string[strLoc:strLoc+2] == 'NP':
            self.outcome = -1
            strLoc += 2
        elif self.outcome_string[strLoc:strLoc+2] == 'IW':
            self.outcome = 13
            strLoc += 2
        elif self.outcome_string[strLoc:strLoc+1] == 'I':
            self.outcome = 13
            strLoc += 2
        elif self.outcome_string[strLoc:strLoc+1] == 'W':
            self.outcome = 14
            strLoc += 1
        else:
            self.outcome = -1
            while (strLoc < len[self.outcome_string]) and (self.outcome_string[strLoc] is not '+' or '/' or '.'):
                strLoc += 1

        if strLoc < len(self.outcome_string) and self.outcome_string[strLoc] == '+':
            beginLoc = strLoc + 1
            while (self.outcome_string[strLoc] is not '/' or '.') and (strLoc < len[self.outcome_string]):
                strLoc += 1
            self.pitching_events.append(self.outcome_string[beginLoc:strLoc])

        while strLoc < len(self.outcome_string) and self.outcome_string[strLoc] == '/':
            strLoc += 1
            beginLoc = strLoc
            while strLoc < len(self.outcome_string) and self.outcome_string[strLoc] is not '/' or '.':
                strLoc += 1
            self.outcome_modifiers.append(em.EMfromStr(self.outcome_string[beginLoc:strLoc]))

    def checkDigit(self, loc):
        if self.outcome_string[loc] is '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0':
            return True
        return False

    def playerString(self, loc):
        strLoc = loc
        while strLoc < len(self.outcome_string) and (self.outcome_string[strLoc] is not '/' or '.' or '+'):
            if self.outcome_string[strLoc] is '/' or '.' or '+':
                break
            if self.outcome_string[strLoc] == '(':
                strLoc += 1
                if self.checkDigit(strLoc):
                    self.outcome_array.append(oaj.OutcomeArrayObj(2, int(self.outcome_string[strLoc])))
                else:
                    self.outcome_array.append(oaj.OutcomeArrayObj(2, 0))
                strLoc += 1
            if self.checkDigit(strLoc):
                isPlayer = not self.checkDigit(strLoc + 1)
                self.outcome_array.append(oaj.OutcomeArrayObj(1, int(self.outcome_string[strLoc]), isPlayer))

            strLoc += 1
        return strLoc
