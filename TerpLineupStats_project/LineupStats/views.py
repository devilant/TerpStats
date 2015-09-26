from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from LineupStats.models import *
from LineupStats.LineupFilterForm import *

def index(request, season):
	context = RequestContext(request)

	if season == '':
		season = "2015"

	includePlayers = []
	excludePlayers = []
	minimumPossessions = 0
	statsToShow = ['Time on Court', 'Possessions', 'Points Per Possession', 'Opponent Points Per Possession', 'Efficiency Margin']
	includeFilterString = ""
	excludeFilterString = ""
	possessionFilterString = ""
	conferenceFilter = "All Games"
	conferenceFilterString = ""
	gameFilter = ""
	gameFilterString = ""
	if request.method == 'POST':
		form = LineupFilterForm(season, request.POST)
		if form.is_valid():
			includePlayers = form.cleaned_data['includePlayers']
			excludePlayers = form.cleaned_data['excludePlayers']
			minimumPossessions = form.cleaned_data['minimumPossessions']
			statsToShow = form.cleaned_data['statsToShow']
			includeFilterString = playerFilterToString(includePlayers, True)
			excludeFilterString = playerFilterToString(excludePlayers, False)
			conferenceFilter = form.cleaned_data['gameType']	
			if conferenceFilter == 'Conference Games Only' or conferenceFilter == 'Nonconference Games Only':
				conferenceFilterString = conferenceFilter
			elif conferenceFilter != 'All Games':
				gameFilter = conferenceFilter
				gameFilterString = str(Game.objects.get(id=gameFilter))
			if minimumPossessions > 0:
				possessionFilterString = "Lineups that played at least " + str(minimumPossessions) + " possessions"
		else:
			return HttpResponse('Error: Invalid filter settings')

	statsToShow.insert(0, "Lineup")
	seasonStartDate = getSeasonStartDate(season)
	seasonEndDate = getSeasonEndDate(season)
	games = Game.objects.filter(date__lte=seasonEndDate, date__gte=seasonStartDate).order_by('-date')
	gamesCount = len(games)
	#get the most recently played game (to show how current the data is)
	if gamesCount > 0:
		latestGame = games[0]
	else:
		latestGame = None
	
	rawLineupData = LineupStats.objects.filter(game__date__lte=seasonEndDate, game__date__gte=seasonStartDate)

	#sum the data per-lineup
	totalLineupData = {}
	for lineupStat in rawLineupData:
		lineup = lineupStat.lineup
		isConferenceGame = lineupStat.game.isConferenceGame
		if conferenceFilterString == 'Conference Games Only':
			if not isConferenceGame:
				continue
		elif conferenceFilterString == 'Nonconference Games Only':
			if isConferenceGame:
				continue
		if gameFilter:
			if str(lineupStat.game.id) != gameFilter:
				continue
		if lineup in totalLineupData:
			totalLineupData[lineup] += lineupStat
		else:
			totalLineupData[lineup] = lineupStat

	sortedLineupStats = sorted(totalLineupData.items(), key=lambda statsDict: statsDict[1].elapsedTime)
	sortedLineupStats.reverse()
	lineupStatsList = [lineupStats[1] for lineupStats in sortedLineupStats]

	data = []
	allLineups = LineupStats()
	allLineups.lineup = "All Lineups"
	for lineupStats in lineupStatsList:
		#apply filters
		if lineupStats.possessionCount < minimumPossessions:
			continue
		filter = True
		for includePlayer in includePlayers:
			print ('Checking if' + includePlayer + ' in ' + lineupStats.lineup)
			if includePlayer not in lineupStats.lineup:
				filter = False
		if not filter:
			continue
		for excludePlayer in excludePlayers:
			if excludePlayer in lineupStats.lineup:
				filter = False
		if not filter:
			continue

		allLineups += lineupStats
		dataRow = getDataRow(lineupStats, statsToShow)
		data.append(dataRow)		
	#add a row for the combined sum of all the lineups
	dataRow = getDataRow(allLineups, statsToShow)
	data.insert(0, dataRow)

	context_dict = {'gamesCount': gamesCount,
					'latestGame': latestGame,
					'tableHeaders': statsToShow,
					'data': data,
					'season': season,
					'includePlayers': includePlayers,
					'excludePlayers': excludePlayers,
					'minimumPossessions': minimumPossessions,
					'includeFilterString' : includeFilterString,
					'excludeFilterString' : excludeFilterString,
					'possessionFilterString' : possessionFilterString,
					'conferenceFilterString' : conferenceFilterString,
					'gameFilterString' : gameFilterString}

	return render_to_response('LineupStats/index.html', context_dict, context)

def getSeasonStartDate(season):
	if season == '2014':
		return '2013-10-01'
	if season == '2015':
		return '2014-10-01'
	if season == '2016':
		return '2015-10-01'
	return '2014-10-01'

def getSeasonEndDate(season):
	if season == '2014':
		return '2014-05-01'
	if season == '2015':
		return '2015-05-01'
	if season == '2016':
		return '2016-05-01'
	return '2015-05-01'

def getDataRow(lineupStat, statsToShow):
	dataRow = []
	for stat in statsToShow:
		if stat == "Lineup":
			dataRow.append(lineupStat.lineup)
		if stat == "Time on Court":
			dataRow.append(lineupStat.getElapsedTime())
		if stat == "Possessions":
			dataRow.append(lineupStat.possessionCount)
		if stat == "Points Per Possession":
			dataRow.append(lineupStat.getPointsPerPossession())
		if stat == "Opponent Points Per Possession":
			dataRow.append(lineupStat.getOppPointsPerPossession())
		if stat == "Efficiency Margin":
			dataRow.append(lineupStat.getEfficiencyMargin())
		if stat == "2p%":
			dataRow.append(lineupStat.get2pPercentage())
		if stat == "3p%":
			dataRow.append(lineupStat.get3pPercentage())
		if stat == "Opp 2p%":
			dataRow.append(lineupStat.getOpp2pPercentage())
		if stat == "Opp 3p%":
			dataRow.append(lineupStat.getOpp3pPercentage())
		if stat == "Def Reb %":
			dataRow.append(lineupStat.getDefReboundPercentage())
		if stat == "Off Reb %":
			dataRow.append(lineupStat.getOffReboundPercentage())
		if stat == "Steal %":
			dataRow.append(lineupStat.getStealPercentage())
		if stat == "Assist %":
			dataRow.append(lineupStat.getAssistPercentage())
		if stat == "Turnover %":
			dataRow.append(lineupStat.getTurnoverPercentage())

	return dataRow

def playerFilterToString(players, isInclude):
	if isInclude:
		conj = "and "
	else:
		conj = "or "
	outputString = ""
	if len(players) < 1:
		return ""
	if len(players) == 1:
		outputString = players[0]
	else:
		for player in players[:-1]:
			outputString += player
			if len(players) > 2:
				outputString += ","
			outputString += " "
		outputString += conj + players[-1]

	if isInclude:
		return "Lineups that contain " + outputString
	else:
		return "Lineups that do not contain " + outputString

def about(request):
	context = RequestContext(request)
	return render_to_response('LineupStats/about.html', None, context)

def filter(request, season):
	context = RequestContext(request)

	if request.method == 'POST':
		form = LineupFilterForm(season, request.POST)
		if form.is_valid():
			return index(request, season)
	else:
		form = LineupFilterForm(season)  #new filter form
	
	context_dict = {'form': form,
					'season': season}

	return render_to_response('LineupStats/filter.html', context_dict, context)


