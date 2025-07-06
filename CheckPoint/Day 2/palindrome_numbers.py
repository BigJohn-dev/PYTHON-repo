# check if a set of numbers are palindrome numbers
numbers = input("Enter numbers: ")
numbers = numbers.split()
for n in numbers:
    if n == n[0::-1]:
        print(f"{numbers} is a palindrome")
    else:
        print(f"{numbers} is not a palindrome")
