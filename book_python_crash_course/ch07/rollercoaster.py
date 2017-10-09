# (1) Using the int() function to convert input() responses to numerical values

height = input('How tall are you, in inches? ')
height = int(height)

if height >= 36:
	print('\nYou\'re tall enough to ride!')
else:
	print('\nYou\'ll be able to ride when you\'re a little older.')