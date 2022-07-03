def prime_checker(number):
    isPrime = True
    for n in range(2, number):
        if number % n == 0:
            isPrime = False

    if isPrime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
