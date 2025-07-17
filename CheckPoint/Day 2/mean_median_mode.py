
def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    for num in set(numbers):
        if numbers.count(num) > len(numbers) / 2:
            return num
    return None

print(mean([1, 22, 31, 31, 1, 1, 1]))
print(median([1, 22, 31, 31, 1, 1, 1]))
print(mode([1, 22, 31, 31, 1, 1, 1]))