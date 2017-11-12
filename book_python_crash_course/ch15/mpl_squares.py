# (1) Practice using the matplotlib library to generate visual
import matplotlib.pyplot as plt

## Create test data to display visual
input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

## Set Chart title and label axes
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Values', fontsize=14)

## Set the size and style of the tick marks
plt.tick_params(axis='both', labelsize=14)

## Display graph
plt.show()