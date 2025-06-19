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

    def test_print_array(self):
        self.assertEqual(len(print_array()), 10)

