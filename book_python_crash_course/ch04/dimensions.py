# (1) Use tuples to create an immutable (i.e. can not change list items)

dimensions = (200, 50)

print(dimensions[0])
print(dimensions[-1])

# (2) Try to change an element in the list

# dimensions[0] = 250

# print('\nNew list item at position 1')
# print(dimensions[0])

# (3) Writing over a Tuple

dimensions = (400, 100)

print(dimensions[0])
print(dimensions[-1])

# (4) Try it yourself

# (4-13) Buffet -> 5 basic foods

basic_foods = ('collard greens', 'tomato', 'apple', 'carrots', 'orange')

# Print all foods in the tuple
for food in basic_foods:
	print(food)

# Create error and try to reassign a value within the tuple
# basic_foods[0] = 'mushrooms'

# Rewrite the Tuple

basic_foods = ('green beans', 'tomato', 'apple', 'carrots', 'strawberries')

for food in basic_foods:
	print(food)
