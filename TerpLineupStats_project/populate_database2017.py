from LineupStats.models import *
from TerpStats import *

md = Team.objects.get(name="Maryland")
american = createTeam("American", "Patriot")
georgetown = Team.objects.get(name="Georgetown")

#american game
date = datetime.datetime(2016, 11, 11, 19, 0)
game = createGame(md, american, date, False, False)
createLineupStatsForGame(game, md, 'terps2016-2017/american.html')

#georgetown game
date = datetime.datetime(2016, 11, 16, 18, 30)
game = createGame(georgetown, md, date, False, False)
createLineupStatsForGame(game, md, 'terps2016-2017/georgetown.html')