# (1) Using the slice method to select section of a list

players = []

players.append('charles')
players.append('martina')
players.append('michael')
players.append('florence')
players.append('eli')

# The below slice will print the players charles thru michael
print(players[0:3])

# Print the names of the last three plays
print(players[-3:])

# Looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
