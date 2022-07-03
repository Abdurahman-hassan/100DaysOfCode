age = input("What is your current age?")

leftAgeInYeasrs= 90 - int(age)
leftAgeInMonth = leftAgeInYeasrs * 12
leftAgeInDays = leftAgeInYeasrs * 365
leftAgeInWeeks = leftAgeInYeasrs * round(365/7)


print(f"You have { leftAgeInDays } days, { leftAgeInWeeks } weeks, and {leftAgeInMonth } months left.")
