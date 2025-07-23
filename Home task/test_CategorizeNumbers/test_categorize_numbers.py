<<<<<<< HEAD
import Dividing_a_category_of_numbers
import unittest

class TestDividing_a_category_of_numbers(unittest.TestCase):
	
	def test_that_categorize_numbers_exists(self):

		Dividing_a_category_of_numbers.categorize_numbers((10, 15, 21, 30), 5)

	def test_that_categorize_numbers_return_correct_answer(self):
		actual = Dividing_a_category_of_numbers.categorize_numbers((10, 15, 21, 30), 5)
		expected = [10, 15, 30]
		self.assertEqual(actual, expected)

		actual = Dividing_a_category_of_numbers.categorize_numbers((10, 15, 21, 30), 3)
		expected = [15, 21, 30]
		self.assertEqual(actual, expected)

	def test_that_categorize_numbers_return_divisible_not_found_when_divisor_equal_zero(self):
		self.assertRaises(ValueError, Dividing_a_category_of_numbers.categorize_numbers, (10, 15, 30, 21), divisor = 0)

	def test_that_categorize_numbers_are_not_empty(self):
        	actual = Dividing_a_category_of_numbers.categorize_numbers((), 5)
        	expected = []
        	self.assertEqual(actual, expected)
=======
import Dividing_a_category_of_numbers
import unittest

class TestDividing_a_category_of_numbers(unittest.TestCase):
	
	def test_that_categorize_numbers_exists(self):

		Dividing_a_category_of_numbers.categorize_numbers((10, 15, 21, 30), 5)

	def test_that_categorize_numbers_return_correct_answer(self):
		actual = Dividing_a_category_of_numbers.categorize_numbers((10, 15, 21, 30), 5)
		expected = [10, 15, 30]
		self.assertEqual(actual, expected)

		actual = Dividing_a_category_of_numbers.categorize_numbers((10, 15, 21, 30), 3)
		expected = [15, 21, 30]
		self.assertEqual(actual, expected)

	def test_that_categorize_numbers_return_divisible_not_found_when_divisor_equal_zero(self):
		self.assertRaises(ValueError, Dividing_a_category_of_numbers.categorize_numbers, (10, 15, 30, 21), divisor = 0)

	def test_that_categorize_numbers_are_not_empty(self):
        	actual = Dividing_a_category_of_numbers.categorize_numbers((), 5)
        	expected = []
        	self.assertEqual(actual, expected)
>>>>>>> origin/main
