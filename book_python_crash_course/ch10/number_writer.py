# (1) Create program to write a list to a json (javascript object notation) file

## Import the json module
import json

## Identify the data to write to the file
numbers = [1,3,5,7,9,11]

# Create path to store users name to file...
abs_file_path = ('/Users/blackice02/Documents/self_development/python/book_' +
			'python_crash_course/ch10/'
			)

## Identify the file to write to
filename = 'numbers.json'

## Write the numbers to the file
with open(abs_file_path + filename, 'w') as f_obj:
	json.dump(numbers, f_obj)


## Load data
with open(abs_file_path + filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)