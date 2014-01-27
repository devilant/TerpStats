from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from LineupStats.models import *
from LineupStats.LineupFilterForm import *

def index(request):
	context = RequestContext(request)

	games = Game.objects.order_by('-date')
	gamesCount = len(games)
	#get the most recently played game (to show how current the data is)
	latestGame = games[0]
	
	rawLineupData = LineupStats.objects.all()

	#sum the data per-lineup
	totalLineupData = {}
	for lineupStat in rawLineupData:
		lineup = lineupStat.lineup
		if lineup in totalLineupData:
			totalLineupData[lineup] += lineupStat
		else:
			totalLineupData[lineup] = lineupStat

	sortedLineupStats = sorted(totalLineupData.items(), key=lambda statsDict: statsDict[1].elapsedTime)
	sortedLineupStats.reverse()
	lineupStatsList = [lineupStats[1] for lineupStats in sortedLineupStats]

	tableHeaders = ['Lineup', 'Time on Court', 'Possessions', 'Points Per Possession', 'Opponent Points Per Possession', 'Efficiency Margin']
	data = []
	for lineupStats in lineupStatsList:
		dataRow = [lineupStats.lineup, lineupStats.getElapsedTime(), lineupStats.possessionCount, lineupStats.getPointsPerPossession(), lineupStats.getOppPointsPerPossession(), lineupStats.getEfficiencyMargin()]
		data.append(dataRow)		

	context_dict = {'gamesCount': gamesCount,
					'latestGame': latestGame,
					'tableHeaders': tableHeaders,
					'data': data}

	return render_to_response('LineupStats/index.html', context_dict, context)

def about(request):
	context = RequestContext(request)
	return render_to_response('LineupStats/about.html', None, context)

def filter(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = LineupFilterForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('Received form')
	else:
		form = LineupFilterForm()  #new filter form

	context_dict = {'form': form}

	return render_to_response('LineupStats/filter.html', context_dict, context)


