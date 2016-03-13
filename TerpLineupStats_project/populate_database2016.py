from LineupStats.models import *
from TerpStats import *

#create teams
md = createTeam("Maryland", "B10")
msm = createTeam("Mount St. Mary's", "NEC")
gtown = createTeam("Georgetown", "BE")
rider = createTeam("Rider", "MAAC")
illst = createTeam("Illinois State", "MVC")
rhodeisland = createTeam("Rhode Island", "A10")
clevelandst = createTeam("Cleveland State", "Horizon")
northcarolina = Team.objects.get(name="North Carolina")
connecticut = Team.objects.get(name="Connecticut")
umes = createTeam("Maryland Eastern Shore", "MEAC")
princeton = createTeam("Princeton", "Ivy")
marshall = createTeam("Marshall", "CUSA")
pennst = Team.objects.get(name="Penn State")
northwestern = Team.objects.get(name="Northwestern")
rutgers = Team.objects.get(name="Rutgers")
wisconsin = Team.objects.get(name="Wisconsin")
michigan = Team.objects.get(name="Michigan")
ohiost = Team.objects.get(name="Ohio State")
michst = Team.objects.get(name="Michigan St")
iowa = createTeam("Iowa", "B10")
nebraska = Team.objects.get(name="Nebraska")
purdue = Team.objects.get(name="Purdue")
minnesota = Team.objects.get(name="Minnesota")
illinois = Team.objects.get(name="Illinois")
indiana = Team.objects.get(name="Indiana")

#mount st. mary's game
date = datetime.datetime(2015, 11, 13, 19, 0)
game = createGame(md, msm, date, False, False)
createLineupStatsForGame(game, md, 'terps2015-2016/mountstmarys.html')

#georgetown game
date = datetime.datetime(2015, 11, 17, 21, 0)
game = createGame(md, gtown, date, False, False)
createLineupStatsForGame(game, md, 'terps2015-2016/georgetown.html')

#rider game
date = datetime.datetime(2015, 11, 20, 19, 0)
game = createGame(md, rider, date, False, False)
createLineupStatsForGame(game, md, 'terps2015-2016/rider.html')

#illinois state game
date = datetime.datetime(2015, 11, 24, 20, 30)
game = createGame(md, illst, date, False, True)
createLineupStatsForGame(game, md, 'terps2015-2016/illinoisst.html')

#rhode island game
date = datetime.datetime(2015, 11, 25, 20, 30)
game = createGame(md, rhodeisland, date, False, True)
createLineupStatsForGame(game, md, 'terps2015-2016/rhodeisland.html')

#cleveland st game
date = datetime.datetime(2015, 11, 28, 19, 30)
game = createGame(md, clevelandst, date, False, False)
createLineupStatsForGame(game, md, 'terps2015-2016/clevelandst.html')

#north carolina game
date = datetime.datetime(2015, 12, 1, 21, 30)
game = createGame(northcarolina, md, date, False, False)
createLineupStatsForGame(game, md, 'terps2015-2016/northcarolina.html')

#connecticut game
date = datetime.datetime(2015, 12, 8, 21, 30)
game = createGame(md, connecticut, date, False, True)
createLineupStatsForGame(game, md, 'terps2015-2016/connecticut.html')

#maryland eastern shore game
date = datetime.datetime(2015, 12, 12, 16, 15)
game = createGame(md, umes, date, False, False)
createLineupStatsForGame(game, md, 'terps2015-2016/marylandeasternshore.html')

#princeton game
date = datetime.datetime(2015, 12, 19, 19, 0)
game = createGame(md, princeton, date, False, True)
createLineupStatsForGame(game, md, 'terps2015-2016/princeton.html')

#marshall game
date = datetime.datetime(2015, 12, 27, 16, 0)
game = createGame(md, marshall, date, False, False)
createLineupStatsForGame(game, md 'terps2015-2016/marshall.html')

#penn st home game
date = datetime.datetime(2015, 12, 30, 17, 0)
game = createGame(md, pennst, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/pennst.html')

#northwestern road game
date = datetime.datetime(2016, 1, 2, 20, 0)
game = createGame(northwestern, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/northwestern-away.html')

#rutgers game
date = datetime.datetime(2016, 1, 6, 19, 0)
game = createGame(md, rutgers, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/rutgers.html')

#wisconsin away game
date = datetime.datetime(2016, 1, 9, 13, 0)
game = createGame(wisconsin, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/wisconsin-away.html')

#michigan away game
date = datetime.datetime(2016, 1, 12, 21, 0)
game = createGame(michigan, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/michigan-away.html')

#ohio st home game
date = datetime.datetime(2016, 1, 16, 12, 0)
game = createGame(md, ohiost, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/ohiost.html')

#northwestern home game
date = datetime.datetime(2016, 1, 19, 20, 0)
game = createGame(md, northwestern, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/northwestern.html')

#michigan state away game
date = datetime.datetime(2016, 1, 23, 18, 30)
game = createGame(michst, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/michiganst-away.html')

#iowa home game
date = datetime.datetime(2016, 1, 28, 19, 0)
game = createGame(md, iowa, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/iowa.html')

#ohio state away game
date = datetime.datetime(2016, 1, 31, 13, 0)
game = createGame(ohiost, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/ohiost-away.html')

#nebraska away game
date = datetime.datetime(2016, 2, 3, 20, 30)
game = createGame(nebraska, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/nebraska-away.html')

#purdue home game
date = datetime.datetime(2016, 2, 6, 16, 0)
game = createGame(md, purdue, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/purdue.html')

#wisconsin home game
date = datetime.datetime(2016, 2, 13, 18, 30)
game = createGame(md, wisconsin, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/wisconsin.html')

#minnesota away game
date = datetime.datetime(2016, 2, 18, 20, 0)
game = createGame(minnesota, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/minnesota-away.html')

#michigan home game
date = datetime.datetime(2016, 2, 21, 13, 0)
game = createGame(md, michigan, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/michigan.html')

#purdue away game
date = datetime.datetime(2016, 2, 27, 16, 0)
game = createGame(purdue, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/purdue-away.html')

#illinois home game
date = datetime.datetime(2016, 3, 3, 19, 0)
game = createGame(md, illinois, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/illinois.html')

#indiana away game
date = datetime.datetime(2016, 3, 6, 16, 30)
game = createGame(indiana, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2015-2016/indiana-away.html')

#nebraska big ten tournament game
date = datetime.datetime(2016, 3, 11, 21, 0)
game = createGame(md, nebraska, date, True, True)
createLineupStatsForGame(game, md, 'terps2015-2016/nebraska-tournament.html')

#michigan st big ten tournament game
date = datetime.datetime(2016, 3, 12, 15, 30)
game = createGame(md, michst, date, True, True)
createLineupStatsForGame(game, md, 'terps2015-2016/michiganst-tournament.htnl')