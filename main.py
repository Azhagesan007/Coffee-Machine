from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from password import Login
from art import logo
import subprocess
login = Login()
start = True
menu = Menu()
menulist = menu.get_items()
coffee = CoffeeMaker()
money = MoneyMachine()
temp_water = 0
temp_coffee = 0
temp_milk = 0


def cls():
    subprocess.run('cls', shell=True)


while start:
    cls()
    print(logo)
    menulist = menu.get_items()
    choice = input(f"What do you want from this {menulist}:\n").lower()
    if choice == "report":
        cls()
        print(logo)
        coffee.report()
        money.report()
        input("Press 'ENTER' to continue")
    elif choice == "login":
        cls()
        print(logo)
        user = input("Enter user id:\n")
        status = login.user_login(user)
        if status == "off":
            cls()
            break
        elif status == "maintenance":
            cls()
            input("Press 'ENTER' to turn off the maintenance")

    else:
        choice = menu.find_drink(choice)
        # print(choice)
        if choice is None:
            # start = False
            input("Press 'ENTER' to continue")
            continue
            # break
        else:
            # print(choice)
            required = menu.find_resource(choice)
            stock = coffee.is_resource_sufficient(choice, required)
            # price = MenuItem(choice)
            price = menu.find_cost(choice)
            # print(type(price))
            if stock:

                last = money.make_payment(price)
                # required = menu.find_resource(choice)
                if last:
                    coffee.make_coffee(choice, required)
