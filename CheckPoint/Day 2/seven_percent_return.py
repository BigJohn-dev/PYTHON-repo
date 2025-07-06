# calculating IOR on 7% returns

principal = 1000
rate = 0.07
number_of_years = 0

for year in range(1, 31):
    amount = 0
    for t in range(0, 21, 10):
        if year >= t:
            amount += principal * (1 + rate) ** (year - t)
    print(f"Year {year}: {amount:.2f}")
