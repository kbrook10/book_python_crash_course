# (9-1) Restaurant
# class Restaurant():
# 	'''Attempt to create a model for a restaurant'''

# 	def __init__(self, restaurant_name, cuisine_type):
# 		'''initialize the restaurant name and cuisine type attributes'''
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type


# 	def describe_restaurant(self):
# 		print("The name of the restaurant is " + self.restaurant_name.title() + ".")
# 		print("The restaurant serves " + self.cuisine_type + " foods.")


# 	def open_restaurant(self):
# 		print(self.restaurant_name.title() + " is now open for business!")



# restaurant = Restaurant("mediterranean grille", "middle eastern")

# print("The name of the restaurant is " + restaurant.restaurant_name.title() + ".")
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
# 		print("The name of the restaurant is " + self.restaurant_name.title() + ".")
# 		print("The restaurant serves " + self.cuisine_type + " foods.")


# 	def open_restaurant(self):
# 		print(self.restaurant_name.title() + " is now open for business!")



# restaurant_0 = Restaurant("mediterranean grille", "middle eastern")
# restaurant_1 = Restaurant("mexican grille", "south american")
# restaurant_2 = Restaurant("siam square", "thai cuisine")

# restaurants = [restaurant_0, restaurant_1, restaurant_2]

# for restaurant in restaurants:	
# 	print("The name of the restaurant is " + restaurant.restaurant_name.title() + ".")
# 	print("The restaurant serves " + restaurant.cuisine_type + " foods.")
# 	restaurant.open_restaurant()
# 	print('\n')

# (9-4) Users
class User():
	'''Attempt to create a model for Users'''
	def __init__(self, first_name, last_name):
		'''Attempt to initialize the first name and last name attributes'''
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		'''Print the users profile information'''
		print("The name of the user is " + self.first_name.title() + ".")
		print("The last name of the user is " + self.last_name.title() + ".")


	def greet_user(self):
		'''Print personal greeting for the user'''
		full_name = self.first_name.title() + ' ' + self.last_name.title()
		print("We are pleased to meet  you, " + full_name)


# Create instances for Users
my_user = User("the world's", "greatest")
your_user = User('janet' , 'jackson')
her_user = User('usher', 'raymond')

users = [my_user, your_user, her_user]

for user in users:
	print(user.describe_user())
	print(user.greet_user())