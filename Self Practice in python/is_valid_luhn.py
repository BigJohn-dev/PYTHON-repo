def is_valid_luhn(number):
    total = 0
    reverse_digits = number[::-1]

    for i, digit in enumerate(reverse_digits):
        if not digit.isdigit():
            return False
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

if __name__ == "__main__":
    num = input("Enter the number to validate: ")
    if is_valid_luhn(num):
        print(f"{num} is valid.")
    else:
        print(f"{num} is invalid.")
