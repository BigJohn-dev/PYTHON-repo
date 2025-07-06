# calculating the average miles per gallon
average = 0
user_input_count = 0
while True:
    gallons_used = float(input("Enter gallons used: "))
    miles_driven = float(input("Enter miles driven: "))
    total_gallons = miles_driven / gallons_used
    print(f"Total miles/gallons for this tank is: {total_gallons:.6f}")
    average += total_gallons
    user_input_count += 1
    end = input("Enter '-1' to quit or 5 to continue : ")
    if end == "-1":
        average /= user_input_count
        print(f"The overall average miles/gallons is: {average}")
        break
    elif end == "5":
        continue
    else:
        print("Invalid input... but carry on")
