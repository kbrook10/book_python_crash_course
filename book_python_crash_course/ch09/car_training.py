# (1) Create an instance of a car from the class object

# class Car():
# 	'''Attempt to create car model'''


# 	def __init__(self, make, model, year):
# 		'''Initialize the various attributes of the class'''
# 		self.make = make
# 		self.model = model
# 		self.year = year


# 	def get_descriptive_name(self):
# 		'''Return neatly formated name for model'''
# 		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
# 		return long_name.title()


# # Create an instance of the object Car

# my_new_car = Car('audi', 'a4', 2006)
# print(my_new_car.get_descriptive_name())

# (2) Add method to Class with initial default value

class Car():
	'''Attempt to create car model'''


	def __init__(self, make, model, year):
		'''Initialize the various attributes of the class'''
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0


	# Create method to print out car description
	def get_descriptive_name(self):
		'''Return neatly formated name for model'''
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	# Create method to print out the current odometer reading
	def read_odometer(self):
		'''Return the string to read out the current odometer'''
		if self.odometer_reading <= 0:
			print("This car has " + str(self.odometer_reading) + 
				" miles on it.")
		else:
			print("This car now has " + str(self.odometer_reading) + 
				" miles on it.")


	# Create method to update the odometer reading
	def update_odometer(self, mileage):
		'''Update odometer to a given value'''
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print('You cannot roll back the odometer!')

	# Create method to increment odometer reading
	def incremet_odometer(self, miles):
		'''Update miles via increments'''
		if miles >= 0:
			self.odometer_reading += miles
		else: 
			print("mileage cannot be decremented")


# Create an instance of the object Car

# my_new_car = Car('audi', 'a4', 2006)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.odometer_reading = 23
# my_new_car.update_odometer(-10)
# my_new_car.read_odometer()

# (2) Create instance for used car
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

# Update odometer via the class method
my_used_car.update_odometer(23500)
my_used_car.read_odometer()

# Update the odometer via the class method increment
my_used_car.incremet_odometer(-100)
my_used_car.read_odometer()


