import unittest
from To_Do_list_application import Task_Manager

class TestTo_Do_list_application(unittest.TestCase):

	def test_that_To_Do_list_application_Setup(self):
		task_manager = Task_Manager()

	def test_that_To_Do_list_application_task_can_be_added(self):
		tasks = Task_Manager()