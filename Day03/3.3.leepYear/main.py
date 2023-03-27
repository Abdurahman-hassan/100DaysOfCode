year = int(input("Which year do you want to check? "))

# return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year.")
    elif year % 400 == 0:
        print("Leap year.")
else:
    print("Not Leap year.")
