def convert_numbers_to_word(numbers):
    numbers_to_word = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
    }
    return numbers_to_word.get(numbers, "Invalid number")

number = int(input("Enter a number: "))
value = convert_numbers_to_word(number)
print(f"The number {number} is {value}")
