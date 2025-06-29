import unittest 
from celsius_to_fahrenheit import celsiusToFahrenheit

class Testcelsius_to_fahrenheit(unittest.TestCase):

	def test_that_function_exist(self):
		self.assertTrue(callable(celsiusToFahrenheit.fahrenheit))
		
	def test_that_function_works(self):
		self.assertEqual(celsiusToFahrenheit.fahrenheit(43.0), "43.0 Celsius is 109.4 Fahrenheit")
		self.assertEqual(celsiusToFahrenheit.fahrenheit(50.0), "50.0 Celsius is 122.0 Fahrenheit")