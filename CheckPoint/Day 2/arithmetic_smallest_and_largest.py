 # Arithmetic, Smallest and Largest
 #sum, average, product, smallest and largest
total = 0
maximum = None
minimum = None

for i in range(1, 5):
    number = int(input(f"Enter value for number{i}: "))
    total += number

    if maximum is None or number > maximum:
        maximum = number
    if minimum is None or number < minimum:
        minimum = number

print("Total:", total)
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
