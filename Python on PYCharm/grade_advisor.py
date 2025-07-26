
def get_grade(score):
    if score >=  80:
      return 'A'
    elif score >= 70:
      return "B"
    elif score >= 60:
      return "c"
    elif score >= 50:
        return "D"
    elif score >= 45:
        return "E"
    else:
        return "F"

def feed_back(score):
    if score >= 80:
        return "Excellent work! Keep it up!"
    elif score >= 70:
        return "Goof job, keep improving"
    elif score >= 60:
        return "Good job! You can do even better!"
    elif score >= 50:
        return "Fair effort, but there's room for improvement."
    elif score >= 45:
        return "You passed, but consider reviewing the material."
    elif score >= 40:
        return "You barely passed, please seek help if needed."
    else:
        return "Unfortunately, you did not pass. Please try again."

def main():
    print("Welcome to the Grade Advisor!")
    print("Please enter your score to receive your grade and feedback.")
    while True:
        score_input = int(input("Enter your score: "))
        if score_input < 0 or score_input > 100:
            print("Invalid input. Please enter a score between 0 and 100.")
            continue
        print(get_grade(score_input))
        print(feed_back(score_input))
        break

if __name__ == "__main__":
    main()