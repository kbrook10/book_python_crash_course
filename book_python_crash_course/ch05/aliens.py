# (1) Try Yourself

# (5-3) Alien Colors

alien_color = 'green'

if alien_color == 'yellow':
	points = 10
if alien_color == 'red':
	points = 15
if alien_color == 'green':
	points = 5
print('Alien color is ' + alien_color + '.' + ' Great Job! You just earned ' + str(points) + ' points.')

# (5-4) stage of life

age = 45

if age < 2:
	title = 'baby'
if age < 4:
	title = 'toddler'
if age < 13:
	title = 'kid'
if age < 20:
	title = 'teenager'
if age < 65:
	title = 'adult'
if age >= 65:
	title = 'elder'


print('Congratulations, you are a ' + title)


# (5-7) Check if favorite fruit is in list

favorite_fruits = ['bananas', 'apples', 'oranges']

print('grapes' in favorite_fruits)

if 'bananas' in favorite_fruits:
	print('You really like bananas')
if 'apples' in favorite_fruits:
	print('You really like apples')
if 'tomato' in favorite_fruits:
	print('You really like tomatoes')
if 'blueberries' in favorite_fruits:
	print('You really like blueberries')
if 'oranges' in favorite_fruits:
	print('You really like oranges')