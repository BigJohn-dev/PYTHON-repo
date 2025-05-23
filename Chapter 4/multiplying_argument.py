# Arbitrary Argument list

def multiplication(*args):
	product = 1
	product *= args

	return product

print(multiplication(10, 15, 25))
        
    