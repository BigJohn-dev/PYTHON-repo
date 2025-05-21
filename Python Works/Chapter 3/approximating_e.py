# Approximating the Mathematical Constant e

import math 

TERMS = 10 
counter = 0.0

for i in range(TERMS):
	counter += 1.0 / math.factorial(i) 


e_approx = counter  
print('Approximated value of e with', TERMS, 'terms is:', e_approx)

