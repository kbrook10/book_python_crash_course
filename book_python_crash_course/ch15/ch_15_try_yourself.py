# (15-1) Cubes
import matplotlib.pyplot as plt

## Define values for 1st 5 cubics
# x_values = [1,2,3,4,5]

## Define values for 5000 cubics
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=5)

## Set the Chart Title and labels
plt.title('Cubic Numbers', fontsize=24)
plt.xlabel('Values', fontsize=14)
plt.ylabel('Cubes of the Values', fontsize=14)

## Set the styling for the tick marks
plt.tick_params(axis='both', which='major', labelsize=14)

## Set range for axes
plt.axis([0,5.5e3,0,1.5e11])

## Display chart
# plt.show()

## Save file
plt.savefig('cubic_values.png', bbox_inches='tight')


# (15-2) Colored Cubes