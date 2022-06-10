print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

final_bill = 0;

if size == "S":
    final_bill += 15
elif size == "M":
    final_bill += 20
else:
    final_bill += 25

if add_pepperoni == "Y":
    if size == "S":
        final_bill += 2
    else:
        final_bill += 3

if extra_cheese == "Y":
    final_bill += 1

print(f"Your final bill is: ${final_bill}.")
