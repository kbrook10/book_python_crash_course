class Restaurant():
	'''Attempt to create a model for a restaurant'''

	def __init__(self, restaurant_name, cuisine_type):
		'''initialize the restaurant name and cuisine type attributes'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0


	def describe_restaurant(self):
		print("The name of the restaurant is " + self.restaurant_name.title() + 
			".")
		print("The restaurant serves " + self.cuisine_type + " foods.")
		print("The restaurant has served over " + str(self.number_served) +
			" this year.")


	def open_restaurant(self):
		print(self.restaurant_name.title() + " is now open for business!")


	def set_number_served(self, num_serv):
		'''Create method to update the number of people served'''
		if num_serv >= 0:
			self.number_served = num_serv
		else:
			print("The number served cannot be decremented")


	def read_number_served(self):
		'''Create method to read current number served'''
		if self.number_served >= 0:
			print("The restaurant has now served over " + str(self.number_served) +
			" this year.")
		else:
			print("The number served cannot be decremented")


	def increment_number_served(self):
		'''Create method to updates the average daily customers served'''
		self.number_served += 100


#<------------------------- Completion of Parent Class ------------------->
class IceCreamStand(Restaurant):
	'''Attempt to create representation of IceCreamStand from Parent Class'''


	def __init__(self,restaurant_name, cuisine_type):
		'''Initiate the child class with the parent attributes and methods'''
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['vanilla', 'chocolate', 'strawberry']
		# self.flavors = []



	def display_flavors(self):
		'''Create method to display flavors'''
		if self.flavors:
			print('Which of the following flavors would you like? ')
			for self.flavor in self.flavors:
				print('\t - ' + self.flavor)
		else:
			print('It appears we have ran out of flavors')


#<------------------------- Completion of Child Class --------------------->
