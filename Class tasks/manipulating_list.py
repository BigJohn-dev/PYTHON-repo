# Array in python
import random

values = []

def print_array():
    for i in range(1, 11):
        values.append(random.randint(1, 51))
    return values

def array_length(values):
    length = 0
    for _ in values:
        length += 1
    return length

def sum_of_even_numbers(values):
    sum = 0
    for number in range(array_length(values)):
        if number % 2 != 0:
            sum += values[number]
    return sum

def sum_of_odd_numbers(values):
    sum = 0
    for number in range(array_length(values)):
        if number % 2 == 0:
            sum += values[number]
    return sum

def multiply_elements_at_third_position(values):
    multiply = 1
    for number in range(2, array_length(values), 3):
        multiply *= values[number]
    return multiply

def average_of_all_element(values):
    sum = 0
    for number in values:
        sum += number
        total = sum / array_length(values)
    return total


print(f"The elements in the array are: {print_array()}")
print(f"The length of array is: {array_length(values)}")
print(f"The sum of even numbers at index position is: {sum_of_even_numbers(values)}")
print(f"The sum of odd numbers at index position is: {sum_of_odd_numbers(values)}")
print(f"The total multiplication of every elements at third place are: {multiply_elements_at_third_position(values)}")
print(f"The average of all elements in function is: {average_of_all_element(values)}")
