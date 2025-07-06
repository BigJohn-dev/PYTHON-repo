# printing triangle below the other using nested loop

for i in range(1, 11):
    for j in range(1, i + 1):
        print("*", end = " ")
    print()

print()
for i in range(10, 0, -1):
    for j in range(1, i + 1):
        print("*", end = " ")
    print()

print()
for i in range(10, 0, -1):
    for j in range(1, i + 1):
        print(" *", end = " ")
    print()