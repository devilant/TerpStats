from django import forms

class LineupFilterForm(forms.Form):
	players = (
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
		choices = players,
		required=False,
		label='Show lineups that include these selected players:')
	excludePlayers = forms.MultipleChoiceField(
		widget=forms.CheckboxSelectMultiple, 
		choices = players,
		required=False,
		label='Show lineups excluding these selected players:')
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