# (1) Create program to call name function based on user input...

## Import name function
from name_function import get_formatted_name

## Request user first and last name

print('Feel free to enter \'q\' to quit at any time.')

while True:
	first = input('Please give your first name. ')
	if first == 'q':
		break

	last = input('Please give your last name. ')
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print('\tNeatly formatted name: ' + formatted_name + '.')