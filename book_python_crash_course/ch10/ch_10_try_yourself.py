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
abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
			'python_crash_course/ch10/'
			)

## Create variable for file name
file_name = 'like_programming.txt'

## Prompt for username
print("Enter 'quit' when you are finished.")
while True:
    name = input('\nWhat is your name? ')
    reason = input("\nWhy do you like programming? ")
    if name or reason == 'quit':
        break
    else:
        with open(file_name, 'a') as f:
            f.write(name + ' likes programming b/c, ' + reason + '\n')
        print(name + ' likes programming because, ' + reason)


