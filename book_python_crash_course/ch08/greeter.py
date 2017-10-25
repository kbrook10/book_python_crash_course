# (1) Create simple greeting function

# def greet_user():
# 	"""Display message to greet new user"""
# 	print('Hello, it is a pleasure to meet you!')


# # Call Function to run code
# greet_user()

# (2) Print the specific users name

# def greet_user():
# 	'''Display message to greet specific user'''
# 	username = input('\nWhat is your name, please? ')
# 	print('Hello ' + username.title() + ', it is a pleasure to meet you!')

# greet_user()

# (3) Using a function with a while loop

def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

# create while loop
while True:
    print('\nPlease tell me your name: ')
    print('(enter \'q\' at any time to quit)')

    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break

formatted_name = get_formatted_name(f_name, l_name)
print('\nHello, ' + formatted_name + ' !')


