<<<<<<< HEAD
# Great circle distance
import math


numx1 = float(input("Enter point 1 latitude: "))
numy1 = float(input("Enter point 1 longitude: "))
numx2 = float(input("Enter point 2 latitude: "))
numy2 = float(input("Enter point 2 longitude: "))

x1 = math.radians(numx1);
y1 = math.radians(numy1);
x2 = math.radians(numx2);
y2 = math.radians(numy2);

radius = 6371.01
PI = 3.1412


distance = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1- y2));
=======
# Great circle distance
import math


numx1 = float(input("Enter point 1 latitude: "))
numy1 = float(input("Enter point 1 longitude: "))
numx2 = float(input("Enter point 2 latitude: "))
numy2 = float(input("Enter point 2 longitude: "))

x1 = math.radians(numx1);
y1 = math.radians(numy1);
x2 = math.radians(numx2);
y2 = math.radians(numy2);

radius = 6371.01
PI = 3.1412


distance = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1- y2));
>>>>>>> origin/main
print("The distance between the two points is ", distance, "km");