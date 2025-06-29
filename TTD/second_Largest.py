#second largest number 

def second_number(values):
	if len(values) < 2:
        	return None

	largest = max(values[0], values[1])
	second_largest = min(values[0], values[1])

	for i in values[2:]:
		if(i > largest):
			second_largest = largest;
			largest = i;

		if(i != largest):
			largest = second_largest;
			second_largest = i;

	return second_largest

print(second_number((9, 6, 8, 11, 12)))