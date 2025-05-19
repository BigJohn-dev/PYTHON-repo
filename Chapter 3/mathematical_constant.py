# Approximating the mathematical constant PI

terms = 1000000 
counter = 0.0

for i in range(terms):
	counter += (-1.0)**i / (2.0 * i + 1)


PI_approx = 4 * counter
print('Approximated value of PI with', terms, 'terms is:', PI_approx)

