# (1) Using the break statement to end program in the middle of a while loop

prompt = '\nPlease enter the name of a city you have visited:'
prompt += '\n(Enter \'quit\' when you are finished.) '

while True:
	city = input(prompt)

	if city == 'quit':
	    break
	else:
		print('I\'d love to go to ' + city.title() + '!')
