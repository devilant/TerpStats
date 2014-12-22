import urllib
import datetime
import string
import re
import os
from LineupStats.models import *

walkons = set(['Jacob Susskind', 'John Auslander', 'Spencer Barks', 'Conner Lipinski', 'Varun Ram'])

def parsePbp(pbpLines, isHomeTeam, starters):
    lineupData = {}
    currentPlayers = set(starters)
    nextLineup = set(starters) #apply subs to this set, then swap with current set
    firstHalf = True
    time = datetime.time(0, 20, 0)
    lineupStats = LineupStats()
    madeBasket = False #used to detect if a foul shot is an and-1 shot
    for line in pbpLines:
       if '2nd PERIOD Play-by-Play' in line:
           firstHalf = False
           #end of first half, store lineup stats
           curTime = datetime.time(0, 0, 0)
           elapsedTime = datetime.datetime.combine(datetime.date.today(), time) - datetime.datetime.combine(datetime.date.today(), curTime)                                      
           lineupStats.setElapsedTime(elapsedTime)
           key = string.join(sorted(currentPlayers), ', ')
           if key in lineupData:               
               lineupData[key] += lineupStats
           else:               
               lineupData[key] = lineupStats

           #start of 2nd half
           time = datetime.time(0, 20, 0)
           currentPlayers = set(starters)
           nextLineup = set(starters)
           lineupStats = LineupStats()
           madeBasket = False
       elif re.search(r'\s*OT[0-9]* PERIOD Play-by-Play', line):
           #Start of overtime period, store lineup stats and reset for start of OT
           curTime = datetime.time(0, 0, 0)
           elapsedTime = datetime.datetime.combine(datetime.date.today(), time) - datetime.datetime.combine(datetime.date.today(), curTime)
           lineupStats.setElapsedTime(elapsedTime)
           key = string.join(sorted(currentPlayers), ', ')
           if key in lineupData:
               lineupData[key] += lineupStats
           else:
               lineupData[key] = lineupStats

           #start of OT
           time = datetime.time(0, 5, 0)
           currentPlayers = set(starters)
           nextLineup = set(starters)
           lineupStats = LineupStats()
           madeBasket = False
       else:
           play = parsePbpLine(line)
           if play:
               teamString = play[1]
               opponentString = play[2]
               if not isHomeTeam:
                   teamString = play[2]
                   opponentString = play[1]
               action = parseTeamString(teamString)
               oppAction = parseTeamString(opponentString)
               if action:                   
                   if action[0] == "MADE":
                       if action[1] == "LAYUP" or action[1] == "JUMPER" or action[1] == "DUNK" or action[1] == "TIP-IN":
                           lineupStats.total2pCount += 1
                           lineupStats.made2pCount += 1
                           lineupStats.pointsFor += 2
                           lineupStats.possessionCount += 1
                           madeBasket = True
                       if action[1] == "3 PTR":
                           lineupStats.total3pCount += 1
                           lineupStats.made3pCount += 1
                           lineupStats.pointsFor += 3
                           lineupStats.possessionCount += 1
                           madeBasket = True
                       if action[1] == "FT SHOT":
                           lineupStats.pointsFor += 1
                           madeBasket = False
                           if oppAction and oppAction[0] == "FOUL":
                               #'shooting foul'
                               True #do nothing
                           else:
                               #2nd of 2 free throws                               
                               lineupStats.possessionCount += 1

                   elif action[0] == "MISSED":
                       if action[1] == "LAYUP" or action[1] == "JUMPER" or action[1] == "DUNK" or action[1] == "TIP-IN":
                           lineupStats.total2pCount += 1
                           madeBasket = False
                       if action[1] == "3 PTR":
                           madeBasket = False
                           lineupStats.total3pCount += 1
                       if action[1] == "FT SHOT":                           
                           if madeBasket:
                               #missed the and-1 free throw, so the possession isn't over yet
                               #need to subtract the possession added in the made shot conditional
                               lineupStats.possessionCount -= 1
                               madeBasket = False
                               #print 'missed an and-1 shot', time

                   elif action[0] == "ASSIST":
                       lineupStats.assistCount += 1
                   
                   elif action[0] == "FOUL":
                       lineupStats.foulCount += 1
                       madeBasket = False
                  
                   elif action[0] == "BLOCK":
                       lineupStats.blockCount += 1
                       madeBasket = False

                   elif action[0] == "TURNOVER":
                       madeBasket = False                       
                       lineupStats.turnoverCount += 1
                       lineupStats.possessionCount += 1
                   
                   elif action[0] == "STEAL":
                       madeBasket = False
                       lineupStats.stealsCount += 1

                   elif action[0] == "REBOUND":
                       madeBasket = False
                       if action[1] == "DEF":
                           lineupStats.defReboundCount += 1
                           lineupStats.totalDefReboundCount += 1
                       if action[1] == "OFF":
                           lineupStats.offReboundCount += 1
                           lineupStats.totalOffReboundCount += 1

                   elif action[0] == "SUBIN":                                        
                       nextLineup.add(extractPlayerName(action[1]))
               
                   elif action[0] == "SUBOUT":                      
                       nextLineup.remove(extractPlayerName(action[1]))
                       if len(nextLineup) == 5:
                           #store data for current lineup
                           curTime = play[0]                           
                           elapsedTime = datetime.datetime.combine(datetime.date.today(), time) - datetime.datetime.combine(datetime.date.today(), curTime)
                           lineupStats.setElapsedTime(elapsedTime)
                                                      
                           key = string.join(sorted(currentPlayers), ', ')
                           if key in lineupData:                               
                               lineupData[key] += lineupStats
                           else:                               
                               lineupData[key] = lineupStats
                           
                           #swap in new lineup
                           currentPlayers = set(nextLineup)
                           time = curTime
                           lineupStats = LineupStats()


               if oppAction:                   
                   if oppAction[0] == "MADE":
                       madeBasket = False
                       if oppAction[1] == "LAYUP" or oppAction[1] == "JUMPER" or oppAction[1] == "DUNK" or oppAction[1] == "TIP-IN":                           
                           lineupStats.pointsAgainst += 2
                           lineupStats.oppMade2pCount += 1
                           lineupStats.oppTotal2pCount += 1
                       if oppAction[1] == "3 PTR":
                           lineupStats.pointsAgainst += 3
                           lineupStats.oppMade3pCount += 1
                           lineupStats.oppTotal3pCount += 1
                       if oppAction[1] == "FT SHOT":
                           lineupStats.pointsAgainst += 1
               
                   if oppAction[0] == "MISSED":
                       madeBasket = False
                       if oppAction[1] == "LAYUP" or oppAction[1] == "JUMPER" or oppAction[1] == "DUNK" or oppAction[1] == "TIP-IN":
                           lineupStats.oppTotal2pCount += 1
                       if oppAction[1] == "3 PTR":
                           lineupStats.oppTotal3pCount += 1

                   if oppAction[0] == "TURNOVER":
                       madeBasket = False

                   if oppAction[0] == "REBOUND":
                       madeBasket = False
                       #if opponent gets a def rebound, that's a missed offensive reb opportunity
                       #and vice versa for off rebounds
                       if oppAction[1] == "DEF":                           
                           lineupStats.totalOffReboundCount += 1
                           #opponent gets a defensive rebound, that ends a possession
                           lineupStats.possessionCount += 1
                       if oppAction[1] == "OFF":                           
                           lineupStats.totalDefReboundCount += 1           

    #end of game--store final lineup stats
    curTime = datetime.time(0, 0, 0)            
    elapsedTime = datetime.datetime.combine(datetime.date.today(), time) - datetime.datetime.combine(datetime.date.today(), curTime)
    lineupStats.setElapsedTime(elapsedTime)
    
    key = string.join(sorted(currentPlayers), ', ')
    if key in lineupData:
        lineupData[key] += lineupStats
    else:
        lineupData[key] = lineupStats    

    return lineupData

def parseTeamString(teamString):
    #SUB IN
    match = re.search(r'\s*SUB IN : (.*)', teamString)
    if match:        
        return ("SUBIN", match.group(1))

    #SUB OUT
    match = re.search(r'\s*SUB OUT: (.*)', teamString)
    if match:
        return ("SUBOUT", match.group(1))

    #Rebound
    match = re.search(r'\s*REBOUND \((...)\)', teamString)
    if match:
        return ("REBOUND", match.group(1))

    #turn over
    match = re.search(r'\s*TURNOVR', teamString)
    if match:        
        return ("TURNOVER",)

    #steal
    match = re.search(r'\s*STEAL', teamString)
    if match:
        return ("STEAL",)

    #foul
    match = re.search(r'\s*FOUL', teamString)
    if match:
        return ("FOUL",)

    #block
    match = re.search(r'\s*BLOCK', teamString)
    if match:
        return ("BLOCK",)

    #assist
    match = re.search(r'\s*ASSIST', teamString)
    if match:
        return ("ASSIST",)

    #missed shot
    match = re.search(r'\s*MISSED (.+) by', teamString)
    if match:
        return ("MISSED", match.group(1))

    #made shot
    match = re.search(r'\s*GOOD! (.+) by',  teamString)
    if match:
        return ("MADE", match.group(1))


#returns tuple (time, homeTeamString, visitorTeamString, scoreUpdate)
def parsePbpLine(line):
    match = re.search(r'(.*)(\d\d:\d\d)(.*)', line)
    if match:
        clock = match.group(2).split(':')
        time = datetime.time(0, int(clock[0]), int(clock[1]))

        homeTeamString = match.group(1)

        #check for score update
        visitorTeamString = match.group(3)
        scoreUpdate = None
        match = re.search(r'(\d+-\d+)\s*[HV] \d+\s*(.*)', visitorTeamString)
        if match:
            scoreUpdate = match.group(1)
            visitorTeamString = match.group(2)

        homeTeamString = string.lstrip(string.rstrip(homeTeamString))
        visitorTeamString = string.lstrip(string.rstrip(visitorTeamString))
        return (time, homeTeamString, visitorTeamString, scoreUpdate)

#parses box score and returns a tuple (isHomeTeam, setOfStarters)
def parseBoxScore(boxScoreLines):
    parsingMdScore = False
    homeTeam = True
    starters = set()
    for line in boxScoreLines:
        team = startOfTeamBoxScore(line)
        if team:
            if team[0] == 'Maryland' or team[0] == 'Maryland Terrapins':
                parsingMdScore = True                
                if team[1] == "VISITORS":                    
                    homeTeam = False
            else:
                parsingMdScore = False                

        if parsingMdScore:
            player = parsePlayer(line)
            if player:
                if player[1]:
                    starters.add(extractPlayerName(player[0]))
    
    return (homeTeam, starters)


#returns a tuple of (playerName, starting)
def parsePlayer(line):
    #match = re.search(r'(\d+)\s+(<A.+</A>)\.*\s*([fcg\*]?)\s+\d', line)
    match = re.search(r'(\d+)\s+([a-zA-Z\s]+)\.+\s([fcg\*]?)\s+\d', line)
    if match: 
        return (match.group(2), match.group(3) != '')
    return None        

def extractPlayerName(htmlATag):
    match = re.search(r'>(.*)</A>', htmlATag)
    if match:
        return match.group(1)
    return htmlATag

def startOfTeamBoxScore(line):
    match = re.search(r'VISITORS: ([\w\s]+) \(?\d', line)
    if match:
        team = match.group(1)
        return (team, "VISITORS")
    match = re.search(r'HOME TEAM: ([\w\s]+) \(?\d', line)
    if match:
        team = match.group(1)
        return (team, "HOMETEAM")

def parseGameLog(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    boxScoreLines = []
    pbpLines = []
    parsingBoxScore = False
    parsingPbp = False
    for line in lines:
        line = string.lstrip(string.rstrip(line))
        if line == "Official Basketball Box Score":                        
            parsingBoxScore = True

        if line == "Play-by-Play":            
            parsingPbp = True
            parsingBoxScore = False
        if "Official Basketball Box Score -- 1st Half" in line:
            parsingPbp = False

        if parsingBoxScore:
            boxScoreLines.append(line)
        if parsingPbp:
            pbpLines.append(line)

    (isHomeTeam, starters) = parseBoxScore(boxScoreLines)
    lineupData = parsePbp(pbpLines, isHomeTeam, starters)
    return lineupData

def parseGameLogsByFolder(path):
    files = os.listdir(path)
    gamesData = []
    for filename in files:
        lineupData = parseGameLog(os.path.join(path, filename))
        data = (filename, lineupData)
        gamesData.append(data)
    return gamesData

#sums lineup stats for all games in games data and sorts by time playing time
#input: result of parseGameLogsByFolder
def sumLineupStats(gamesData):
    totalLineupData = {}
    for gameData in gamesData:
        lineupsData = gameData[1]
        for lineupData in lineupsData.items():
            lineup = lineupData[0]
            stats = lineupData[1]
            if lineup in totalLineupData:
                totalLineupData[lineup] += stats
            else:
                totalLineupData[lineup] = stats
    sortedLineupStats = sorted(totalLineupData.items(), key=lambda statsDict: statsDict[1].elapsedTime)
    sortedLineupStats.reverse()
    return sortedLineupStats

#input: list of tuples (lineup, lineupStats)
def outputLineupsToHtml(lineupStats):
    html = "<table border='1'>\n"
    html += "<tr>\n"
    html += "<th>Lineup</th>\n"
    html += "<th>Time On Court</th>\n"
    html += "<th>Possessions</th>\n"    
    html += "<th>Points Per Poss</th>\n"
    html += "<th>Opp Points Per Poss</th>\n"
    html += "<th>Efficiency Margin</th>\n"
    html += "<th>2p%</th>\n"
    html += "<th>3p%</th>\n"
    html += "<th>Def Rb %</th>\n"
    html += "<th>Off Rb %</th>\n"
    html += "</tr>\n"

    for lineupTuple in lineupStats:
        if lineupTuple[1].possessionCount > 0:
            html += "<tr>\n"
            html += "<td>" + lineupTuple[0] + "</td>\n"
            html += "<td>" + str(lineupTuple[1].elapsedTime) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].possessionCount) + "</td>\n"            
            html += "<td>" + str(lineupTuple[1].getPointsPerPossession()) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].getOppPointsPerPossession()) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].getEfficiencyMargin()) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].get2pPercentage()) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].get3pPercentage()) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].getDefReboundPercentage()) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].getOffReboundPercentage()) + "</td>\n"
            html += "</tr>\n"

    html += "</table>"

    file = open("test.html", 'w')
    file.write(html)
    file.close()

    return html

def outputRawDataToHtml(lineupStats):
    html = "<table border='1'>\n"
    html += "<tr>\n"
    html += "<th>Lineup</th>\n"
    html += "<th>Time On Court</th>\n"
    html += "<th>Possessions</th>\n"    
    html += "<th>Points For</th>\n"
    html += "<th>Points Against</th>\n"
    html += "<th>2p Makes</th>\n"
    html += "<th>2p Attempts</th>\n"
    html += "<th>3p Makes</th>\n"
    html += "<th>3p Attempts</th>\n"
    html += "<th>Opp 2p Makes</th>\n"
    html += "<th>Opp 2p Attempts</th>\n"
    html += "<th>Opp 3p Makes</th>\n"
    html += "<th>Opp 3p Attempts</th>\n"
    html += "<th>def rebounds</th>\n"
    html += "<th>possible def rebounds\n"
    html += "<th>off rebounds</th>\n"
    html += "<th>possible off rebounds\n"
    html += "<th>Assists</th>\n"
    html += "<th>Turnovers</th>\n"
    html += "<th>Steals</th>\n"
    html += "<th>Blocks</th>\n"
    html += "<th>Fouls Committed</th>\n"
    html += "</tr>\n"

    for lineupTuple in lineupStats:
        if lineupTuple[1].possessionCount > 0:
            html += "<tr>\n"
            html += "<td>" + lineupTuple[0] + "</td>\n"
            html += "<td>" + str(lineupTuple[1].elapsedTime) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].possessionCount) + "</td>\n"            
            html += "<td>" + str(lineupTuple[1].pointsFor) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].pointsAgainst) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].made2pCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].total2pCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].made3pCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].total3pCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].oppMade2pCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].oppTotal2pCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].oppMade3pCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].oppTotal3pCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].defReboundCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].totalDefReboundCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].offReboundCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].totalOffReboundCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].assistCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].turnoverCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].stealsCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].blockCount) + "</td>\n"
            html += "<td>" + str(lineupTuple[1].foulCount) + "</td>\n"
            html += "</tr>\n"

    html += "</table>"        

    file = open("test.html", 'w')
    file.write(html)
    file.close()
    return html

def writeUrlToFile(url, filename):
    page = urllib.urlopen(url)
    contents = page.read()
    if "We're sorry" in contents:
        return
    file = open(filename, 'w')
    file.write(contents)
    file.close()

def formatDateNum(val):
    if val < 10:
        return '0' + str(val)
    return str(val)

#example:
#urlStart = 'http://www.umterps.com/sports/m-baskbl/stats/2012-2013/'
#startDate = datetime.date(2012, 12, 13)
#endDate = datetime.date(2012, 12, 30)
#readGameLogsFromWeb(urlStart, startDate, endDate)
def readGameLogsFromWeb(urlStart, startDate, endDate):
    while startDate < endDate:
        filename = 'md' + formatDateNum(startDate.year - 2000) + formatDateNum(startDate.month) + formatDateNum(startDate.day) + '.html'
        url = urlStart + filename
        writeUrlToFile(url, filename)
        startDate = startDate + datetime.timedelta(1)


def createTeam(name, conference):
    t = Team(name=name, conference=conference)
    t.save()
    return t

def createGame(homeTeam, awayTeam, datePlayed, confGame, neutGame):
    g = Game(homeTeam=homeTeam, awayTeam=awayTeam, date=datePlayed, isConferenceGame=confGame, neutralCourtGame=neutGame)
    g.save()
    return g

def createLineupStatsForGame(game, team, filename):
    lineupData = parseGameLog(filename)
    for (lineup, lineupStats) in lineupData.items():
        lineupStats.lineup = lineup
        lineupStats.game = game
        lineupStats.team = team
        lineupStats.save()

    return lineupData

    
