MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18, },
        "cost": 1.5, },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24, },
        "cost": 2.5, },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24, },
        "cost": 3.0, }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0}

# Value of coins

quarter_value = 0.25
dime_value = 0.1
nickle_value = 0.05
penny_value = 0.01

# Functions


def print_report():
    print(f"Water: {resources["water"]}ml\n"
          f"Milk: {resources["milk"]}ml\n"
          f"Coffee: {resources["coffee"]}ml\n"
          f"Money: ${resources["money"]}")


def check_resources(machine_order):
    order = MENU[machine_order]
    required_ingredients = order["ingredients"]
    make_coffee = True

    required_coffee = required_ingredients["coffee"]
    required_water = required_ingredients["water"]

    if required_coffee > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        make_coffee = False
    elif required_water > resources["water"]:
        print("Sorry there is not enough water.")
        make_coffee = False

    if machine_order == "latte" or machine_order == "cappuccino":
        required_milk = required_ingredients["milk"]
        if required_milk > resources["milk"]:
            print("Sorry there is not enough milk.")
            make_coffee = False

    return make_coffee


def reduce_resources(machine_order):
    order = MENU[machine_order]
    required_ingredients = order["ingredients"]

    required_coffee = required_ingredients["coffee"]
    required_water = required_ingredients["water"]

    resources["coffee"] -= required_coffee
    resources["water"] -= required_water

    if machine_order == "latte" or machine_order == "cappuccino":
        required_milk = required_ingredients["milk"]
        resources["milk"] -= required_milk

    return resources


def process_coins(quarter, dime, nickle, penny):
    sum_quarters = quarter_value * quarter
    sum_dimes = dime_value * dime
    sum_nickles = nickle_value * nickle
    sum_pennies = penny_value * penny
    sum_amount = sum_quarters + sum_dimes + sum_nickles + sum_pennies
    return sum_amount


def process_transaction(amount_received, machine_order):
    order = MENU[machine_order]
    order_amount = order["cost"]
    transaction_processed = True
    if amount_received < order_amount:
        print("Sorry that's not enough money. Money refunded.")
        transaction_processed = False
    elif amount_received > order_amount:
        change = round(amount_received - order_amount, 2)
        print(f"Here is ${change} dollars in change.")
        resources["money"] += order_amount
    elif amount_received == order_amount:
        resources["money"] += order_amount
    return transaction_processed


# Coffee machine
machine_on = True

while machine_on:

    coffee_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_order == "report":
        print_report()

    elif coffee_order == "off":
        machine_on = False

    else:
        resource_check = check_resources(coffee_order)

        if resource_check is True:

            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            paid_amount = process_coins(quarters, dimes, nickles, pennies)

            money_processed = process_transaction(paid_amount, coffee_order)

            if money_processed is True:

                resources = reduce_resources(coffee_order)

                print(f"Here is your {coffee_order}.")
