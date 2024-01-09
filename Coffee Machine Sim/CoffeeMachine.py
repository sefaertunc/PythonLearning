from prettytable import PrettyTable

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_process_over = False
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

def make_table():
    table = PrettyTable()
    table.add_column("Coffee Types", ["Espresso", "Latte", "Cappuccino"])
    table.add_column("Price", ["1.50$", "2.50$", "3.00$"])
    print(table)


def request_check(user_input):
    global is_process_over
    if user_input == "report":
        money_machine.report()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    elif user_input == "off":
        print("Machine is closing!")
        is_process_over = True
    else:
        print("Invalid Input!")


make_table()


while not is_process_over:
    request = input("What would you like? (espresso/latte/cappuccino) ").lower()
    request_check(request)
