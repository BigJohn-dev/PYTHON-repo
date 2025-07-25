# indeed doing something
# Lets do a calculator
import math


def add_numbers(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

def subtract_numbers(firstnumber, secondnumber):
    return firstnumber - secondnumber

def multiply_numbers(*numbers):
    multiply = 1
    for number in numbers:
        multiply *= number
    return multiply

def divide_numbers(firstnumber, secondnumber):
    return math.floor(firstnumber / secondnumber)

def get_remainder(firstnumber, secondnumber):
    return firstnumber % secondnumber

def get_square(firstnumber):
    return  firstnumber * firstnumber

def get_cube(firstnumber):
    result = 1
    for i in range(1, 4):
        result *= firstnumber
    return result

def get_square_root(firstnumber):
    return math.sqrt(firstnumber)

def get_power(firstnumber, power):
    return math.pow(firstnumber, power)

def get_cube_root(firstnumber):
    return (firstnumber // 3)

def get_sin(firstnumber):
    return math.sin(firstnumber)

def get_cos(firstnumber):
    return math.cos(firstnumber)

