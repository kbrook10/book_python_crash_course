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
# class User():
# 	'''Attempt to create a model for Users'''
# 	def __init__(self, first_name, last_name):
# 		'''Attempt to initialize the first name and last name attributes'''
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.login_attempts = 0

# 	def describe_user(self):
# 		'''Print the users profile information'''
# 		print("The name of the user is " + self.first_name.title() + ".")
# 		print("The last name of the user is " + self.last_name.title() + ".")


# 	def greet_user(self):
# 		'''Print personal greeting for the user'''
# 		print("We are pleased to meet  you, " + self.first_name.title() + ' ' + 
# 			self.last_name.title())


# 	def increment_login_attempts(self):
# 		'''Create method to track the amount of login attemps'''
# 		self.login_attempts += 1



# 	def reset_login_attempts(self):
# 		'''Create method to resets login attemps back to zero'''
# 		self.login_attempts = 0

# # Create instances for Users
# your_user = User('janet' , 'jackson')
# attempts = 0

# for i in range(1,5):
# 	your_user.increment_login_attempts()
# 	print("User attempt count is currently " + str(i) + " attempts.")
# 	attempts = i

# print("User currently has made " + str(attempts) + "  attempts...")
# print("Reset the user attempts after call with tech support")
# your_user.reset_login_attempts()
# print(your_user.login_attempts)


# (9-6) Ice Cream Stand
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


# #<------------------------- Completion of Parent Class ------------------->
# class IceCreamStand(Restaurant):
# 	'''Attempt to create representation of IceCreamStand from Parent Class'''


# 	def __init__(self,restaurant_name, cuisine_type):
# 		'''Initiate the child class with the parent attributes and methods'''
# 		super().__init__(restaurant_name, cuisine_type)
# 		self.flavors = ['vanilla', 'chocolate', 'strawberry']
# 		# self.flavors = []



# 	def display_flavors(self):
# 		'''Create method to display flavors'''
# 		if self.flavors:
# 			print('Which of the following flavors would you like? ')
# 			for self.flavor in self.flavors:
# 				print('\t - ' + self.flavor)
# 		else:
# 			print('It appears we have ran out of flavors')


# #<------------------------- Completion of Child Class --------------------->
# kims_ice_cream = IceCreamStand("cool treats", "ice cream")
# kims_ice_cream.describe_restaurant()
# kims_ice_cream.display_flavors()


# (9-7 & 9-8) Admin.
# class User():
# 	'''Attempt to create a model for Users'''
# 	def __init__(self, first_name, last_name):
# 		'''Attempt to initialize the first name and last name attributes'''
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.login_attempts = 0

# 	def describe_user(self):
# 		'''Print the users profile information'''
# 		print("The name of the user is " + self.first_name.title() + ".")
# 		print("The last name of the user is " + self.last_name.title() + ".")


# 	def greet_user(self):
# 		'''Print personal greeting for the user'''
# 		print("We are pleased to meet  you, " + self.first_name.title() + ' ' + 
# 			self.last_name.title())


# 	def increment_login_attempts(self):
# 		'''Create method to track the amount of login attemps'''
# 		self.login_attempts += 1



# 	def reset_login_attempts(self):
# 		'''Create method to resets login attemps back to zero'''
# 		self.login_attempts = 0

# #<------------------------- Completion of Parent Class ------------------->
# class Privileges():
# 	'''Create representation of Privileges to separate out child attributes'''


# 	def __init__(self):
# 		'''Initiate attributes for the child class attribute'''
# 		self.privileges = [
# 				'can add post',
# 				'can delete post',
# 				'can ban user'
# 		]


# 	def show_privileges(self):
# 		'''Create function to display privileges of Admin. User'''
# 		if self.privileges:
# 			print('The Admin users has the following privileges: ')
# 			for privilege in self.privileges:
# 				print('\t - ' + privilege)

# #<-------------------- Completion of Child Attribute Class --------------->
# class Admin(User):
# 	'''Create representation of Admin from parent class User'''


# 	def __init__(self, first_name, last_name):
# 		'''Initiate child class with parent attributes'''
# 		super().__init__(first_name, last_name)
# 		self.privileges = Privileges()

# #<------------------------- Completion of Child Class --------------------->

# # Create instances for Admin child class
# principal = Admin('leroy' , 'brown')
# principal.describe_user()
# principal.greet_user()
# principal.privileges.show_privileges()


# (9-8) Privileges
# See Above...


# (9-10) Battery Upgrade
# class Car():
# 	'''Attempt to create a model of a car'''

# 	def __init__(self, make, model, year):
# 		'''Create the initial attributes (i.e. properties) for the car class'''
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odometer_reading = 0 # Create initial value
# 		self.gas_tank = 30 # Create initial value


# 	def get_descriptive_name(self):
# 		'''Create method to provide neatly formatted string'''
# 		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
# 		return long_name # Returns the value to the call function



# 	def read_odometer(self):
# 		'''Create method to read current value of odometer'''
# 		print('This car has ' + str(self.odometer_reading) + ' ' + 'miles on ' +
# 			'it.')


# 	def update_odometer(self, mileage):
# 		'''Create method to update the value of the odometer'''
# 		if mileage >= 0:
# 			self.odometer_reading = mileage
# 		else:
# 			print('You can\'t roll back an odometer!')


# 	def increment_odometer(self, miles):
# 		'''Create method to increase odometer value by constant'''
# 		self.odometer_reading += miles



# 	# Example of overriding the parent method
# 	def fill_gas_tank(self):
# 		print('The vehicle currently has ' + str(self.gas_tank) + ' gallon '
# 			+ 'tank.')

# #<------------------------- Completion of Parent Class ------------------->
# class Battery():
# 	'''Attempt to create a representation of a battery'''

# 	def __init__(self, battery_size=70):
# 		'''Initialize the attributes for the Battery Class'''
# 		self.battery_size = battery_size



# 	def describe_battery(self):
# 		'''Create method to describe the size of the battery'''
# 		print('This car has a ' + str(self.battery_size) + ' -kWh battery.')



# 	def get_range(self):
# 		'''Create method to display range based on battery size'''
# 		if self.battery_size == 70:
# 			range = 240
# 		elif self.battery_size == 85:
# 			range = 270

# 		message = 'This car has an approximate range of ' + str(range)
# 		message += ' miles on a full charge'
# 		print(message)


# 	def update_battery(self):
# 		'''Create method to update battery specs'''
# 		if self.battery_size != 85:
# 			self.battery_size = 85

	

# #<------------------------- Completion of Battery Class ------------------->
# class ElectricCar(Car):
# 	'''Attempt to create representation of Electric Car from Car super class'''

# 	def __init__(self, make, model, year):
# 		'''initialize attributes from parent class'''
# 		super().__init__(make, model, year)
# 		# self.battery_size = 70
# 		self.battery = Battery()


# 	def fill_gas_tank(self):
# 		'''Create method to override the parent method'''
# 		print('Electric cars do not have a need for a gas tank.')

# # Generate description of child class from parent class
# my_tesla = ElectricCar('tesla', 'model 3', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# print('\nUpdating the battery specs...')
# my_tesla.battery.update_battery()
# my_tesla.battery.get_range()

# (9-10) - Imported Restaurant
# import restaurant

# kims_ice_cream = restaurant.Restaurant("cool treats", "ice cream")
# kims_ice_cream.describe_restaurant()


# (9-11) - Imported Admin
# from user_module import User, Admin, Privileges

# # Create instances for Admin child class
# principal = Admin('leroy' , 'brown')
# principal.describe_user()
# principal.greet_user() 
# principal.privileges.show_privileges()


# (9-12) - Multiple Modules
# from user_module import User
# from admin import Privileges, Admin

# # Create instances for Admin child class
# principal = Admin('leroy' , 'brown')
# principal.describe_user()
# principal.greet_user() 
# principal.privileges.show_privileges()

# (9-13) OrderedDict Rewrite
##skipped


# (9-14) Dice
from random import randint

class Die():
	'''Create represenation of die'''


	def __init__(self, sides=6):
		'''Initialize the class with attributes'''
		self.sides = sides
		self.repeat = 10



	def roll_die(self):
		'''Create representation for rolling dice'''
		x = randint(1, self.sides)
		print(x)



	def repeat_dice_roll(self, repeat):
		'''Create repeat function for dice roll'''
		for i in range(0, repeat):
			self.roll_die()

	# def update_sides(self, sides):
	# 	'''Update the sides of the dice'''
	# 	self.sides = sides


# six_side_dice = Die(6)
# print(six_side_dice.sides)
# six_side_dice.repeat_dice_roll()
# ten_side_dice = Die(10)
# ten_side_dice.update_sides(10)
# print(ten_side_dice.sides)
# ten_side_dice.repeat_dice_roll(5)
twenty_side_dice = Die(20)
# twenty_side_dice.update_sides(20)
# print(twenty_side_dice.sides)
twenty_side_dice.repeat_dice_roll(2)


# (9-15) Python Module of the Week


