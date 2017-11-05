# (1) Test the city_function module
import unittest
from city_functions import city_country

## create unit tests
class CityCountryTests(unittest.TestCase):
	'''Create child class to test functions'''

	def test_city_country_names(self):
		'''Does the city, country Santiago, Chile work?'''

		# formatted_city_country = city_country('santiago', 'chile')
		# self.assertEqual(formatted_city_country, 'Santiago, Chile')

		formatted_city_country = city_country('santiago', 'chile', 5000000)
		self.assertEqual(formatted_city_country, 'Santiago, Chile - ' +
			'population 5000000')


	def test_city_country_population(self):
		'''Test we can run values of santiago, chile, and population'''

		formatted_city_country_population = city_country('santiago', 'chile',
			population = 5000000)
		self.assertEqual(formatted_city_country_population, 'Santiago, Chile - ' 
			+ 'population 5000000')

unittest.main()