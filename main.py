from resources import MENU
from resources import resources



def check_resource(users_coffee):
    if users_coffee == "espresso":
        if resources["water"] > MENU[users_coffee]["ingredients"]["water"]:
            if resources["coffee"] > MENU[users_coffee]["ingredients"]["coffee"]:
                print(f"**{users_coffee} can be made**")
                return True
            else:
                print("sorry, not enough coffee...")
                return False
        else:
            print("sorry, not enough water...")
    elif users_coffee == "latte" or "cappuccino":
        if resources["water"] > MENU[users_coffee]["ingredients"]["water"]:
            if resources["coffee"] > MENU[users_coffee]["ingredients"]["coffee"]:
                if resources["milk"] > MENU[users_coffee]["ingredients"]["milk"]:
                    print(f"**{users_coffee} can be made**")
                    return True
                else:
                    print("sorry, not enough milk...")
                    return False
            else:
                print("sorry, not enough coffee...")
                return False
        else:
            print("sorry, not enough water...")
            return False


def report():
    if users_coffee == "report":
        print(f"Water left in machine is {resources['water']}")
        print(f"Milk left in machine is {resources['milk']}")
        print(f"Coffee left in machine is {resources['coffee']}")


def money_inserted(quarters, dimes, nickles, pennies):
    return round((0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies))


def resources_left():
    if users_coffee == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    elif users_coffee == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
    elif users_coffee == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24


profit = 0

machine_on = True

while machine_on:

    users_coffee = input("What would you like?(espresso/latte/cappuccino):")
    if users_coffee == "report":
        report()
    elif users_coffee == "off":
        print("Shutting down...")
        machine_on = False
    else:
        if check_resource(users_coffee):
            print(f"for {users_coffee} please pay {MENU[users_coffee]['cost']} $")
            quarters = int(input("how many quarters you want to insert? "))
            dimes = int(input("how many dimes you want to insert? "))
            nickles = int(input("how many nickles you want to insert? "))
            pennies = int(input("how many pennies you want to insert? "))
            total_money = (money_inserted(quarters, dimes, nickles, pennies))
            if total_money > MENU[users_coffee]['cost']:
                change_back = total_money - MENU[users_coffee]['cost']
                print(f"you have inserted total {total_money} $, here's your change back {change_back} $")
                print(f"Making your {users_coffee}, please wait...")
                print("*-*-*-*-*-*-*-*-*-*")
                print(f"here's your {users_coffee}, enjoy")
                change = (total_money - change_back)
                profit += change
                resources_left()
                print(f"profit is {profit}")
            elif total_money < MENU[users_coffee]['cost']:
                print(f"you have inserted only total of {total_money} $")
                print("**not enough money**")
