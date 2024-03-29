from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create three objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

options = menu.get_items()
choice = input(f"What would you like? ({options})")
drink = menu.find_drink(choice)
if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
    coffee_maker.make_coffee(drink)