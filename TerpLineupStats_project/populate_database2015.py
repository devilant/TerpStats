from LineupStats.models import *
from TerpStats import *

md = Team.objects.get(name="Maryland")

#create team
iowast = createTeam("Iowa State", "B12")
arizonast = createTeam("Arizona State", "P12")
wagner = createTeam("Wagner", "NE")
monmouth = createTeam("Monmouth", "MAAC")
uscupstate = createTeam("USC Upstate", "ASun")
vmi = createTeam("VMI", "Southern")
virginia = Team.objects.get(name="Virginia")
okst = createTeam("Oklahoma St", "B12")
michst = createTeam("Michigan St", "B10")
minnesota = createTeam("Minnesota", "B10")
illinois = createTeam("Illinois", "B10")
purdue = createTeam("Purdue", "B10")
rutgers = createTeam("Rutgers", "B10")
indiana = createTeam("Indiana", "B10")
northwestern = createTeam("Northwestern", "B10")
ohiost = Team.objects.get(name="Ohio State")
pennst = createTeam("Penn State", "B10")
nebraska = createTeam("Nebraska", "B10")
wisconsin = createTeam("Wisconsin", "B10")
michigan = createTeam("Michigan", "B10")
valparaiso = createTeam("Valparaiso", "Horizon")
westvirginia = createTeam("West Virginia", "B12")

#wagner game
date = datetime.datetime(2014, 11, 14, 19, 30)
game = createGame(md, wagner, date, False, False)
createLineupStatsForGame(game, md, 'terps2014-2015/wagner.html')

#arizona state game
date = datetime.datetime(2014, 11, 24, 19, 0)
game = createGame(md, arizonast, date, False, True)
createLineupStatsForGame(game, md, 'terps2014-2015/arizonastate.html')

#iowa state game
date = datetime.datetime(2014, 11, 25, 21, 30)
game = createGame(md, iowast, date, False, True)
createLineupStatsForGame(game, md, 'terps2014-2015/iowastate.html')

#monmouth game
date = datetime.datetime(2014, 11, 28, 19, 0)
game = createGame(md, monmouth, date, False, False)
createLineupStatsForGame(game, md, 'terps2014-2015/monmouth.html')

#vmi game
date = datetime.datetime(2014, 11, 30, 18, 0)
game = createGame(md, vmi, date, False, False)
createLineupStatsForGame(game, md, 'terps2014-2015/vmi.html')

#virginia game
date = datetime.datetime(2014, 12, 3, 21, 15)
game = createGame(md, virginia, date, False, False)
createLineupStatsForGame(game, md, 'terps2014-2015/virginia.html')

#usc upstate game
date = datetime.datetime(2014, 12, 13, 11, 0)
game = createGame(md, uscupstate, date, False, False)
createLineupStatsForGame(game, md, 'terps2014-2015/uscupstate.html')

#okst game
date = datetime.datetime(2014, 12, 21, 14, 0)
game = createGame(okst, md, date, False, False)
createLineupStatsForGame(game, md, 'terps2014-2015/okst-away.html')

#mich st away game
date = datetime.datetime(2014, 12, 30, 17, 0)
game = createGame(michst, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/michiganst-away.html')

#minnesota home game
date = datetime.datetime(2015, 1, 3, 12, 0)
game = createGame(md, minnesota, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/minnesota.html')

#illinois away game
date = datetime.datetime(2015, 1, 7, 21, 0)
game = createGame(illinois, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/illinois-away.html')

#purdue away game
date = datetime.datetime(2015, 1, 10, 14, 30)
game = createGame(purdue, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/purdue-away.html')

#rutgers home game
date = datetime.datetime(2015, 1, 14, 19, 0)
game = createGame(md, rutgers, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/rutgers.html')

#michiganst home game
date = datetime.datetime(2015, 1, 17, 16, 0)
game = createGame(md, michst, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/michiganst.html')

#indiana away game
date = datetime.datetime(2015, 1, 22, 21, 0)
game = createGame(indiana, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/indiana-away.html')

#northwestern home game
date = datetime.datetime(2015, 1, 25, 19, 30)
game = createGame(md, northwestern, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/northwestern.html')

#ohio st away game
date = datetime.datetime(2015, 1, 29, 19, 0)
game = createGame(ohiost, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/ohiost-away.html')

#penn st home game
date = datetime.datetime(2015, 2, 4, 20, 30)
game = createGame(md, pennst, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/pennstate.html')

#indiana home game
date = datetime.datetime(2015, 2, 11, 18, 0)
game = createGame(md, indiana, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/indiana.html')

#penn st away game
date = datetime.datetime(2015, 2, 14, 17, 30)
game = createGame(pennst, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/pennstate-away.html')

#nebraska home game
date = datetime.datetime(2015, 2, 19, 19, 0)
game = createGame(md, nebraska, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/nebraska.html')

#wisconsin home game
date = datetime.datetime(2015, 2, 24, 19, 0)
game = createGame(md, wisconsin, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/wisconsin.html')

#michigan home game
date = datetime.datetime(2015, 2, 28, 12, 0)
game = createGame(md, michigan, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/michigan.html')

#rutgers away game
date = datetime.datetime(2015, 3, 3, 19, 0)
game = createGame(rutgers, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/rutgers-away.html')

#nebraska away game
date = datetime.datetime(2015, 3, 8, 19, 30)
game = createGame(nebraska, md, date, True, False)
createLineupStatsForGame(game, md, 'terps2014-2015/nebraska-away.html')

#indiana big 10 tournament game
date = datetime.datetime(2015, 3, 13, 18, 30)
game = createGame(md, indiana, date, True, True)
createLineupStatsForGame(game, md, 'terps2014-2015/indiana-tournament.html')

#michigan state big 10 tournament game
date = datetime.datetime(2015, 3, 14, 15, 30)
game = createGame(md, michiganst, date, True, True)
createLineupStatsForGame(game, md, 'terps2014-2015/michiganst-tournament.html')

#valparaiso ncaa first round game
date = datetime.datetime(2015, 3, 20, 16, 40)
game = createGame(md, valparaiso, date, False, True)
createLineupStatsForGame(game, md, 'terps2014-2015/valparaiso.html')

#west virginia ncaa round of 32 game
date = datetime.datetime(2015, 3, 22, 20, 40)
game = createGame(md, westvirginia, date, False, True)
createLineupStatsForGame(game, md, 'terps2014-2015/westvirginia.html')