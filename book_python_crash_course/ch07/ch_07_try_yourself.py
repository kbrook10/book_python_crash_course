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

# prompt = 'Our movie tickets vary depending on your age...'
# prompt += '\nWhat is your current age, please... '

# age = input(prompt)

# while age != quit:
# 	age = int(age)

# 	if age != 'quit':

# 		if age < 3:
# 			print('There is nothing to pay')
# 		elif age <= 12:
# 			print('Please pay $10 dollars')	
# 		else:
# 			print('Please pay $15 dollars')
# 	else:
# 		break
# print('Thank you for coming')	

# (7-8) Deli

# Create a list of sandwiches and an empty list of finised sandwiches
# sandwich_orders = ['reuben', 'pastrami', 'blt', 'pastrami', 'turkey', 'roast beef', 'pastrami']
# finished_sandwiches = []

# Suggest the deli is out of pastrami and remove all instances from sandwich 
# orders

# print('\nOur apologies, but we are out of pastrami')
# while 'pastrami' in sandwich_orders:
# 	sandwich_orders.remove('pastrami')

# print(sandwich_orders)

# # Loop through list of sandwich orders and print out each and move to finished

# while sandwich_orders:
# 	# Obtain the last sandwich from the list to work on
# 	current_sandwich = sandwich_orders.pop()

# 	# Create message that we are working on sandwich then add to finished list
# 	print('\nWe are currently working on the ' + current_sandwich + ' sandwich.')
# 	finished_sandwiches.append(current_sandwich)

# # Display list of all finished sandwiches

# print('\nThe following sandwiches have now been completed...')
# for sandwich in finished_sandwiches:
# 	print('\t' + sandwich.title())

# print(sandwich_orders)


# (7-9) No Pastrami

# Code Above...


# (7-10) Dream Vacation	

# Poll users about there dream vacation

# Create dictionary to obtain name of user and their response...
# Create flag to trigger loop to end
responses = {}
polling_active = True

# Create loop to request user input

while polling_active:
    # Create prompt for user name and dream vacation
    name = input('\nWhat is your name? ')
    response = input('If you could go anywhere in the world, where would ' + 
    	            'it be? ')

    # Add response to dictionary
    responses[name] = response

    # Identify if further users would like to participate in poll
    repeat_poll = input('\nWould anyone else like to participate? (y/n) ')
    if repeat_poll == 'n':
        polling_active = False

# Display the final Polling Results
print('\n---Polling Results---')
for name, response in responses.items():
    print(name.title() + ' would love to take an adventure to ' 
        + response.title() + ' some day.')

