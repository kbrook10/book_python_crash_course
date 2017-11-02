# (1) Create program to read username from file
import json

## Identify file where username is stored
filename = 'username.json'

## Read file and print username
with open(filename, 'r') as f_obj:
	username = json.load(f_obj)
	print('Welcome back, ' + username)
	