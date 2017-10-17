# (1) Remove all instances of a value from a list

pets = ['dog', 'cat', 'bird', 'dog', 'cat', 'rabbit']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)