# (1) Practice with analyzing text

# title = 'Alice in Wonderland'
# print(title.split())

## Define the absolute path
abs_path = ('/Users/blackice02/Documents/self_development/python/'
			+ 'book_python_crash_course/source_files/chapter_10/'
			)

## Define the file
file_name = 'alice.txt'

## Define the file_path
f_path = abs_path + file_name

## Create try-except block to handle FileNotFoundError
try:
	with open(f_path) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = 'Sorry, the file (' + f_path + ') does not exist.'
	print(msg)
else:
	## Count the words in the file
	word_list = contents.split()
	num_count = len(word_list)
	total = ('The file... \n(' + f_path + ') \nhas about (* ' + str(num_count) + 
		' *) words')
	print(total)
