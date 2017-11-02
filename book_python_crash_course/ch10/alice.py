# (1) Create situation to handle file not found

# abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
# 			'python_crash_course/source_files/chapter_10/'
# 			)

abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
			'python_crash_course/ch10/'
			)

## Create variable for file name
text_file_name = abs_file_path + 'alice.txt'

## Read entire file by storing the lines in a list
try:
	with open(text_file_name) as file_object:
		file_object.read()

except FileNotFoundError:
	msg = ('We are sorry, but we can\'t seem to find your ' + text_file_name 
			+  ' file')
	print(msg)