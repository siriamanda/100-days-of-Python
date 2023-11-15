from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects from classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    options = menu.get_items()
    coffee_order = input(f"What would you like? ({options}): ").lower()

    if coffee_order == "off":
        machine_on = False

    elif coffee_order == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(coffee_order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
