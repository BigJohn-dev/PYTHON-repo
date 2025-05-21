# Problem with the Median
import statistics

Values = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]

Values.sort()
print(Values)

n = len(Values)

if n % 2 != 0:
	median = Values[n // 2]
	print(f'The middle number is {median}')
else:	
	middle_number = n // 2
	median = statistics.mean(Values[middle_number-1:middle_number+1])
	print(f'The average of the two middle values is {median}')


    