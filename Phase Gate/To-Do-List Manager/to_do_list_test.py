import unittest
from to_do_list import task_manager, to_do_task

class TestToDoList(unittest.TestCase):

	def test_that_to_do_list_exist(self):
		self.task = task_manager()

	def test_that_to_do_list_task_can_be_created(self):
		tasks = to_do_task("add task", "View task", "mark task", "delete task")
		
	def test_that_add_task_function_works(self):
		tasks = to_do_task("add task", "View task", "mark task", "delete task")
		result = tasks.add_task("Groceries")
		self.assertEqual(tasks.view_task, "View task")
		self.assertEqual(result, "New Task added")