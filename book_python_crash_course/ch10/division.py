# (1) Create a file that generates an zero division error

## Intentionally create ZeroDivisionError
# print(5/0)

## Use the try-except block to handle the ZeroDivisionError
# try:
# 	print(5/0)
# except:
# 	print('You can\'t divide by zero!')


# (2) Create a simple calculator that does division

# print('Provide two values and I\'ll divide them for your')
# print('Whenever you stop feeling froggy press \'q\' to quit')

# while True:
# 	first_number = input('First number: ')
# 	if first_number == 'q':
# 		break
# 	second_number = input('Second number: ')
# 	if second_number == 'q':
# 		break

# 	answer = int(first_number) / int(second_number)
# 	print(answer)

# (3) Create a simple calculator that does division w/ try-except to handle
#     errors

print('Provide two values and I\'ll divide them for your')
print('Whenever you stop feeling froggy press \'q\' to quit')

while True:
	first_number = input('First number: ')
	if first_number == 'q':
		break
	second_number = input('Second number: ')
	if second_number == 'q':
		break

	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print('We cannot divide by 0, silly!')
	else:
		print(answer)