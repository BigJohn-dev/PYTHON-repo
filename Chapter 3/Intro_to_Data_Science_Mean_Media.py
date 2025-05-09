import statistics

# Intro to Data Science: Mean, Median and Mode

Values = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]
Values.sort()

print(Values)

mean = statistics.mean(Values)

median = statistics.median(Values)

mode = statistics.mode(Values)

print(f'Mean is: {mean}, Median is: {median}, Mode is: {mode}')

