# Approximate the mathematical constant e using its series expansion
import math

e_actual = math.e
approximation = 1
factorial = 1
count = 0

for i in range(1, 20):
    factorial *= i
    approximation += 1 / factorial
    count += 1

print(f"Approximated e: {approximation} after {count} times")
print(f"Actual e: {e_actual}")
