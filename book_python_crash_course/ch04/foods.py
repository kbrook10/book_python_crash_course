# (1) Use slice to copy lists
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(list(my_foods))

print("\nMy friend's favorite foods are:")
print(friend_foods)

# (2) Try yourself --->

# (4-10) Slices
players = []

players.append('charles')
players.append('martina')
players.append('michael')
players.append('florence')
players.append('eli')

print('The first three items in the list are: \n' + str(players[:3]) +'\n')
print('The middle three items in the list are: \n' + str(players[1:4]) +'\n')
print('The last three items in the list are: \n' + str(players[-3:]) + '\n')


# (4-11) My Pizzas, Your Pizza


# (4-12) More Loops
print('\n')
print('My favorite foods are')
for food in my_foods:
	print(food)

print('\n')

print('My friends favorite foods are')
for food in friend_foods:
	print(food)