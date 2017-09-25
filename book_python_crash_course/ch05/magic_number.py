# (1) Testing for two numbers not equal to one another

answer = 17

if answer != 42:
	print('That is not the correct answer. Please try again!')

# (2) Using And to check for multiple conditions -> Results to True b/c
#     both of the tests pass

age_0 = 22
age_1 = 24

print((age_0 >= 21) and (age_1 >= 21))

# (3) Using Or to check for multiple conditions -> Results to True b/c at least
#     one of the tests passes

age_0 = 22
age_1 = 18

print((age_0 >= 21) or (age_1 >= 21))

# (4) Test if item is in list using the keyword 'in'

print('Start of test using the keyword in...')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

