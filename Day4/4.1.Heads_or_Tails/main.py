import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

rand_num = random.randint(0, 1)

if rand_num == 0:
    print("Tails")
else:
    print("Heads")
