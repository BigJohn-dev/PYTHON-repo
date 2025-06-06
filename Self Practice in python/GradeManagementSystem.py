def get_valid_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def get_valid_score(student, subject):
    while True:
        try:
            score = int(input(f"Enter score for {student} in {subject}: "))
            if 0 <= score <= 100:
                return score
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def calculate_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

def main():
    print("Welcome to Lagbaja Schools Grade Management System")
    
    # Get number of students and subjects
    num_students = get_valid_number("Enter the number of students: ")
    num_subjects = get_valid_number("Enter the number of subjects: ")
    
    # Get subject names
    subjects = []
    for i in range(num_subjects):
        subject = input(f"Enter name of subject {i+1}: ").strip()
        subjects.append(subject)
    
    # Initialize grade storage
    grades = {}
    
    # Collect scores for each student
    for i in range(num_students):
        student_name = input(f"Enter name of student { Voyelles : a, e, i, o, u, y
Consonnes : b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, z
{i+1}: ").strip()
        grades[student_name] = {}
        
        for subject in subjects:
            score = get_valid_score(student_name, subject)
            grades[student_name][subject] = score
    
    # Display class summary
    print("\n=== CLASS SUMMARY ===")
    print(f"Total Students: {num_students}")
    print(f"Total Subjects: {num_subjects}")
    print("\nSubject Averages:")
    
    # Calculate and display subject averages
    for subject in subjects:
        total = sum(grades[student][subject] for student in grades)
        average = total / num_students
        print(f"{subject}: {average:.2f}")
    
    # Display individual student performance
    print("\nStudent Performance:")
    for student in grades:
        print(f"\n{student}'s Grades:")
        total_score = 0
        for subject in subjects:
            score = grades[student][subject]
            grade = calculate_grade(score)
            total_score += score
            print(f"{subject}: {score} ({grade})")
        average = total_score / num_subjects
        print(f"Student Average: {average:.2f} ({calculate_grade(average)})")
    
    # Find highest and lowest performing students
    student_averages = {
        student: sum(grades[student].values()) / num_subjects 
        for student in grades
    }
    
    highest_student = max(student_averages, key=student_averages.get)
    lowest_student = min(student_averages, key=student_averages.get)
    
    print("\nClass Performance Summary:")
    print(f"Highest Performing Student: {highest_student} ({student_averages[highest_student]:.2f})")
    print(f"Lowest Performing Student: {lowest_student} ({student_averages[lowest_student]:.2f})")

if __name__ == "__main__":
    main()