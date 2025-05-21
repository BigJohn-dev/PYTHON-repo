# Miles per Gallon

total_miles_driven = 0
total_miles_per_gallon = 0
gallons_used = 0
miles_driven = 0
counter = 0

gallons_used = float(input('Enter the gallons used (-1 to end): '))

while gallons_used != -1:
	miles_driven = float(input('Enter the miles driven: '))
	miles_per_gallon = miles_driven / gallons_used

	total_miles_per_gallon += gallons_used
	total_miles_driven += miles_driven

	print(f'The miles/gallon for this tank was {miles_per_gallon}')

	counter += 1
	gallons_used = float(input('Enter the gallons used (-1 to end): '))

if counter != 0:
	average = total_miles_driven / total_miles_per_gallon

	print(f'The overall average miles_per_gallon was {average}')

else:
	print('No input were made')