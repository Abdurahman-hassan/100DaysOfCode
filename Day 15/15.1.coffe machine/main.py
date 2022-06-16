from data import MENU, resources

def report_formatting(money):
    return f"Water: {availble_Water}ml\nMilk: {availble_Milk}ml\nCoffee: {availble_Coffee}g\nMoney: ${money}"

def resources_sufficient(order):
    if order != "report" and order != "off":

        availble_Water = resources["water"]
        availble_Milk = resources["milk"]
        availble_Coffee = resources["coffee"]
        MilkNeeds = 0

        WaterNeeds = MENU[order]["ingredients"]["water"]
        CoffeNeeds = MENU[order]["ingredients"]["coffee"]
        if order != "espresso":
            MilkNeeds = MENU[order]["ingredients"]["milk"]

        if transaction == True:
            availble_Water -= WaterNeeds
            availble_Coffee -= CoffeNeeds
            if order != "espresso":
                availble_Milk -= MilkNeeds

        # return True if sufficient or False

        if WaterNeeds > availble_Water:
            print("Sorry there is not enough water")
        elif CoffeNeeds > availble_Coffee:
            print("Sorry there is not enough coffee")
        elif MilkNeeds > availble_Milk and order != "espresso":
            print("Sorry there is not enough Milk")
        else:
            return True


def processCoins(quarters, dimes, nickles, pennies):
    quartersFees = float((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies))
    return quartersFees


machineON = True
change = 0
money = 0

availble_Water = resources["water"]
availble_Milk = resources["milk"]
availble_Coffee = resources["coffee"]

transaction = False

while machineON:

    order = input("What would you like? (espresso/latte/cappuccino)")
    # TODO: Turn off the Coffee Machine by entering “off” to the prompt.

    if order == "off":
        machineON = False
    elif order == "report":
        print(report_formatting(money))

    # TODO: Check transaction successful?
    checking = resources_sufficient(order)
    if checking == True:
        print("Please insert coins.")
        quarters = float(input("how many quarters?:"))
        dimes = float(input("how many quarters?:"))
        nickles = float(input("how many quarters?:"))
        pennies = float(input("how many quarters?:"))

        fees = processCoins(quarters, dimes, nickles, pennies)
        if fees < MENU[order]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            # transaction is success
            transaction = True
            availble_Water -= MENU[order]["ingredients"]["water"]
            availble_Coffee -= MENU[order]["ingredients"]["coffee"]
            if order != "espresso":
                availble_Milk -= MENU[order]["ingredients"]["milk"]
            change = round(fees - MENU[order]["cost"], 2)
            money += MENU[order]["cost"]
            print(f"Here is ${change} in change.")
            print(f"Here is your {order} ☕️.Enjoy!")

