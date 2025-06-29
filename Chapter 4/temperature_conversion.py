#Temperature Conversion

def fahrenheit(celsius):
    return (9/5) * celsius + 32

print("Celsius \tFahrenheit")
for c in range(0, 101):
	f = fahrenheit(c)
	print(f"{c:>6}, {f:>15.2f}")