# (1) Practice writing to a file

abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
			'python_crash_course/ch10/'
			)

## Create variable for file name
file_name = 'programming.txt'

## Read entire file by storing the lines in a list
with open(file_name, 'a') as file_object:
	file_object.write('I also love finding meaning in large datasets.\n')
	file_object.write('I love creating apps that can run in the browser.\n')


