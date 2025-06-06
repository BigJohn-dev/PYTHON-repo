# Area of pentagon 
import math

length = float(input("Enter the length from the center to a vertex: "))

PI = 3.1412

sides = 2 * length * (math.sin(PI / 5))
area = (5 * (sides * sides)) / (4 * (math.tan(PI / 5)));

print("The area of the pentagon is ", area)