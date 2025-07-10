# random characters
import math
import random


print("Random letters: ")

for i in range(0, 10):
	letter = chr('A' + (math.floor)(random.randrange(1, 27)))
	print(letter, end = " ")