from LineupStats.models import *
from TerpStats import *

#create teams
md = createTeam("Maryland", "B10")
msm = createTeam("Mount St. Mary's", "NEC")

#mount st. mary's game
date = datetime.datetime(2015, 11, 13, 19, 0)
game = createGame(md, msm, date, False, False)
createLineupStatsForGame(game, md, 'terps2015-2016/mountstmarys.html')