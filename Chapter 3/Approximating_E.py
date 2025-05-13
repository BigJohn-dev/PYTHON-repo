# Approximating the Mathematical Constant e

import math 

terms = 10 
counter = 0.0

for i in range(terms):
	counter += 1.0 / math.factorial(i) 


e_approx = counter  
print('Approximated value of e with', terms, 'terms is:', e_approx)

