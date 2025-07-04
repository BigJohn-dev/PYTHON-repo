<<<<<<< HEAD
import unittest
from manipulating_list import *
import random

class Testmanipulating_list (unittest.TestCase):

    def test_function_works(self):
        self.assertEqual(callable(print_array), True)
        self.assertEqual(callable(array_length(values)), False)
        self.assertEqual(callable(sum_of_even_numbers), True)
        self.assertEqual(callable(sum_of_odd_numbers), True)
        self.assertEqual(callable(multiply_elements_at_third_position), True)
        self.assertEqual(callable(average_of_all_element), True)

    def test_array_length(self):
        self.assertEqual(array_length(values), 10)

    def test_sum_of_even_numbers(self):
        actual = [1,2,3,4,5,6,7,8,9,10]
        expected = 30
        self.assertEqual(sum_of_even_numbers(actual), expected)

    def test_sum_of_odd_numbers(self):
        actual = [1,2,3,4,5,6,7,8,9,10]
        expected = 25
        self.assertEqual(sum_of_odd_numbers(actual), expected)

    def test_multiply_elements_at_third_position(self):
        actual = [1,2,3,4,5,6,7,8,9,10]
        expected = 162
        self.assertEqual(multiply_elements_at_third_position(actual), expected)

    def test_average_of_all_elements(self):
        actual = [1,2,3,4,5,6,7,8,9,10]
        expected = 5.5
        self.assertEqual(average_of_all_element(actual), expected)
=======
import unittest
from manipulating_list import *
import random

class Testmanipulating_list (unittest.TestCase):

    def test_function_works(self):
        self.assertEqual(callable(print_array), True)
        self.assertEqual(callable(array_length(values)), False)
        self.assertEqual(callable(sum_of_even_numbers), True)
        self.assertEqual(callable(sum_of_odd_numbers), True)
        self.assertEqual(callable(multiply_elements_at_third_position), True)
        self.assertEqual(callable(average_of_all_element), True)

    def test_array_length(self):
        self.assertEqual(array_length(values), 10)

    def test_sum_of_even_numbers(self):
        actual = [1,2,3,4,5,6,7,8,9,10]
        expected = 30
        self.assertEqual(sum_of_even_numbers(actual), expected)

    def test_sum_of_odd_numbers(self):
        actual = [1,2,3,4,5,6,7,8,9,10]
        expected = 25
        self.assertEqual(sum_of_odd_numbers(actual), expected)

    def test_multiply_elements_at_third_position(self):
        actual = [1,2,3,4,5,6,7,8,9,10]
        expected = 162
        self.assertEqual(multiply_elements_at_third_position(actual), expected)

    def test_average_of_all_elements(self):
        actual = [1,2,3,4,5,6,7,8,9,10]
        expected = 5.5
        self.assertEqual(average_of_all_element(actual), expected)
>>>>>>> origin/main
