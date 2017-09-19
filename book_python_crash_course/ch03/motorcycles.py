# (1) Create a list to add and remove from called motorcycles

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# (2) Modify the list element at position 1

# motorcycles[0] = 'ducati'
# print(motorcycles)
# motorcycles[0] = 'honda'

# (3) Use the Append method to add new element to the end of the list

# motorcycles = []

# print(motorcycles)

# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# motorcycles.append('ducati')

# print(motorcycles)


# (4) Using the insert method to add elements to a list

# motorcycles.insert(0,'ducati')
# print(motorcycles)

# (5) Removing items from a list using the del statement;  This will remove the ducati element at position 1

# del motorcycles[0]
# print(motorcycles)

# (6) Remove elements from the end of a list using the pop method

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# the variable popped_motorcycles stores the popped value from the list
# popped_motorcycles = motorcycles.pop()
# print(popped_motorcycles)

# Use the index of the method pop() to specify the position to remove
# first_owned = motorcycles.pop(0)
# print(motorcycles)
# print(first_owned)

# (7) Removing items by there values

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)

# (8) Try it yourself

people_to_invite_to_dinner = []

people_to_invite_to_dinner.append('Malcolm X')
people_to_invite_to_dinner.append('Tom Hanks')
people_to_invite_to_dinner.append('Jon Stewart')

print(people_to_invite_to_dinner)

message = 'We would like to invite ' + people_to_invite_to_dinner[0] + ' to dinner.'
message2 = 'We would like to invite ' + people_to_invite_to_dinner[1] + ' to dinner.'
message3 = 'We would like to invite ' + people_to_invite_to_dinner[2] + ' to dinner.'

print(message)
print(message2)
print(message3)

cannot_make_dinner = people_to_invite_to_dinner[2]

no_show = cannot_make_dinner + ' can not make the dinner, I\'m sorry'

print(no_show)

people_to_invite_to_dinner.pop(2)
people_to_invite_to_dinner.append('Johnny Quest')
print(people_to_invite_to_dinner)

message = 'We would like to invite ' + people_to_invite_to_dinner[0] + ' to dinner.'
message2 = 'We would like to invite ' + people_to_invite_to_dinner[1] + ' to dinner.'
message3 = 'We would like to invite ' + people_to_invite_to_dinner[2] + ' to dinner.'


print(message)
print(message2)
print(message3)


