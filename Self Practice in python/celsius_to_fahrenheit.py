# celsius To Fahrenheit
class celsiusToFahrenheit:

	def fahrenheit(celsius):
		fahrenheit = (9.0 / 5.0) * celsius + 32
		return f"{celsius} Celsius is {fahrenheit} Fahrenheit"

degree = float(input("Enter a degree in celsius: "))
print(celsiusToFahrenheit.fahrenheit(degree))
