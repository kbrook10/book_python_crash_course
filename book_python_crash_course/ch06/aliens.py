# (1) Make a list of aliens in which each alien is a dictionary of information
#     about that alien.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

print('\n')
# (2) Use the range() method to create a fleet of aliens

# # Make an empty list to hold the aliens
aliens = []

# # Make 15 yellow aliens
for alien_number in range(15):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# # Alter a slice of the aliens group created

	for alien in aliens[0:3]:
		if alien['color'] == 'green':
			alien['color'] = 'yellow'
			alien['speed'] = 'medium'
			alien['points'] = 10
		elif alien['color'] == 'yellow':
			alien['color'] = 'red'
			alien['speed'] = 'fast'
			alien['points'] = 15


# # Show the first 5 aliens
for alien in aliens[:5]:
	print(alien)
print('...')

# # Display how many aliens have been created
print('Total number of aliens: ' + str(len(aliens)))


