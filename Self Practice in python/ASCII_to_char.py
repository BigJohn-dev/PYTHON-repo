# ASCII to Char


code = int(input("Enter an ASCII code (0 to 127): "));

if code >= 0 and code <= 127:
	character = chr(code)
	print(f"The character for ASCII code {code} is: '{character}'")
else:
	print("Invalid input! Please enter a number between 0 and 127.")
