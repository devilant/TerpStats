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