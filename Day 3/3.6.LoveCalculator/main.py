print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

full_name = name1+name2
name_lower = full_name.lower()
checkTheFirstName = name_lower.count('t') + name_lower.count('r')+name_lower.count('u') + name_lower.count('e')
checkTheLastName = name_lower.count('l') + name_lower.count('o')+name_lower.count('v') + name_lower.count('e')

name_combain = str(checkTheFirstName)+str(checkTheLastName)

if int(name_combain) < 10 or int(name_combain) > 90:
    print(f"Your score is {name_combain}, you go together like coke and mentos.")
elif int(name_combain) >= 40 and int(name_combain) <=50:
    print(f"Your score is {name_combain}, you are alright together.")
else:
    print(f"Your score is {name_combain}.")
