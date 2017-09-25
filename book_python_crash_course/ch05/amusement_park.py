# (1) Using if-elif-else chain to test for multiple conditions

age = 12

if age < 4:
	print('Your admission cost is $0.')
elif age < 18:
	print('Your admission cost is $5.')
else:
	print('Your admission cost is $10.')

# (2) Using if-elif-else chain to test for multiple conditions, while using
#     efficiencies

age = 55

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
elif age >= 65:
	price = 5

print('Your admission cost is $' + str(price) + '.')
