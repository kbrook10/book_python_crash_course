# (1) Creating a list in a dictionary

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
}

# # Summarize the order

print( 'You ordered ' + pizza['crust'].title() + '-crust pizza ' + 
	   'with the following toppings:')

for topping in pizza['toppings']:
	print('\t' + topping)