# (1) Using the while loop to run as long as a given condition is TRUE

# current_number = 1

# while current_number <= 5:
	# print(current_number)
	# current_number += 1

# print('That is all folks!')

# (2) Using the continue statement in a loop to not break out of a loop

current_number = 0

while current_number < 10:
	current_number += 1
	
	if current_number % 2 == 0:
		continue

	print(current_number)