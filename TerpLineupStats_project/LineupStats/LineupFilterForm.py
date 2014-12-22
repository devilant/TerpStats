from django import forms

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

	gameTypes = (
		('All Games', 'All Games'),
		('Conference Games Only', 'Conference Games Only'),
		('Nonconference Games Only', 'Nonconference Games Only'),
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
	gameType = forms.ChoiceField(
		choices = gameTypes,
		label="Show lineups for this game type:")
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

		self.fields["includePlayers"].choices = players
		self.fields["excludePlayers"].choices = players