# (1) Obtain the country codes
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
	'''Return the pygal (2) two-digit country code'''

	for code, name in COUNTRIES.items():
		if name == country_name:
			return code

	## If country not found
	return None

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))

