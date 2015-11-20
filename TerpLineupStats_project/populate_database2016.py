from LineupStats.models import *
from TerpStats import *

#create teams
md = createTeam("Maryland", "B10")
msm = createTeam("Mount St. Mary's", "NEC")
gtown = createTeam("Georgetown", "BE")
rider = createTeam("Rider", "MAAC")

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