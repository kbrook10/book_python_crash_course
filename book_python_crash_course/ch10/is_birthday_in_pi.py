# (1) Determine if birthday is in 1st million digits of pi

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

## Search for birthday in pi_string
birthday = input('Please enter your birthday in the form mmddyy: ')

if birthday in pi_string:
	print('Congratulations, your birthday appears in the first million digits'
		' of pi.'
		)
else:
	print('Sorrt, your birthday Does Not appear in the first million digits'
		' of pi.'
		)
