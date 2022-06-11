import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# the easiest way

# # Michael is going to buy the meal today!
# choice_Name = random.choice(names)
# print(f"{choice_Name} is going to buy the meal today!")

# another way

random_index = random.randint(0, len(names) - 1)

print(f"{names[random_index]} is going to buy the meal today!")
