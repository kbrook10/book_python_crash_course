class User():
	'''Attempt to create a model for Users'''
	def __init__(self, first_name, last_name):
		'''Attempt to initialize the first name and last name attributes'''
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		'''Print the users profile information'''
		print("The name of the user is " + self.first_name.title() + ".")
		print("The last name of the user is " + self.last_name.title() + ".")


	def greet_user(self):
		'''Print personal greeting for the user'''
		print("We are pleased to meet  you, " + self.first_name.title() + ' ' + 
			self.last_name.title())


	def increment_login_attempts(self):
		'''Create method to track the amount of login attemps'''
		self.login_attempts += 1



	def reset_login_attempts(self):
		'''Create method to resets login attemps back to zero'''
		self.login_attempts = 0

