# (1) Generate a polling list with individual responses...

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

print('Sarah\'s favorite language is ' + 
	   favorite_languages['sarah'].title() +
	   '.')

for name, language in favorite_languages.items():
	print(name.title() + '\'s favorite language is ' + language.title() + '.')

print('\n')

for name in favorite_languages.keys():
	print(name.title())

print('\n')

for name in sorted(favorite_languages.keys()):
	print(name.title() + ' , thank you for taking the poll.')

print('\n')	

print('The following languages have been mentioned:')
for language in favorite_languages.values():
	print(language.title())

print('\n')	

# (2) Try it yourself

# (6-1) Person
person = {
	'first_name': 'John',
	'last_name': 'Doe',
	'age': 45,
	'city': 'Salt Lake City',
}

print('First name is ' + person['first_name'])
print('Last name is ' + person['last_name'])
print('Age is ' + str(person['age']))
print('City is ' + person['city'])

# (6-2) Favorite Number
favorite_number = {
	'Jack': 45,
	'Jane': 23,
	'Jill': 10,
	'Tyler': 89,
	'John': 58,
}

# Create two lists, one for the keys and another for the values

favorite_num_keys = favorite_number.keys()
favorite_num_values = favorite_number.values()
print('\nFavorite numbers of friends')

# The zip() function is used to to process two lists in parallel
# ...Used the tab character to space out the two lists

for number_key, number_value in zip(favorite_num_keys, favorite_num_values):
	print(number_key, '\t', number_value)

# (6-3) Glossary

glossary = {
	'del_statement': 'used to completely remove a key-value pair.',
	'if_else': 'syntax makes it possible to take one action when a' +
	'conditional test passes and a different action in all other cases', 
	'in': 'Used to find out whether a particular value is already in a list',
	'and': 'Used to check whether two conditions are both True simultaneously.',
	'conditional_test': 'an expression that can be evaluated as True or False'
}

print('\n')
glossary_keys = glossary.keys()
glossary_values = glossary.values()
print('\nGlossary of recent terms learned:\n')

# The zip() function is used to to process two lists in parallel
# ...Used the tab character to space out the two lists

for glossary_key, glossary_value in zip(glossary_keys, glossary_values):
	print(glossary_key, ': (Meaning) -> \t', glossary_value, '\n')

# (6-4) Glossary 2
glossary_2 = {
	'del_statement': 'used to completely remove a key-value pair.',
	'if_else': 'syntax makes it possible to take one action when a ' +
	 'conditional test passes and a different action in all other cases',
	'in': 'Used to find out whether a particular value is already in a list',
	'and': 'Used to check whether two conditions are both True simultaneously.',
	'conditional_test': 'an expression that can be evaluated as True or False',
	'set': 'is similar to a list except that each item in the set must' + 
	'be unique.',
	'key': 'is useful when you don\'t need to work w/ all' +
	 'of the values in a dictionary',
	 'values': 'is useful when you don\'t need to work with all' + 
	 'of the keys in a dictionary',

}

print('\nThe following are recent terms learned\n')
for term, definition in glossary_2.items():
	print(term, ': (Meaning) -> \t', definition, '\n')

print('\n')

# (6-5) Rivers

rivers = {
	'nile': 'egypt',
	'amazon': 'columbia',
	'yangtze': 'najing',
	'mississippi': 'missouri',
}

print('Famous rivers of the world and where they run')
for river, country in rivers.items():
	print('The ' + river.title() + ' runs through ' + country.title())
print('\n')

print('Famous rivers of the world')
for river in rivers.keys():
	print(river.title())
print('\n')

print('Countries that famous rivers run through in the world')
for country in rivers.values():
	print(country.title())
print('\n')

# (6-6) Polling

print('\nPolling:')
available_polling = ['spot','jack', 'richard','jill', 'janet','jane', 'kim',
                     'john', 'tyler',]


polled_responses = {
	'jack': 'Python',
	'jill': 'Ruby',
	'jane': 'Javascript',
	'john': 'Python',
}

for name in available_polling:
	if name in polled_responses.keys():
		print('Thank you ' + name.title() + ' for taking our favorite '
		'language poll!')
		print(name.title() + '\'s favorite progamming language is ' + 
		language.title())
		print('\n')
	else:
		print(name.title() + ', Please submit response for favorite language.')
		print('\n')

print('End of List')

