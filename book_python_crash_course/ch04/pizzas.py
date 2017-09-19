# (1) Trying it yourself - Pizza List

pizzas = []

pizzas.append('pepperoni')
pizzas.append('cheese')
pizzas.append('veggie')

# Using for loop to print the name of each pizza

for pizza in pizzas:
	# print(pizza)
	print('I would really like some ' + pizza.title() + ' right now...')

print('Well, can you tell that I like pizza?')
print('\n')

# (2) Trying it yourself - Animals List

animals = []

animals.append('goose')
animals.append('duck')
animals.append('hawk')

for animal in animals:
	# print(animal)
	print('A ' + animal.title() + " would make a great pet!")
	print('\n')

print('A of the animals have feathers!')