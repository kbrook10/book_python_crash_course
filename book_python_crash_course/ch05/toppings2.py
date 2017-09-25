# (1) Looping through list of toppings to check if match

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
					  'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# requested_toppings = []

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
	    print('Adding ' + requested_topping + '.')
	else:
		print('Sorry, we are out of ' + requested_topping + ' right now.')

print('\nFinished making your pizza!')