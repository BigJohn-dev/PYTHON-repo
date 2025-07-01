# print table of square and cube between the range 0 - 5(inclusive)

print('numbers\tsquares\tcubes')
for i in range(0, 6):
    print(f"{i:>7} {i ** 2:>7} {i ** 3:>5}")