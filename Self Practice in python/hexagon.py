# area of a hexagon
import math

print("COMPUTING THE AREA OF AN HEXAGON");

side = float(input("Enter the side: "))
PI = 3.1412
area = (6 * (side * side)) / (4 * (math.tan(PI / 6)));

print("The area of the hexagon is ", area)