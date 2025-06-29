# calculating IOR on 7% returns

principal = 1000
rate = 0.07
number_of_years = 0

while number_of_years <= 20:
    amount = principal * (1 + rate) ** number_of_years
    number_of_years += 10
    print(f"The amount on deposit after {number_of_years} years is {amount:.2f}")