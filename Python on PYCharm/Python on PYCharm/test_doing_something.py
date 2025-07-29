import unittest
from doing_something import *

class testdoing_something(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3, 10, 50, 40), 105)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(50, 40), 10)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(2, 3, 10), 60)

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(2, 3), 0)

    def test_get_remainder(self):
        self.assertEqual(get_remainder(2, 3), 2)

    def test_get_squared_numbers(self):
        self.assertEqual(get_square(13), 169)

    def test_get_cube(self):
        self.assertEqual(get_cube(10), 1000)

    def test_get_square_root(self ):
        self.assertEqual(get_square_root(25), 5)

    def test_raised_to_power(self):
        self.assertEqual(get_power(5, 2), 25)

    def test_get_cube_root(self):
        self.assertEqual(get_cube_root(75), 25)

    def test_get_sin(self):
        self.assertEqual(get_sin(1), 0.8414709848078965)

    def test_get_cos(self):
        self.assertEqual(get_cos(1), 0.5403023058681398)