
class Reflection:

	def __init__(self):
		self.Problems = []

	def add_problem(self, description):
		if description == " ":
			return "No problems added."
		if description not in self.Problems:
			self.Problems.append({"Problem": description, "status": False})
			return "New problem added"

		return "Problem already exists"

	def view_problems(self):
		if not self.Problems:
			return "No problem available"
		result = "Your problems:\n"
		for i, problem in enumerate(self.Problems, 1):
			status = "Solved" if problem ['solved'] else "Not solved"
			result += f"{i}. {self.Problems['solved']} - {status}\n"
		return result3

	def mark_solved_problems(self, index):
		if 1 <= index <= len(self.Problems):
			self.Problems[index - 1]["solved"] = True
			return f"Task '{self.Problems[index - 1]['description']}' marked as solved"
		return "Invalid problem number"

	def remove_problem(self, index):
		if 1 <= index <= len(self.Problems):
			remove_problem = self.Problems.pop(index - 1)
			return f"Problem '{remove_problem['description']}' removed"
		return "Invalid problem number"

def main():
	reflection = Reflection()
	while True:
		print("\nWELCOME TO SELF REFLECTION")
		print("...manage your everyday problems")
		menu = """
REFLECTION CHECK

1. Add a problem
2. View all problems
3. Mark a problem as solved
4. Delete a problem
5. Exit
"""
		print(menu)
		choice = input("Enter your choice (1-5): ")

		if choice == "1":
			print("ADD A PROBLEM")
			problem_input = input("Enter your problem: ")
			print(reflection.add_problem(problem_input))

		elif choice == "2":
			print("VIEW ALL PROBLEMS")
			print(reflection.view_problems())

		elif choice == "3":
			print("MARK A PROBLEMS AS SOLVED")
			print(reflection.view_problems())
			try:
				problem_num = int(input("Enter task number to mark as solved: "))
				print(reflection.mark_solved_problems(problem_num))
			except ValueError:
				print("Invalid input, please enter a number")

		elif choice == "4":
			print("DELETE A PROBLEM")
			print(reflection.view_problems())
			try:
				problem_num = int(input("Enter problem number to delete: "))
				print(reflection.remove_problem(problem_num))
			except ValueError:
				print("Invalid input, please enter a number")
		elif choice == "5":
			print("...all problems solved!")
			print("...@REFLECTION-CHECKS")
			break
		else:
			print("Invalid option")
if __name__ == "__main__":
	main()