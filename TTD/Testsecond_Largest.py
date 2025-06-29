import second_Largest
import unittest

class Testsecond_Largest(unittest.TestCase):
	def test_that_second_largest_function_exixts(self):

		second_Largest.second_number((9, 6, 8, 11, 12))
	
	def test_that_second_largest_function_is_correct(self):
		actual = second_Largest.second_number((9, 6, 8, 11, 12))
		expected = 11
		self.assertEqual(actual, expected)

	def test_that_second_largest_function_raise_value_error(self):
		self.assertRaises(valueError, second_Largest.second_number, )