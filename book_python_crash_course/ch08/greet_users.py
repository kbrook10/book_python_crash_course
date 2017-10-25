# (1) Send lists to functions
def greet_users(names):
	'''Print a simple greeting for the users in a list'''
	for name in names:
		msg = 'Hello, ' + name.title() + '!'
		print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
