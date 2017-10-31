# (1) Create a file reader

# ## Define the absolute path for the test file
# file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
# 			'python_crash_course/source_files/chapter_10/'
# 			)
# ## Define the file name to use
# file_name = str(file_path + 'pi_digits.txt')

# # print(file)

# ## Read the file
# with open(file_name) as file_object:
# 	# contents = file_object.read()
# 	# print(contents.rstrip())
# 	for line in file_object:
# 		print(line.rstrip())


# (2) Create file reader to access lines after with block ends
## Define the absolute path for the test file
file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
			'python_crash_course/source_files/chapter_10/'
			)
## Define the file name to use
file_name = str(file_path + 'pi_digits.txt')

# print(file)

## Read the file
with open(file_name) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())