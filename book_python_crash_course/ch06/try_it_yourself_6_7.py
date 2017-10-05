# (1) 6 - 7 People
user_0 = {
	'username': 'jackdoe01',
	'first_name': 'jack',
	'last_name': 'doe',
}
user_1 = {
	'username': 'janedoe01',
	'first_name': 'jane',
	'last_name': 'doe',
}
user_2 = {
	'username': 'spotdoe01',
	'first_name': 'spot',
	'last_name': 'doe',
}

people = [user_0, user_1, user_2]

# print(people)

for username in people:
	print('The username: ' + username['username'].title() + ' belongs to:')
	full_name = username['first_name'].title() + ' ' + username['last_name'].title()
	print('\t' + full_name.title())

print('\n')

# (2) 6 - 8 Pets

# (3) 6 - 9 Favorite Places

# (4) 6 - 10 Favorite Numbers

# (5) 6 - 11 Cities

cities = {
	'nashville': {
	    'country': 'usa',
	    'population': '1.2 million',
	    'city_fact': 'music city',
	},
	'dubai': {
	    'country': 'uae',
	    'population': '2.4 million',
	    'city_fact': 'burg khalifa',	    
	},
	'manila': {
	    'country': 'thailand',
	    'population': '3.4 million',
	    'city_fact': 'thai boxing',	
	},
}

for city, city_infos in cities.items():
	print('\nWelcome to ' + city.title())
	country = city_infos['country']
	population = city_infos['population']
	city_fact = city_infos['city_fact']
	print('\tWhich is a city in ' + country.title())
	print('\tHome to roughly ' + str(population.title()) + ' people')
	print('\tAnd you best believe they have ' + city_fact)

print('...')
# (6) 6 - 12 Extensions