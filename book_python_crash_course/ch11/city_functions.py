## Function that accepts two parameters
def city_country(city, country, population=''):
	'''Function that returns single string of city and country'''

	if population:
		return (city.title() + ', ' + country.title() + ' - population ' +
				str(population))
	else:
		return city.title() + ', ' + country.title()