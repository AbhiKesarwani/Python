from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
money_machine = MoneyMachine()
coffee_make = CoffeeMaker()


is_machine_on = True
while is_machine_on:
    print("Welcome to coffee machine")
    option = menu.get_items()
    order = input(f"What drink you want to purchase {option}: ")
    order_in = menu.find_drink(order)
    if order == "off":
        is_machine_on = False
    elif order == "report":
        coffee_make.report()
        money_machine.report()
    elif money_machine.make_payment(order_in.cost) and coffee_make.is_resource_sufficient(order_in):
        coffee_make.make_coffee(order_in)