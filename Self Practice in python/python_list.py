# practicing python's list

my_list = ["supraMk4", "M5", "GtrR35", "Konissegge", "lamboghini", "aventador", "ferrari"]
"""
my_list.pop(1)
print(my_list)

my_list.remove("ferrari")
print(my_list)

my_list.append("Toyota V8")
print(my_list)

my_list.insert(4, "Jeep")
print(my_list)

my_list.clear()
print(my_list)

# looping through python's list
print(my_list)
for x in my_list:
	print(x, end = " ")

#Loop through the index numbers
print(my_list)
for x in range(len(my_list)):
	print(my_list[x], end = " " * 2)

print(my_list)
x = 0
while x < len(my_list):
	print(my_list[x])
	x += 1

print(my_list)
[print(x) for x in my_list]

# list comprehension in python

print(my_list)
newlist = []

for x in my_list:
	if "a" in x:
		newlist.append(x)

print(newlist)
"""
print(my_list)
newlist = [x for x in my_list if "r" in x]
print(newlist)

