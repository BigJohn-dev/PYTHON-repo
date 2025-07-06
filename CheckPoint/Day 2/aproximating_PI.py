# Approximating mathematical constant PI
PI = 3.14159
approximation = 0
count = 0
for i in range(1_000_000):
    result = ((-1) ** i) / (2 * i + 1)
    approximation += result
    count += 1

approximation *= 4

print(f"Approximated PI: {approximation:.5f} is reached after {count:,} times.")
print(f"Actual PI: {PI}")
