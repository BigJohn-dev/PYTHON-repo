#Target heart-rate calculator

print(' __-- HEART RATE CALCULATOR --__ ')

HEART_RATE_IN_BEATS_PER_MINUTES = 220

age = int(input('Enter your age: '))

heart_rate = HEART_RATE_IN_BEATS_PER_MINUTES - age

target_heart_rate = heart_rate * 0.50

target_heart_rateII = heart_rate * 0.85


print('Your heart rate is ', heart_rate)
print('Your target heart range is ', target_heart_rate, '-', target_heart_rateII, 'bpm')