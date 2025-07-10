# Volume of a cylinder

class volume_of_a_cynlinder:

	def area(radius):
		PI = 3.1412
		area = radius * radius * PI
		return area

	def volume(area, length):
		volume = area * length
		return f"The volume is {volume}"

radius = float(input("Enter the radius of the cylinder: "))
length = float(input("Enter the length of the cylinder: "))

print(volume_of_a_cynlinder.area(radius))
print(volume_of_a_cynlinder.volume(volume_of_a_cynlinder.area(radius), length))
