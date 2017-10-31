# (1) Create a child class (subclass) from the Car parent class (superclass)

class Car():
	'''Attempt to create a model of a car'''

	def __init__(self, make, model, year):
		'''Create the initial attributes (i.e. properties) for the car class'''
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0 # Create initial value
		self.gas_tank = 30


	def get_descriptive_name(self):
		'''Create method to provide neatly formatted string'''
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name # Returns the value to the call function



	def read_odometer(self):
		'''Create method to read current value of odometer'''
		print('This car has ' + str(self.odometer_reading) + ' ' + 'miles on ' +
			'it.')


	def update_odometer(self, mileage):
		'''Create method to update the value of the odometer'''
		if mileage >= 0:
			self.odometer_reading = mileage
		else:
			print('You can\'t roll back an odometer!')


	def increment_odometer(self, miles):
		'''Create method to increase odometer value by constant'''
		self.odometer_reading += miles



	# Example of overriding the parent method
	def fill_gas_tank(self):
		print('The vehicle currently has ' + str(self.gas_tank) + ' gallon '
			+ 'tank.')

#<------------------------- Completion of Parent Class ------------------->
class Battery():
	'''Attempt to create a representation of a battery'''

	def __init__(self, battery_size=85):
		'''Initialize the attributes for the Battery Class'''
		self.battery_size = battery_size



	def describe_battery(self):
		'''Create method to describe the size of the battery'''
		print('This car has a ' + str(self.battery_size) + ' -kWh battery.')



	def get_range(self):
		'''Create method to display range based on battery size'''
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = 'This car has an approximate range of ' + str(range)
		message += ' miles on a full charge'
		print(message)
	

#<------------------------- Completion of Battery Class ------------------->
class ElectricCar(Car):
	'''Attempt to create representation of Electric Car from Car super class'''

	def __init__(self, make, model, year):
		'''initialize attributes from parent class'''
		super().__init__(make, model, year)
		# self.battery_size = 70
		self.battery = Battery()


	def fill_gas_tank(self):
		'''Create method to override the parent method'''
		print('Electric cars do not have a need for a gas tank.')

# Generate description of child class from parent class
my_tesla = ElectricCar('tesla', 'model 3', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
my_tesla.battery.get_range()