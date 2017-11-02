# (1) Create a function to count the words in books

## Define the absolute path
abs_path = ('/Users/blackice02/Documents/self_development/python/'
			+ 'book_python_crash_course/source_files/chapter_10/'
			)

## Define the file_path
# f_path = abs_path + file_name

def count_words(f_path, file):
	'''
		Create function that takes (1) argument for the file path
		(i.e. .../book_python_crash_course/source_files/chapter_10/alice.txt)
	'''

	try:
		with open(f_path) as f_obj:
			contents = f_obj.read()
	except:
		print('\n')
		msg = 'Sorry, the file (' + f_path + ') does not exist'
		print(msg)
	else:
		# Count the words in the list
		word_list = contents.split()
		num_count = len(word_list)
		count_msg = ('Your file (' + file + ') contains about ' +  
					str(num_count) + ' words'
					)
		print('\n' + count_msg)


## Define the file
# file_name = 'alice.txt'
file_name = ['alice.txt', 'siddhartha.txt', 'jungle_fever.txt', 'moby_dick.txt', 
			'little_women.txt'
			]

## Count the words in the file
for file in file_name:
	f_path = abs_path + file
	count_words(f_path, file)