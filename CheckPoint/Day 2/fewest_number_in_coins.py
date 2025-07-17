
def fewest_number_in_coins(amount):
    quarters = amount // 25
    amount %= 25
    dimes = amount // 10
    amount %= 10
    nickels = amount // 5
    amount %= 5
    pennies = amount // 1
    output = f"{quarters} quarter, \n{dimes} dimes,\n{nickels} nickels, \n{pennies} pennies"
    return output

print(fewest_number_in_coins(73))