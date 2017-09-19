# (1) Put the first 10 square numbers into a list

squares = []

for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)

# (2) Statistics with list of numbers

numbers = list(range(0,10))

print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# (3) Using list comprehensions to reduce the lines of code to generate a series of numbers

squares2 = [value**2 for value in range(1,11)]
print(squares2)