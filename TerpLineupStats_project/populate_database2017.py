from LineupStats.models import *
from TerpStats import *

md = Team.objects.get(name="Maryland")
american = createTeam("American", "Patriot")