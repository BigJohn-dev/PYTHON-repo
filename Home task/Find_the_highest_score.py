# Find the highest score

number_0f_students = int(input('Enter number of students: '))

highest_score = 0
highest_name = ""

for count in range (0, number_0f_students):
	name = (input("\nEnter student's name: "))
	score = int(input("Enter student's score: "))

	if score > highest_score:
		highest_score = score
		highest_name = name

print('\n',highest_name,'has the highest score of ', highest_score)
		