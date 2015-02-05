from LineupStats.models import *
from TerpStats import *

md = Team.objects.get(name="Maryland")

#create team
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

#wagner game
date = datetime.datetime(2014, 11, 14, 19, 30)
game = createGame(md, wagner, date, False, False)
createLineupStatsForGame(game, md, 'terps2014-2015/wagner.html')

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