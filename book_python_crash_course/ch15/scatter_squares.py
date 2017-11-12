# (1) Styling single data plot points
import matplotlib.pyplot as plt

## Define individual point to plot
# plt.scatter(2,4, s=200)

## Define series of points to plot
# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]

## Automate list creation
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values,edgecolor='none', c=y_values, cmap=plt.cm.Blues,
			 s=5)

## Style the Chart title and labels
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Values', fontsize=14)

## Set the size of the tick marks
plt.tick_params(axis='both', which='major', labelsize=14)

## Set the axis ranges
plt.axis([0,1100,0,1100000])

## Display plot
# plt.show()
plt.savefig('squares_test_plot.png', bbox_inches='tight')
