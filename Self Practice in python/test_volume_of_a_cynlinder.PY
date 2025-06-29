import unittest
from volume_of_a_cynlinder import volume_of_a_cynlinder

class Testvolume_of_a_cynlinder(unittest.TestCase):

	def test_functions_work(self):
		self.assertTrue(callable(volume_of_a_cynlinder.area))
		self.assertTrue(callable(volume_of_a_cynlinder.volume))

	def test_area(self):
		self.assertEqual(volume_of_a_cynlinder.area((5.5)), 95.0213)

	def test_volume(self):
		self.assertEqual(volume_of_a_cynlinder.volume((95.0213, 12.0), 1140.2556))