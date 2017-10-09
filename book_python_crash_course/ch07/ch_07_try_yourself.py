# (7-1) Rental Car Exercise

# prompt = 'To ensure the best service as possible, please provide...'
# prompt += '\nWhat kind of rental car would you like? '

# response = input(prompt)

# feedback = '\nLet me see if we have a ' + response + ' on hand.'
# print(feedback) 


# (7-2) Restaurant Seating

# prompt = 'How many people will be dining with your party this evening? '
# prompt += '\nPlease provide a numerical value...'

# response = input(prompt)
# response = int(response)

# if response > 8:
	# print('\nMy apologies, there will be a short wait for seating.')
# else:
	# print('\nCongratulations, please follow the waiter to your table')


# (7-3) Multiples of Ten

# prompt = 'Welcome to the snake salesman\'s tent...Time to pick a '
# prompt += 'number 1 to 100.\nPick a numerical value between 1 and 100, please '

# response = int(input(prompt))

# if response % 10 == 0:
# 	print('Your value of ' + str(response) + ' is divisble by 10.')
# else:
# 	print('Your value of ' + str(response) + ' is not divisisble by 10, but that is'
# 		  ' ok!')

# (7-4) Pizza Toppings

# prompt = '\nWelcome to Geiko\'s Pizza Palace'
# prompt += '\nPlease enter a series of pizza toppings and enter \'quit\' when '
# prompt += 'finished... '

# toppings = []

# while True:
# 	topping = input(prompt)

# 	if topping == 'quit':
# 		print('Congratulations, you have ordered a pizza with the following')
# 		for topping in toppings:
# 			print('\t' + topping)
# 		break
# 	else:
# 		toppings.append(topping)
# 		print(toppings)


# (7-5) Movie Tickets

prompt = 'Our movie tickets vary depending on your age...'
prompt += '\nWhat is your current age, please... '

age = input(prompt)

while age != quit:
	age = int(age)

	if age != 'quit':

		if age < 3:
			print('There is nothing to pay')
		elif age <= 12:
			print('Please pay $10 dollars')	
		else:
			print('Please pay $15 dollars')
	else:
		break
print('Thank you for coming')		 
