# (1) Create a child class (subclass) from the Car parent class (superclass)

from car import Car

#<------------------------- Completion of Car Class --------------------------->
class Battery():
	'''Attempt to create a representation of a battery'''

	def __init__(self, battery_size=70):
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


#<--------------------- Completion of Battery Class --------------------------->

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


#<----------------- Completion of ElectricCar Class --------------------------->
