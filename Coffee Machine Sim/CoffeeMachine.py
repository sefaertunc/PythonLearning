from CoffeeMach_Data import MENU
from CoffeeMach_Data import RESOURCES
from prettytable import PrettyTable

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = 0
is_process_over = False


def identify_inserted_coins(q, d, n, p):
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nick = int(input("How many nickles?: "))
    penn = int(input("How many pennies?: "))
    return quarter * q + dime * d + nick * n + penn * p


def activate_operator(inserted_coins, userinput):
    global money
    cost = MENU[userinput]["cost"]
    if inserted_coins >= cost:
        earned = cost
        exchange = inserted_coins - earned
        money += earned
        if exchange > 0:
            print(f"Here is ${exchange:.2f} in change.")
        make_coffee(userinput)
    else:
        print("Sorry that's not enough money. Money refunded.")


def check_sources(userinput):
    for ingredient in MENU[userinput]["ingredients"]:
        if MENU[userinput]["ingredients"][ingredient] > RESOURCES[ingredient]:
            return False
    return True


def make_coffee(userinput):
    for ingredient in MENU[userinput]["ingredients"]:
        RESOURCES[ingredient] -= MENU[userinput]["ingredients"][ingredient]
    print(f"Here is your {userinput} ☕ Enjoy!")


def request_check(user_input):
    global is_process_over
    if user_input == "report":
        var_dic = RESOURCES
        for i in var_dic:
            print(i + ": " + f"{var_dic[i]}")
        print("money= $" + str(money))
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if check_sources(user_input):
            inserted = identify_inserted_coins(0.25, 0.1, 0.05, 0.01)
            activate_operator(inserted, user_input)
        else:
            print("Sorry, we don't have enough source")
            return
    elif user_input == "off":
        print("Machine is closing!")
        is_process_over = True
    else:
        print("Invalid Input!")


table = PrettyTable()
table.add_column("Coffee Types", ["Espresso", "Latte", "Cappuccino"])
table.add_column("Price", ["1.50$", "2.50$", "3.00$"])
print(table)


while not is_process_over:
    request = input("What would you like? (espresso/latte/cappuccino) ").lower()
    request_check(request)
