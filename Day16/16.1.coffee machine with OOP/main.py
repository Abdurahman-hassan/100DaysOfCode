from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()

close = False

while not close:
    options = menu.get_items()
    order = input(f"What would you like? {options}:")

    if order == "off":
        close = True

    elif order == "report":
        coffeeMaker.report()
        moneyMachine.report()

    else:
        drink = menu.find_drink(order)
        if coffeeMaker.is_resource_sufficient(drink):
            if moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
