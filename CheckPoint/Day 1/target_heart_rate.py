# Target heart calculator

age = int(input("How old are you? "))

heart_rate = 220 - age

range1 = heart_rate * 0.50
range2 = heart_rate * 0.85

print(f"The heart rate is {heart_rate}bpm")
print(f"The range of heart rate is {range1} and {range2}")