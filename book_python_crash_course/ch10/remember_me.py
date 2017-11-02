# (1) Create program to remember username
# import json

# ## Define initial variables for program
# filename = 'username.json'

# try:
# 	## Read file and print username
# 	with open(filename, 'r') as f_obj:
# 		username = json.load(f_obj)
# except FileNotFoundError:
# 	## Write username to file
# 	w_username = input('What is your name, please? ')
# 	with open(filename, 'w') as f_obj:
# 		json.dump(w_username, f_obj)
# 		print('We will remember you when you come back ' + username + '!')
# else:
# 	print('Welcome back, ' + username)


# (2) Refactor code
import json

def get_stored_username():
	'''Obtain stored user name'''
	filename = 'username.json'

	try:
		with open(filename, 'r') as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	'''Create new username'''
	username = input('What is your name? ')
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	'''Create function to greet the user by name'''

	username = get_stored_username()

	if username:
		print('Welcome back, ' + username)
	else:
		username = get_new_username()
		print('We will remember you next time, ' + username + '.')

greet_user()



