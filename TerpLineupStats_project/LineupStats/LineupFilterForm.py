from django import forms
from LineupStats.models import *
import views

class LineupFilterForm(forms.Form):

	players2013_2014 = (
		('A.J. Metz', 'A.J. Metz'),
		('Charles Mitchell', 'Charles Mitchell'),
		('Connor Lipinski', 'Connor Lipinski'),
		('Damonte Dodd', 'Damonte Dodd'),
		('Dez Wells', 'Dez Wells'),
		('Evan Smotrycz', 'Evan Smotrycz'),
		('Jacob Susskind', 'Jacob Susskind'),
		('Jake Layman', 'Jake Layman'),
		('John Auslander', 'John Auslander'),
		('Jonathan Graham', 'Jonathan Graham'),
	 	('Nick Faust', 'Nick Faust'),
	 	('Roddy Peters', 'Roddy Peters'),
	 	('Seth Allen', 'Seth Allen'),
	 	('Shaquille Cleare', 'Shaquille Cleare'),
	 	('Spencer Barks', 'Spencer Barks'),
	 	('Varun Ram', 'Varun Ram'),	 	
	 	)

	players2014_2015 = (		
		('Damonte Dodd', 'Damonte Dodd'),
		('Dez Wells', 'Dez Wells'),
		('Dion Wiley', 'Dion Wiley'),
		('Evan Smotrycz', 'Evan Smotrycz'),
		('Jacob Susskind', 'Jacob Susskind'),
		('Jake Layman', 'Jake Layman'),
		('Jared Nickens', 'Jared Nickens'),
		('Jon Graham', 'Jon Graham'),
		('Melo Trimble', 'Melo Trimble'),
		('Michal Cekovsky', 'Michal Cekovsky'),
		('Richaud Pack', 'Richaud Pack'),
		('Spencer Barks', 'Spencer Barks'),
		('Trevor Anzmann', 'Trevor Anzmann'),
		('Varun Ram', 'Varun Ram'),
		)

	players2015_2016 = (
		('Andrew Terrell', 'Andrew Terrell'),
		('Damonte Dodd', 'Damonte Dodd'),
		('Diamond Stone', 'Diamond Stone'),
		('Dion Wiley', 'Dion Wiley'),
		('Ivan Bender', 'Ivan Bender'),
		('Jake Layman', 'Jake Layman'),
		('Jared Nickens', 'Jared Nickens'),
		('Jaylen Brantley', 'Jaylen Brantley'),
		('Kent Auslander', 'Kent Auslander'),
		('Michal Cekovsky', 'Michal Cekovsky'),
		('Melo Trimble', 'Melo Trimble'),
		('Rasheed Sulaimon', 'Rasheed Sulaimon'),
		('Robert Carter', 'Robert Carter'),
		('Trevor Anzmann', 'Trevor Anzmann'),
		('Varun Ram', 'Varun Ram'),
		)

	players2016_2017 = (
		('Andrew Terrell', 'Andrew Terrell'),
		('Anthony Cowan', 'Anthony Cowan'),
		('Damonte Dodd', 'Damonte Dodd'),
		('Dion Wiley', 'Dion Wiley'),
		('Ivan Bender', 'Ivan Bender'),
		('Jared Nickens', 'Jared Nickens'),
		('Jaylen Brantley', 'Jaylen Brantley'),
		('Joshua Tomaic', 'Joshua Tomaic'),
		('Justin Jackson', 'Justin Jackson'),
		('Kent Auslander', 'Kent Auslander'),
		('Kevin Huerter', 'Kevin Huerter'),
		('L.G. Gill', 'L.G. Gill'),
		('Melo Trimble', 'Melo Trimble'),
		('Micah Thomas', 'Micah Thomas'),
		('Michal Cekovsky', 'Michal Cekovsky'),
		('Travis Valmon', 'Travis Valmon'),
		)

	players2017_2018 = (
		('Alex Tostado', 'Alex Tostado'),
		('Andrew Terrell', 'Andrew Terrell'),
		('Anthony Cowan', 'Anthony Cowan'),
		('Bruno Fernando', 'Bruno Fernando'),
		('Darryl Morsell', 'Darryl Morsell'),
		('Dion Wiley', 'Dion Wiley'),
		('Ivan Bender', 'Ivan Bender'),
		('Jared Nickens', 'Jared Nickens'),
		('Joshua Tomaic', 'Joshua Tomaic'),
		('Justin Jackson', 'Justin Jackson'),
		('Kevin Huerter', 'Kevin Huerter'),
		('Michal Cekovsky', 'Michal Cekovsky'),
		('Reese Mona', 'Reese Mona'),
		('Sean Obi', 'Sean Obi'),
		('Travis Valmon', 'Travis Valmon'),
		)

	gameTypes = (
		('All Games', 'All Games'),
		)

	confGameTypes = (
		('All Games', 'All Games'),
		('Conference Games Only', 'Conference Games Only'),
		('Nonconference Games Only', 'Nonconference Games Only'),
		)

	homeAwayTypes = (
		('All Games', 'All Games'),
		('Home Games Only', 'Home Games Only'),
		('Away Games Only', 'Away Games Only'),
		('Neutral Court Games Only', 'Neutral Court Games Only')
		)

	statTypes = (
		('Time on Court', 'Time on Court'),
		('Possessions', 'Possessions'),
		('Points Per Possession', 'Points Per Possession'),
		('Opponent Points Per Possession', 'Opponent Points Per Possession'),
		('Efficiency Margin', 'Efficiency Margin'),
		('2p%', '2p%'),
		('3p%', '3p%'),
		('Opp 2p%', 'Opp 2p%'),
		('Opp 3p%', 'Opp 3p%'),
		('Def Reb %', 'Def Reb %'),
		('Off Reb %', 'Off Reb %'),
		('Steal %', 'Steal %'),
		('Assist %', 'Assist %'),
		('Turnover %', 'Turnover %'),		
		)
	initialStatTypes= ['Time on Court', 'Possessions', 'Points Per Possession', 'Opponent Points Per Possession', 'Efficiency Margin']

	includePlayers = forms.MultipleChoiceField(
		widget=forms.CheckboxSelectMultiple, 
		choices = (),
		required=False,
		label='Show lineups that include these selected players:')
	excludePlayers = forms.MultipleChoiceField(
		widget=forms.CheckboxSelectMultiple, 
		choices = (),
		required=False,
		label='Show lineups excluding these selected players:')
	conferenceGameType = forms.ChoiceField(
		choices = confGameTypes,
		label = "Show lineups for conference or nonconference games:")
	homeAwayGameType = forms.ChoiceField(
		choices = homeAwayTypes,
		label = "Show lineups for home or away games:")
	gameType = forms.ChoiceField(
		choices = gameTypes,
		label="Show lineups for a particular game:")
	minimumPossessions = forms.IntegerField(
		min_value=0,
		max_value=1000,
		initial=0,
		label='Show only lineups that have played at least this many possessions:')
	statsToShow = forms.MultipleChoiceField(
		widget=forms.CheckboxSelectMultiple,
		choices = statTypes,
		required=True,
		initial=initialStatTypes,
		label='Select the statistics to show:')

	def __init__(self, season='2014', *args, **kwargs):
		super(LineupFilterForm, self).__init__(*args, **kwargs)
		players = self.players2013_2014
		if season == '2014':
			players = self.players2013_2014
		if season == '2015':
			players = self.players2014_2015
		if season == '2016':
			players = self.players2015_2016
		if season == '2017':
			players = self.players2016_2017
		if season == '2018':
			players = self.players2017_2018

		seasonStartDate =  views.getSeasonStartDate(season)
		seasonEndDate = views.getSeasonEndDate(season)
		games = Game.objects.filter(date__lte=seasonEndDate, date__gte=seasonStartDate).order_by('date')
		gameTypes = self.gameTypes
		confGameTypes = self.confGameTypes
		homeAwayTypes = self.homeAwayTypes
		for game in games:
			gameTypes += ((game.id, str(game)),)
		self.fields["gameType"].choices = gameTypes
		self.fields["conferenceGameType"].choices = confGameTypes
		self.fields["homeAwayGameType"].choices = homeAwayTypes
		self.fields["includePlayers"].choices = players
		self.fields["excludePlayers"].choices = players