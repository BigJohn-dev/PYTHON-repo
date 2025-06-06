# To-Do list application

class Task_Manager:

	def __init__(self):
		self.tasks = []

	def add_task(self, description):
		if description == " ":
			return "No task added."
		if description not in self.tasks:
			self.tasks.append({"Task": description, "completed": False})
			return "New task added"

		return "Task already exists"

	def view_task(self):
		if not self.tasks:
			return "No tasks available"
		result = "Your to-do task:\n"
		for i, task in enumerate(self.tasks, 1):
			status = "✔ Completed" if task ["completed"] else "⦿ Not completed"
			result += f"{i}. {tasks['description']} - {status}\n"
		return result

	def mark_task(self, index):
		if 1 <= index <= len(self.task):
			self.tasks[index - 1]["completed"] = True
			return f"Task '{self.tasks[index - 1]['description']}' marked as complete"
		return "Invalid task number"

	def delete_task(self, index):
		if 1 <= index <= len(self.tasks):
			deleted_task = self.tasks.pop(index - 1)
			return f"Task '{deleted_task['description']}' deleted"
		return "Invalid task number"

def main():
	task_manager = Task_Manager()
	while True:
		print("\nWELCOME TO YOUR TO-DO LIST MANAGER")
		print("...manage your everyday tasks")
		menu = """
TO-DO LIST
1. Add a task
2. View all tasks
3. Mark a task as complete
4. Delete a task
5. Exit
"""
		print(menu)
		choice = input("Enter your choice (1-5): ")

		if choice == "1":
			print("ADD A TASK")
			task_input = input("Enter task: ")
			print(task_manager.add_task(task_input))

		elif choice == "2":
			print("VIEW ALL TASKS")
			print(task_manager.view_task())

		elif choice == "3":
			print("MARK A TASK AS COMPLETE")
			print(task_manager.view_task())
			try:
				task_num = int(input("Enter task number to mark as complete: "))
				print(task_manager.mark_task_complete(task_num))
			except ValueError:
				print("Invalid input, please enter a number")

		elif choice == "4":
			print("DELETE A TASK")
			print(task_manager.view_task())
			try:
				task_num = int(input("Enter task number to delete: "))
				print(task_manager.delete_task(task_num))
			except ValueError:
				print("Invalid input, please enter a number")
		elif choice == "5":
			print("...task completed!")
			print("...@TO-DO LIST MANAGER")
			break
		else:
			print("Invalid option")
if __name__ == "__main__":
	main()