from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calc():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    close = False

    while not close:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        first_answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {first_answer}")
        conOrCloseCheck = input("Type 'y' to cont or 'n' to start new clac or c to close.").lower()

        if conOrCloseCheck == "y":
            num1 = first_answer
        elif conOrCloseCheck == "n":
            close = True
            calc()
        else:
            close = True

calc()
