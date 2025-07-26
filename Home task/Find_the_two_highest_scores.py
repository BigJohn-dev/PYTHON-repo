# Find the two highest scores

number_0f_students = int(input('Enter number of students: '))

highest_score = 0
second_highest_score = 0

highest_name = ""
second_highest_name = ""

for count in range (0, number_0f_students):
	name = (input("\nEnter student's name: "))
	score = int(input("Enter student's score: "))

	if score > highest_score:
		second_highest_score = highest_score
		second_highest_name = highest_name
		highest_score = score
		highest_name = name

if score >= second_highest_score and score <= highest_score:
	second_highest_score = score
	second_highest_name = name

print('\n',highest_name, 'has the second highest score of ', highest_score)
print(second_highest_name, 'has the second highest score of ', second_highest_score)	
