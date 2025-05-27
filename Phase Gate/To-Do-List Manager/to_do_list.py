#To-Do List Manager


class to_do_task:

	def __init__(self, add_task, view_task, mark_task, delete_task):
		self.add_task = add_task
		self.view_task = view_task
		self.mark_task = mark_task
		self.delete_task = delete_task

	def add_task(self, task):
		if task != " ":
			self.add_task += [task]
			return "New Task added"
		else:
			return "No task added"

	def view_task(self):
		return  f"This are your to-do task {self.add_task}"

	def delete_task(self, task):
		if task == self.add_task:
			self.add_task -= add_task
			return "Task was successfully deleted"
		return "Invalid option to delete task"

class task_manager:
	
	def __init__(self):
		self.tasks = {}

	def add_task(self, add_task):
		if add_task not in self.tasks:
			new_task = to_do_task(add_task)
			self.to_do_task[add_task] = new_task
			return f"New Task added"
		else:
			return "Task to do already exists"
	
	def delete_task(self, add_task):
		if add_task in self.to_do_task and self.to_do_task[add_task].delete_task == add_task:
			self.tasks = self.to_do_task[add_task]
			return "You've deleted a task"
		else:
			return "Task doesn't exist"

	def view_task(self, add_task):
		return self.to_do_task.get(add_task)

def main():
	task = task_manager()
	while True:

		print('\nWELCOME TO YOUR TO-DO LIST MANAGER')
		print("...manage your everyday's task")

		menu = """

	TO-DO list
1. Add a task
2. View all task
3. Mark a task as complete
4. Delete a task
5. Exit
		"""
		print(menu)
		choice = input()

		if choice == "1":
			print("ADD A TASK")
			Task = input("Enter task you want add: ")
			if Task != " ":
				tasks.append(tasks)
			print(task.to_do_task(Task, add_task))

		elif choice == "2":
			print("VIEW ALL TASK")
			print(task.view_task(view_task))

		elif choice == "3":
			print("MARK A TASK AS COMPLETE")
				
		elif choice == "4":
			print("DELETE A TASKs")

		elif choice == "5":
			print("...task completed!")
			print("...@TO-D0 LIST MANAGER")
			break

		else:
			print("Invalid option")
		

if __name__ == "__main__":
	main()