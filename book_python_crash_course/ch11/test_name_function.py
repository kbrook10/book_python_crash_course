# (1) Use the unittest module to create unit tests for test case

## Import necessary modules, functions and classes
import unittest
from name_function import get_formatted_name

## Create class that inherits from the parent class TestCase

class NamesTestCase(unittest.TestCase):
	'''Test the function get_formatted_name from the name_function module'''

	## Create unit tests
	def test_first_last_name(self):
		'''Does the name Janet Jackson work?'''

		formatted_name = get_formatted_name('janet','jackson')
		self.assertEqual(formatted_name, 'Janet Jackson')

	## Create unit tests for middle name
	def test_first_last_middle_name(self):
		'''Does the name Wolfgang Mozart Amadeus work?'''

		formatted_name = get_formatted_name('wolfgang','mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()