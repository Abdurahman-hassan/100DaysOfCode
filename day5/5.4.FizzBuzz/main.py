# 3 Fizz
# 5 Buzz

# 3 and 5 FizzBuzz

for n in range(1, 101):

    if n % 3 == 0 and n % 5 != 0:
        print("Fizz")
    elif n % 5 == 0 and n % 3 != 0:
        print("Buzz")
    elif n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")

    else:
        print(n)
