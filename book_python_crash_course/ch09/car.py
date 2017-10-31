'''A class that can be used to create a car'''

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
		if self.odometer_reading < 0:
			print('It seems that the odometer is misreading')
		elif self.odometer_reading == 0:
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


