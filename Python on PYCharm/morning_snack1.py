def third_element():
    list_nums = [10, 20, 30, 40, 50]
    print(list_nums[2])

def change_item():
    list_colours = ['red', 'green', 'blue', ]
    list_colours[2] = 'yellow'
    list_colours.append('purple')
    print(list_colours)

def third():
    lst = [1, 2, 3, 4, 5]
    lst.remove(lst[2])
    print(lst)

def  length_of():
    list = ['Alice', 'Bob', 'Charlie']
    print(len(list))

def ascending():
    lst_nums = [4, 1, 3, 9, 2]
    print(sorted(lst_nums))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def even_numbers(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)
    return result

a = [1, 2, 3]
b = [4, 5, 6]
def combine(a, b):
    return a + b

list_string = ["lamb", "Kit", "Yam", "Kings", "dogs", "Man"]

def three_letters(list_string):
    list_letters = []
    for i in range(len(list_string)):
        if len(list_string[i]) == 3:
            list_letters.append(list_string[i])
    print(list_letters)

third_element()
change_item()
third()
length_of()
ascending()
print(even_numbers(numbers))
print(combine(a, b))
three_letters(list_string)