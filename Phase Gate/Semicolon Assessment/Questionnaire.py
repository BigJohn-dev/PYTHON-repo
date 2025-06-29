# Semicolon Assessment: Questionnaire
import random
def create_questions():
	return [
		{
			"question": "What is the opposite of black?",
			"options": ["A. White", "B. Red", "C. Green", "D. All of the above"],
			"correct": "D"
		},
		{
			"question": "We should alwaly accept everything at face value?",
			"options": ["A. No", "B. Yes", "C. Maybe", "D. Sometimes"],
			"correct": "A"
		},
		{
			"question": "Fighting is a crime; fight for life, is it a crime?",
			"options": ["A. It depends", "B. No", "C. Yes", "D. Perspective matters here"],
			"correct": "D"
		},
		{
			"question": "What is the opposite of Man?",
			"options": ["A. Woman", "B. Boy", "C. Men", "D. A and B"],
			"correct": "A"
		},
		{
			"question": "The main character in the popular movie JOHN WICK is...?",
			"options": ["A. Keanue Reaves", "B. John Cena", "C. Idris Elba", "D. Gibbs White"],
			"correct": "A"
		},
		{
			"question": "What is the sum of 14 and 62?",
			"options": ["A. 146", "B. 46", "C. 76", "D. I don't know"],
			"correct": "C"
		},
		{
			"question": "What creature has its exo-skeletal system as its outer skin?",
			"options": ["A. Pig", "B. Crocodile", "C. Crabs", "D. All of the above"],
			"correct": "C"
		},
		{
			"question": "What is element has the chemical symbol 'O2'?",
			"options": ["A. Sodium", "B. Orange", "C. Oxygen", "D. Calcium"],
			"correct": "C"
		},
		{
			"question": "What is the chemical formula for water?",
			"options": ["A. H2O", "B. O2", "C. NaCl", "D. CO2"],
			"correct": "A"
		},
		{
			"question": "What ocean is the largest in the world?",
			"options": ["A. Atlantic", "B. Indiana", "C. Pacific", "D. Artic"],
			"correct": "A"
		}
	]

def main():
	questions = create_questions()
	random.shuffle(questions)
	score = 0
	incorrect_answers = []

while False in answered:
	print("WELCOME TO SEMICOLON'S QUIZ GAME")
	print("\n...select your question from 1 - 10")

	choice = int(input("Enter question number (1-10) or 0 to finish: "))
	if choice == 0:
		break
	if choice < 1 or choice > 10:
		print("Invalid choice. Please select a number between 1 and 10.")
		continue
	if answered[choice - 1]:
		print("You don do am!")
		continue
	question = questions[choice - 1]
	attempts = 2
	answered[choice - 1] = True
	while attempts > 0:
		print(f"\nQuestion {choice}: {question['question']}")
		for option in question['options']:
			print(option)
			answer = input("Enter your answer (A, B, C, or D)").upper()
			if answer not in ['A', 'B', 'C', 'D']:
				print("Invalid input! Please enter A, B, C, or D.")
				continue
			
			if answer == question['correct']:
				print("Correct!")
				score += 1
				break
			else:
				attempts -= 1
				if attempts > 0:
					print(f"Incorrect. Try again. {attempts} attempt(s) left.")
				else:
					print(f"Incorrect. The correct answer was {question['correct']}.")
					incorrect_answers.append ({
					"question": question['question'],
					"correct": question['correct'],
					"correct_answer": })
