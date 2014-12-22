from LineupStats.models import *
from TerpStats import *

md = Team.objects.get(name="Maryland")

#create team
wagner = createTeam("Wagner", "NE")

#wagner game
date = datetime.datetime(2014, 11, 14, 19, 30)
game = createGame(md, wagner, date, False, False)
createLineupStatsForGame(game, md, 'terps2014-2015/wagner.html')
