import urllib.request
from bs4 import BeautifulSoup
import csv
import Player
import Team
import Game
import Play

print("The information used here was obtained free of charge from and is copyrighted by Retrosheet.  Interested "
      "parties may contact Retrosheet at 20 Sunset Rd., Newark, DE 19711.")

years = [2020]
folder = "C:\\Users\\daraw\\Documents\\bevent"

teams = {}
players = {}
games = {}


def checkNoBatterPlay(out_string):
    toCheck = out_string[:2]
    if toCheck is "BK" or "CS" or "DI" or "OA" or "PB" or "WP" or "PO" or "SB":
        return True
    return False


for year in years:
    teamFileName = folder + "\\TEAM" + str(year)

    with open(teamFileName, newline='') as teamFile:
        teamreader = csv.reader(teamFile)
        for row in teamreader:
            teams[row[0]] = Team.Team(row[3], row[2], row[0], row[1])

    for team in teams.values():
        rosterFileName = folder + "\\" + team.ID + str(year) + ".ROS"
        with open(rosterFileName, newline='') as rosterFile:
            rosterreader = csv.reader(rosterFile)
            for row in rosterreader:
                bats_lefty = (row[3] == "L")
                throws_lefty = (row[4] == "L")
                player = Player.Player(row[0], row[2], row[1], row[5], row[6], throws_lefty, bats_lefty)
                players[player.ID] = player
                teams[player.team].addPlayer(player)

    for team in teams.values():
        gameFileName = folder + "\\" + str(year) + team.ID + ".EV" + team.league
        with open(gameFileName, newline='') as gameFile:
            gamereader = csv.reader(gameFile)
            currentGame = None
            homePitcher = None
            awayPitcher = None
            eventList = []
            bases = [None, None, None]
            homeScore = 0
            awayScore = 0
            for row in gamereader:
                if row[0] == "id":
                    currentGame = Game.Game(row[1])
                    homePitcher = None
                    awayPitcher = None
                    games[row[1]] = currentGame
                elif row[0] == "info":
                    if row[1] == "visteam" or row[1] == "hometeam":
                        teams[row[2]].addGame(currentGame)
                    currentGame.addInfo(row[1], row[2])
                elif row[0] == "start":
                    currentPlayer = players[row[1]]
                    currentPlayer.addGame(currentGame)
                    currentGame.addPlayer(currentPlayer, (row[3] == "1"))

                    if int(row[5]) == 1:
                        if int(row[3]) == 0:
                            awayPitcher = currentPlayer
                        elif int(row[3]) == 1:
                            homePitcher = currentPlayer
                elif row[0] == "play":
                    if checkNoBatterPlay(row[6]):
                        eventList.append(row[6])
                        if row[6].__contains__("."):
                            start = row[6].find(".") + 1
                            running = True
                            while running:
                                substr = row[6][start:start + 3]
                                if substr[1] == "-":
                                    if substr[2] == "H":
                                        bases[int(substr[0]) - 1] = None
                                        # if there is a B-H situation when the ball wasnt put into play i am gonna
                                        # lose it
                                        if row[2] == "0":
                                            awayScore += 1
                                        else:
                                            homeScore += 1
                                    else:
                                        bases[int(substr[2]) - 1] = bases[int(substr[0]) - 1]
                                        bases[int(substr[0]) - 1] = None
                                else:
                                    bases[int(substr[0]) - 1] = None
                                start = row[6].find(";", start + 1)
                                if start == -1:
                                    running = False
                                else:
                                    start += 1
                    elif row[6] != "NP":
                        pitcher = None
                        if int(row[2]) == 0:
                            pitcher = homePitcher
                        else:
                            pitcher = awayPitcher
                        topInning = (row[2] == "0")
                        # TODO bases score
                        currentPlay = Play.Play(game=currentGame, pitcher=pitcher, batter=players[row[3]],
                                                inning=int(row[1]), topInning=topInning, ballsStrike=int(row[4]),
                                                pitches_string=row[5], outcome_string=row[6], pitching_events=eventList,
                                                bases_before_bat=bases, home_score=homeScore, visit_score=awayScore)
                        eventList = []
                        currentGame.addPlay(currentPlay)
                        bases = currentPlay.bases_after
                        homeScore = currentPlay.home_score
                        awayScore = currentPlay.visit_score
