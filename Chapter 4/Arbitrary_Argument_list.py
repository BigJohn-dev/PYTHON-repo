# Arbitrary Argument list

def average(*args):
	if not args:
		raise TypeError("average() requires at least one argument")
	return sum(args) / len(args)

print(average(10, 15, 25))
        
    