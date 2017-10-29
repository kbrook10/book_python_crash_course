# Developing classes and generating instances of those classes

class Dog():
	'''An attempt to model man's best friend'''

	def __init__(self, name, age):
		'''Initialize attributes name and age'''
		self.name = name
		self.age = age


	def sit(self):
		'''Simulate method for dog sitting'''
		print(self.name.title() + ' is now sitting')


	def roll_over(self):
		'''Simulate method for dog rolling over'''
		print(self.name.title() + ' is rolling over')

# (2) Create Instance of dog
## Create instance of a dog name willie of age 6
my_dog = Dog('willie', 6)
# my_dog.sit()
# my_dog.roll_over()

## Print details of dog
# print('My dog\'s name is ' + my_dog.name.title() + '!')
# print('My dog is ' + str(my_dog.age) + ' years old!')

# (3) Creating multiple instances
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old")
your_dog.sit()
