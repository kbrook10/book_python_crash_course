# (1) Creating a Dictionary to fill with user input

# Set active flag and empty dictionary to trigger loop
responses = {}
polling_active = True

# Create while loop to obtain user input and cont. until no more feedback

while polling_active:
	# Prompt for username and travel location
	name = input('\nWhat is your name? ')
	response = input('Where would you love to travel? ')

	# Update dictionary with username and response
	responses[name] = response

	# Identify if further users want to be polled
	repeat = input('Would another like to take the poll? (y/n) ')
	if repeat == 'n':
		polling_active = False

# Once Polling is complete show results

print('\n---Poll Results---')
for name, response in responses.items():
	print(name.title() + ' would love to travel to ' + response + ' one day.')