# (1) Create simple program to read user name

# def get_formatted_name(first, last):
# 	'''Neatly format users full name'''

# 	full_name = first + ' ' + last
# 	return full_name.title()


# (2) Break the function to test it out...

def get_formatted_name(first, last, middle=''):
	'''Neatly format users full name'''

	# full_name = first + ' ' + last
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()