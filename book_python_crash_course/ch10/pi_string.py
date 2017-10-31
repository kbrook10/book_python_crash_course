# (1) Attempt to build a single string containing all the digits in the file

## Define the absolute path for the test file
file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
			'python_crash_course/source_files/chapter_10/'
			)
## Define the file name to use
# file_name = str(file_path + 'pi_digits.txt')
file_name = str(file_path + 'pi_million_digits.txt')



## Read the file
with open(file_name) as file_object:
	lines = file_object.readlines()

## Create variable to hold the pi string...
pi_string = ''

## Loop over the content lines and add each to the string...
for line in lines:
	pi_string += line.strip()

## Display contents; limit to 51
# print(pi_string)
print(pi_string[:52] + '...')
print(len(pi_string))