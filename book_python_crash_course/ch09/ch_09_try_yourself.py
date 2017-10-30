# (9-1) Restaurant
# class Restaurant():
# 	'''Attempt to create a model for a restaurant'''

# 	def __init__(self, restaurant_name, cuisine_type):
# 		'''initialize the restaurant name and cuisine type attributes'''
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type


# 	def describe_restaurant(self):
# 		print("The name of the restaurant is " + self.restaurant_name.title() + 
#		".")
# 		print("The restaurant serves " + self.cuisine_type + " foods.")


# 	def open_restaurant(self):
# 		print(self.restaurant_name.title() + " is now open for business!")



# restaurant = Restaurant("mediterranean grille", "middle eastern")

# print("The name of the restaurant is " + restaurant.restaurant_name.title() + 
#		".")
# print("The restaurant serves " + restaurant.cuisine_type + " foods.")
# restaurant.open_restaurant()

# (9-2) Three Restaurant
# class Restaurant():
# 	'''Attempt to create a model for a restaurant'''

# 	def __init__(self, restaurant_name, cuisine_type):
# 		'''initialize the restaurant name and cuisine type attributes'''
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type


# 	def describe_restaurant(self):
# 		print("The name of the restaurant is " + self.restaurant_name.title() + 
#		".")
# 		print("The restaurant serves " + self.cuisine_type + " foods.")


# 	def open_restaurant(self):
# 		print(self.restaurant_name.title() + " is now open for business!")



# restaurant_0 = Restaurant("mediterranean grille", "middle eastern")
# restaurant_1 = Restaurant("mexican grille", "south american")
# restaurant_2 = Restaurant("siam square", "thai cuisine")

# restaurants = [restaurant_0, restaurant_1, restaurant_2]

# for restaurant in restaurants:	
# 	print("The name of the restaurant is " + restaurant.restaurant_name.title() 
#	+ ".")
# 	print("The restaurant serves " + restaurant.cuisine_type + " foods.")
# 	restaurant.open_restaurant()
# 	print('\n')

# (9-3) Users
# class User():
# 	'''Attempt to create a model for Users'''
# 	def __init__(self, first_name, last_name):
# 		'''Attempt to initialize the first name and last name attributes'''
# 		self.first_name = first_name
# 		self.last_name = last_name

# 	def describe_user(self):
# 		'''Print the users profile information'''
# 		print("The name of the user is " + self.first_name.title() + ".")
# 		print("The last name of the user is " + self.last_name.title() + ".")


# 	def greet_user(self):
# 		'''Print personal greeting for the user'''
# 		print("We are pleased to meet  you, " + self.first_name.title() + ' ' + 
# 			self.last_name.title())

# # Create instances for Users
# my_user = User("the world's", "greatest")
# your_user = User('janet' , 'jackson')
# her_user = User('usher', 'raymond')

# users = [my_user, your_user, her_user]

# for user in users:
# 	print(user.describe_user())
# 	print(user.greet_user())
# 	print('\n')


# (9-4)  Number Served:
# class Restaurant():
# 	'''Attempt to create a model for a restaurant'''

# 	def __init__(self, restaurant_name, cuisine_type):
# 		'''initialize the restaurant name and cuisine type attributes'''
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type
# 		self.number_served = 0


# 	def describe_restaurant(self):
# 		print("The name of the restaurant is " + self.restaurant_name.title() + 
# 			".")
# 		print("The restaurant serves " + self.cuisine_type + " foods.")
# 		print("The restaurant has served over " + str(self.number_served) +
# 			" this year.")


# 	def open_restaurant(self):
# 		print(self.restaurant_name.title() + " is now open for business!")


# 	def set_number_served(self, num_serv):
# 		'''Create method to update the number of people served'''
# 		if num_serv >= 0:
# 			self.number_served = num_serv
# 		else:
# 			print("The number served cannot be decremented")


# 	def read_number_served(self):
# 		'''Create method to read current number served'''
# 		if self.number_served >= 0:
# 			print("The restaurant has now served over " + str(self.number_served) +
# 			" this year.")
# 		else:
# 			print("The number served cannot be decremented")


# 	def increment_number_served(self):
# 		'''Create method to updates the average daily customers served'''
# 		self.number_served += 100




# restaurant = Restaurant("mediterranean grille", "middle eastern")

# restaurant.describe_restaurant()
# restaurant.set_number_served(50)
# restaurant.read_number_served()
# restaurant.increment_number_served()
# print("At the end of the day...")
# restaurant.read_number_served()


# (9-5) Login Attempts:
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

# Create instances for Users
your_user = User('janet' , 'jackson')
attempts = 0

for i in range(1,5):
	your_user.increment_login_attempts()
	print("User attempt count is currently " + str(i) + " attempts.")
	attempts = i

print("User currently has made " + str(attempts) + "  attempts...")
print("Reset the user attempts after call with tech support")
your_user.reset_login_attempts()
print(your_user.login_attempts)

