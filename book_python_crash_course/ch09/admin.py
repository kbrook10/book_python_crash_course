from user_module import User

#<------------------------- Completion of Parent Class ------------------->
class Privileges():
	'''Create representation of Privileges to separate out child attributes'''


	def __init__(self):
		'''Initiate attributes for the child class attribute'''
		self.privileges = [
				'can add post',
				'can delete post',
				'can ban user'
		]


	def show_privileges(self):
		'''Create function to display privileges of Admin. User'''
		if self.privileges:
			print('The Admin users has the following privileges: ')
			for privilege in self.privileges:
				print('\t - ' + privilege)

#<-------------------- Completion of Child Attribute Class --------------->
class Admin(User):
	'''Create representation of Admin from parent class User'''


	def __init__(self, first_name, last_name):
		'''Initiate child class with parent attributes'''
		super().__init__(first_name, last_name)
		self.privileges = Privileges()

#<------------------------- Completion of Child Class --------------------->