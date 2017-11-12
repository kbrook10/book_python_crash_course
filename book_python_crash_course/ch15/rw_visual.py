# (1) Create a visual of the random walk
import matplotlib.pyplot as plt
from random_walk import RandomWalk

## Make random walk and plot the points
while True:
	rw = RandomWalk()
	rw.fill_walk()

	# Set plot window size
	plt.figure(dpi= 128, figsize=(10,6))

	## Plot the points
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
			edgecolor='none', s=15)
	plt.scatter(0,0, c='green', edgecolor='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)
	plt.show()


	# Cleaning up the Axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	## Control active status of program
	keep_running = input('Make another walk? (y/n): ')
	if keep_running == 'n':
		break