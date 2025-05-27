import unittest
from to_do_list import task_manager, to_do_task

class TestToDoList(unittest.TestCase):

	def test_that_to_do_list_exist(self):
		self.task = task_manager()