# (10-1) Learning Python
## Create Absolute file path
# abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
# 			'python_crash_course/ch10/'
# 			)

# ## Create variable for file name
# file_name = 'learning_python.txt'

# ## Read entire file
# # with open(file_name) as file_object:
# # 	contents = file_object.read()
# # 	print(contents)

# ## Read entire file by looping over each line
# # with open(file_name) as file_object:
# # 	for line in file_object:
# # 		print(line.strip())


# ## Read entire file by storing the lines in a list
# with open(file_name) as file_object:
# 	rows = file_object.readlines()

# for row in rows:
# 	print(row.strip())

# (10-2) Learning C

## Create Absolute file path
# abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
# 			'python_crash_course/ch10/'
# 			)

# ## Create variable for file name
# file_name = 'learning_python.txt'

# ## Read entire file by storing the lines in a list
# with open(file_name) as file_object:
# 	rows = file_object.readlines()

# for row in rows:
# 	new_row = row.replace('Python', 'C')
# 	print(new_row.strip())


# (10-3) - Guest

# ## Create input to obtain user's name...
# first_name = input('What is your first name, please? ')
# last_name = input('What is your last name, please? ')

# user_name = first_name + ' ' + last_name

# ## Create path to store users name to file...
# abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
# 			'python_crash_course/ch10/'
# 			)

# ## Create variable for file name
# file_name = 'guest.txt'

# with open('guest.txt', 'w') as file_object:
# 	file_object.write('The following contains user names: \n')
# 	file_object.write(user_name + '\n')



# (10-4) - Guest Book
# ## Create path to store users name to file...
# abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
# 			'python_crash_course/ch10/'
# 			)

# ## Create variable for file name
# file_name = 'guest_book.txt'

# ## Prompt for username
# print("Enter 'quit' when you are finished.")
# while True:
#     name = input("\nWhat's your name? ")
#     if name == 'quit':
#         break
#     else:
#         with open(file_name, 'a') as f:
#             f.write(name + "\n")
#         print("Hi " + name + ", you've been added to the guest book.")

# (10-5) - Programming Poll
## Create path to store users name to file...
# abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
# 			'python_crash_course/ch10/'
# 			)

# ## Create variable for file name
# file_name = 'like_programming.txt'

# ## Prompt for username
# print("Enter 'quit' when you are finished.")
# while True:
#     name = input('\nWhat is your name? ')
#     reason = input("\nWhy do you like programming? ")
#     if name or reason == 'quit':
#         break
#     else:
#         with open(file_name, 'a') as f:
#             f.write(name + ' likes programming b/c, ' + reason + '\n')
#         print(name + ' likes programming because, ' + reason)

# (10-6) - Addition
# print(int('jogging'))

# print('Provide two values and I\'ll add them for your')
# print('Whenever you stop feeling froggy press \'q\' to quit')


# while True:
# 	first_number = input('First number: ')
# 	if first_number == 'q':
# 		break

# 	second_number = input('Second number: ')
# 	if second_number == 'q':
# 		break

# 	numbers = [first_number, second_number]

# 	for number in numbers:
# 		try:
# 			number_check = int(number)
# 		except ValueError:
# 			msg = 'The entry ' + number + ' is not an number, try again'
# 			print(msg)
# 	try:
# 		addition = int(first_number) + int(second_number)
# 	except ValueError:
# 		print('Please update your values to integers and try again.')
# 	else:
# 		print(addition)

# (10-7) - Addition Calculator
# print('Provide two values and I\'ll add them for your')
# print('Whenever you stop feeling froggy press \'q\' to quit')


# while True:
# 	first_number = input('First number: ')
# 	if first_number == 'q':
# 		break

# 	second_number = input('Second number: ')
# 	if second_number == 'q':
# 		break

# 	numbers = [first_number, second_number]

# 	for number in numbers:
# 		try:
# 			number_check = int(number)
# 		except ValueError:
# 			msg = 'The entry ' + number + ' is not an number, try again'
# 			print(msg)
# 	try:
# 		addition = int(first_number) + int(second_number)
# 	except ValueError:
# 		print('Please update your values to integers and try again.')
# 	else:
# 		print(addition)


# (10-8) - Cats and Dogs
# ## Create path to store users name to file...
# abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
# 			'python_crash_course/ch10/'
# 			)

# ## Create variable for file name
# filenames = ['cats.txt', 'dogs.txt']

# for filename in filenames:
#     print("\nReading file: " + filename)
#     try:
#         with open(abs_file_path + filename) as f:
#             contents = f.read()
#             print(contents)
#     except FileNotFoundError:
#         print("  Sorry, I can't find that file.")


# (10-9) - Silent Cats and Dogs
## Create path to store users name to file...
# abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
# 			'python_crash_course/ch10/'
# 			)

# ## Create variable for file name
# filenames = ['cats.txt', 'dogs.txt', 'jungle_fever.txt']

# for filename in filenames:
#     try:
#         with open(abs_file_path + filename) as f:
#         contents = f.read()
#     except FileNotFoundError:
#         # print("  Sorry, I can't find that file.")
#         pass
#     else:
#     	print("\nReading file: " + filename)
#         print(contents)
    	


# (10-10)
# Create path to store users name to file...
# abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
# 			'python_crash_course/ch10/'
# 			)

# ## Create variable for file name
# filename = 'sleepy.txt'

# ## Select word to count
# ctn_word = 'sleepy'

# ##Create option to count a specific word in a string...

# try:
# 	with open(abs_file_path + filename) as f:
# 		contents = f.read()
# except FileNotFoundError:
# 	pass
# else:
# 	count = contents.count(ctn_word)
# 	counts = contents.lower().count(ctn_word)
# 	print(count)
# 	print(counts)

# line = 'Row, row, row your boat'
# no_case = line.count('row')
# lower_case = line.lower().count('row')

# print(no_case)
# print(lower_case)


# (10-11) Favorite Number
import json

def get_stored_number():
	'''Obtain stored user name'''
	filename = 'fav_number.json'

	try:
		with open(filename, 'r') as f_obj:
			fav_number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return fav_number

def get_new_number():
	'''Create new username'''
	fav_number = input('What is your number? ')
	filename = 'fav_number.json'
	with open(filename, 'w') as f_obj:
		json.dump(fav_number, f_obj)
	return fav_number

def guess_number():
	'''Create function to greet the user by name'''

	fav_number = get_stored_number()

	if fav_number:
		print('I know your number is , ' + fav_number)
	else:
		fav_number = get_new_number()
		print('We will remember your number , ' + fav_number + '.')

guess_number()


## Program to recall users favorite number


# (10-12) Favorite Number Remembered

# (10-13) Verify User


