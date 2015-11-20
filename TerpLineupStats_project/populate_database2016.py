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