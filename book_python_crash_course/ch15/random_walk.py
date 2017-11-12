# (1) Create program to generate a random walk

## Import required modules/ functions
from random import choice

## Create class to intialize
class RandomWalk():
	'''Class to generate a random walk'''

	def __init__(self, num_points=5000):
		'''Initialized attributes of walk'''

		self.num_points = num_points

		## Ensure all walks start at point (0,0)
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		'''Calculate all points of the walk'''

		## Keep taking steps until the walk has reached the desired length
		while len(self.x_values) < self.num_points:

			## Decide what direction to take and how far in direction
			x_direction = choice([1,-1])
			x_distance = choice([0,1,2,3,4])
			x_step = x_direction * x_distance

			y_direction = choice([1,-1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_direction * y_distance

			## Only take steps that go somewhere, reject others
			if (x_step == 0) and (y_step == 0):
				continue

			## Calculate next x- and y- values
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			## Add steps to list
			self.x_values.append(next_x)
			self.y_values.append(next_y)			