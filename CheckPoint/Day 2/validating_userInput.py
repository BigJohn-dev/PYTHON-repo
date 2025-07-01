"""Using nested control statements to analyze examination results."""
passes = 0  # number of passes
failures = 0  # number of failures
count = 1

while count <= 10:
    result = int(input('Enter result (1=pass, 2=fail): '))
    if result == 1:
        passes = passes + 1
        count += 1
    elif result == 2:
        failures = failures + 1
        count += 1
    else:
        print('Invalid input')
        continue

print('Passed:', passes)
print('Failed:', failures)
