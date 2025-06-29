# Table of squares and cubes
print("number\tsquare\tcube")

for i in range(1, 6):
    print(f"{i}\t\t{i ** 2}\t\t{i ** 3}")

# Table of values align right
print("number\tsquare\tcube")

for i in range(1, 6):
    print(f"{i} {i ** 2:>8} {i ** 3:>9}")