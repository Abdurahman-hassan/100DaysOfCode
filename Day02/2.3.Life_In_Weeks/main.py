age = input("What is your current age?")

if int(age) > 90 or int(age) < 0:
    print("You can't be that old or that young!")
    exit()
else:
    leftAgeInYears = 90 - int(age)
    leftAgeInMonth = leftAgeInYears * 12
    leftAgeInDays = leftAgeInYears * 365
    leftAgeInWeeks = leftAgeInYears * round(365 / 7)

print(f"You have {leftAgeInDays} days, {leftAgeInWeeks} weeks, and {leftAgeInMonth} months left.")
