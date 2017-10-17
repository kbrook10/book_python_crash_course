# (1) Create simple greeting function

# def greet_user():
# 	"""Display message to greet new user"""
# 	print('Hello, it is a pleasure to meet you!')


# # Call Function to run code
# greet_user()

# (2) Print the specific users name

def greet_user():
	'''Display message to greet specific user'''
	username = input('\nWhat is your name, please? ')
	print('Hello ' + username.title() + ', it is a pleasure to meet you!')

greet_user()