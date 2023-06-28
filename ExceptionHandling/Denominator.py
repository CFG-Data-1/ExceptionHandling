
denominator = int(input("Please eneter a number to divide by: "))

try:
    division_result = 100 / denominator
    print(division_result)

except ZeroDivisionError:
    print("You cannot divide by 0, please try gain")
