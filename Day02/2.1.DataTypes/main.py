two_digit_number = input("Type a two digit number: ")

# Check input length
if len(two_digit_number) == 2:
    print(int(two_digit_number[0]) + int(two_digit_number[1]))
else:
    print("Invalid input you must enter a two digit number!")