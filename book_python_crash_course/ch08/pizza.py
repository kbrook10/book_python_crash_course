# (1) Passing arguments to a function parameter without know the amount

# def make_pizza(*toppings):
# 	'''Pirnt the list of toppings that have been requested...'''
# 	print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# (2) Describe the list of toppings on each order
def make_pizza(size, *toppings):
	'''Pirnt the list of toppings that have been requested...'''
	print('\nMaking a ' + str(size) + ' inch pizza with the following ' +
		'toppings: ')
	for topping in toppings:
		print('\t- ' + topping)
