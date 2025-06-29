import Arbitrary_Argument_list
import unittest

class TestArbitrary_Argument_list(unittest.TestCase):
	
	def test_that_Arbitrary_Argument_list_exists(self):

		Arbitrary_Argument_list.average(5, 10)

	def test_that_Arbitrary_Argument_list_is_correct(self):
		actual = Arbitrary_Argument_list.average(5, 10)
		expected = 7.5
		self.assertEqual(actual, expected)

		actual = Arbitrary_Argument_list.average(5, 10, 15)
		expected = 10.0
		self.assertEqual(actual, expected)

	def test_that_Arbitrary_Argument_list_raise_Type_Error_for_missing_argumen(self):
		self.assertRaises(TypeError, Arbitrary_Argument_list.average, )