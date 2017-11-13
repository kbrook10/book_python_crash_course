# (1) Import the country codes from Pygal
from pygal.maps.world import COUNTRIES

## Loop over two-digit codes
for country_code in sorted(COUNTRIES.keys()):
	print(country_code, COUNTRIES[country_code])

	 