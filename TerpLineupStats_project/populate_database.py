from LineupStats.models import *
from TerpStats import *

#create teams
md = createTeam("Maryland", "ACC")
uconn = createTeam("Connecticut", "AAC")
abc = createTeam("Abilene Christian", "Southland")
oregonst = createTeam("Oregon State", "P12")
marist = createTeam("Marist", "MAAC")
niowa = createTeam("Northern Iowa", "MVC")
prov = createTeam("Providence", "BE")
morganst = createTeam("Morgan State", "MEAC")
ohiost = createTeam("Ohio State", "B10")
gw = createTeam("George Washington", "A10")
bc = createTeam("Boston College", "ACC")
flaatl = createTeam("Florida Atlantic", "CUSA")
bostonu = createTeam("Boston University", "Pat")
tulsa = createTeam("Tulsa". "CUSA")
nccent = createTeam("North Carolina Central", "MEAC")
gatech = createTeam("Georgia Tech", "ACC")
pitt = createTeam("Pittsburgh", "ACC")
flast = createTeam("Florida State", "ACC")
notredame = createTeam("Notre Dame", "ACC")
ncst = createTeam("North Carolina State", "ACC")
miami = createTeam("Miami", "ACC")
vatech = createTeam("Virginia Tech", "ACC")
unc = createTeam("North Carolina", "ACC")
uva = createTeam("Virginia", "ACC")

#uconn game
date = datetime.datetime(2013, 11, 8, 18, 30)
game = createGame(md, uconn, date, False, True)
createLineupStatsForGame(game, md, "terps2013-2014/uconn.html")

#abilene christian game
date = datetime.datetime(2013, 11, 13, 19)
game = createGame(md, abc, date, False, False)
createLineupStatsForGame(game, md, "terps2013-2014/abilenechristian.html")

#oregon state game
date = datetime.datetime(2013, 11, 17, 18)
game = createGame(md, oregonst, date, False, False)
createLineupStatsForGame(game, md, "terps2013-2014/oregonstate.html")

#marist game
date = datetime.datetime(2013, 11, 22, 16)
game = createGame(md, marist, date, False, True)
createLineupStatsForGame(game, md, "terps2013-2014/marist.html")

#northern iowa game
date = datetime.datetime(2013, 11, 24, 19)
game = createGame(md, niowa, date, False, True)
createLineupStatsForGame(game, md, "terps2013-2014/northerniowa.html")

#providence game
date = datetime.datetime(2013, 11, 25, 22)
game = createGame(md, prov, date, False, True)
createLineupStatsForGame(game, md, "terps2013-2014/providence.html")

#morgan state game
date = datetime.datetime(2013, 11, 29, 18)
game = createGame(md, morganst, date, False, False)
createLineupStatsForGame(game, md, "terps2013-2014/morganstate.html")

#ohio state game
date = datetime.datetime(2013, 12, 4, 19)
game = createGame(ohiost, md, date, False, False)
createLineupStatsForGame(game, md, "terps2013-2014/ohiostate.html")

#george washington game
date = datetime.datetime(2013, 12, 8, 15, 30)
game = createGame(md, gw, date, False, True)
createLineupStatsForGame(game, md, "terps2013-2014/georgewashington.html")

#boston college game
date = datetime.datetime(2013, 12, 12, 19)
game = createGame(bc, md, date, True, False)
createLineupStatsForGame(game, md, "terps2013-2014/bostoncollege-away.html")

#florida atlantic game
date = datetime.datetime(2013, 12, 14, 14)
game = createGame(md, flaatl, date, False, False)
createLineupStatsForGame(game, md, "terps2013-2014/floridaatlantic.html")

#boston university game
date = datetime.datetime(2013, 12, 21, 13)
game = createGame(md, bostonu, date, False, False)
createLineupStatsForGame(game, md, "terps2013-2014/bostonuniversity.html")

#tulsa game
date = datetime.datetime(2013, 12, 29, 19)
game = createGame(md, tulsa, date, False, False)
createLineupStatsForGame(game, md, "terps2013-2014/tulsa.html")

#north carolina central game
date = datetime.datetime(2013, 12, 31, 14, 30)
game = createGame(md, nccent, date, False, False)
createLineupStatsForGame(game, md, "terps2013-2014/northcarolinacentral.html")

#georgia tech home game
date = datetime.datetime(2014, 1, 4, 14)
game = createGame(md, gatech, date, True, False)
createLineupStatsForGame(game, md, "terps2013-2014/georgiatech-home.html")

#pittsburgh away game
date = datetime.datetime(2014, 1, 6, 19)
game = createGame(pitt, md, date, True, False)
createLineupStatsForGame(game, md, "terps2013-2014/pittsburgh-away.html")

#florida state away game
date = datetime.datetime(2014, 1, 12, 20)
game = createGame(flast, md, date, True, False)
createLineupStatsForGame(game, md, "terps2013-2014/floridastate-away.html")

#notre dame home game
date = datetime.datetime(2014, 1, 15, 19)
game = createGame(md, notredame, date, True, False)
createLineupStatsForGame(game, md, "terps2013-2014/notredame-home.html")

#nc state away game
date = datetime.datetime(2014, 1, 20, 21)
game = createGame(ncst, md, date, True, False)
createLineupStatsForGame(game, md, "terps2013-2014/ncstate-away.html")

#miami home game
date = datetime.datetime(2014, 1, 29, 21)
game = createGame(md, miami, date, True, False)
createLineupStatsForGame(game, md, "terps2013-2014/miami-home.html")

#virginia tech home game
date = datetime.datetime(2014, 2, 1, 12)
game = createGame(md, vatech, date, True, False)
createLineupStatsForGame(game, md, "terps2013-2014/virginiatech-home.html")

#unc away game
date = datetime.datetime(2014, 2, 4, 20)
game = createGame(unc, md, date, True, False)
createLineupStatsForGame(game, md, "terps2013-2014/NorthCarolina-away.html")

#uva away game
date = datetime.datetime(2014, 2, 10, 21)
game = createGame(uva, md, date, True, False)
createLineupStatsForGame(game, md, "terps2013-2014/virginia-away.html")
