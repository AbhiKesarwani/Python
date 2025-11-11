MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

money_is_ok = True
def money(user_coffee):
    """money checker"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    if total_money > MENU[user_coffee]["cost"]:
        print(f"Here is ${round(total_money-MENU[user_coffee]["cost"],2)} in change🤑.")
        report(user_coffee)
    elif total_money == MENU[user_coffee]["cost"]:
       report(user_coffee)
    else:
        print(f"Sorry that's not enough money.")
        global money_is_ok
        money_is_ok = False

def resource_checker(user_coffee):
    """Check available resource"""
    resource_list = [resources["water"],resources["milk"],resources["coffee"],resources["money"]]
    count=0
    for resource in resource_list:
       if resource>=0:
           count+=1
       else:
           print(f"Sorry there is not enough resource in coffee machine to make coffee.")
           print("Money refunded🤑.")
           global machine_is_on
           machine_is_on = False
           break
    if count==4 and money_is_ok:
        print(f"Here is your {user_coffee}☕.Enjoy!")

def report(user_coffee):
    """reduce resource after a successful coffe is made"""
    resources["water"] = resources["water"] - MENU[user_coffee]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[user_coffee]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[user_coffee]["ingredients"]["coffee"]
    resources["money"] = resources["money"] + MENU[user_coffee]["cost"]




machine_is_on = True
print('''.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     ______   | || |     ____     | || |  _________   | || |  _________   | || |  _________   | || |  _________   | | | | ____    ____ | || |      __      | || |     ______   | || |  ____  ____  | || |     _____    | || | ____  _____  | || |  _________   | |
| |   .' ___  |  | || |   .'    `.   | || | |_   ___  |  | || | |_   ___  |  | || | |_   ___  |  | || | |_   ___  |  | | | ||_   \  /   _|| || |     /  \     | || |   .' ___  |  | || | |_   ||   _| | || |    |_   _|   | || ||_   \|_   _| | || | |_   ___  |  | |
| |  / .'   \_|  | || |  /  .--.  \  | || |   | |_  \_|  | || |   | |_  \_|  | || |   | |_  \_|  | || |   | |_  \_|  | | | |  |   \/   |  | || |    / /\ \    | || |  / .'   \_|  | || |   | |__| |   | || |      | |     | || |  |   \ | |   | || |   | |_  \_|  | |
| |  | |         | || |  | |    | |  | || |   |  _|      | || |   |  _|      | || |   |  _|  _   | || |   |  _|  _   | | | |  | |\  /| |  | || |   / ____ \   | || |  | |         | || |   |  __  |   | || |      | |     | || |  | |\ \| |   | || |   |  _|  _   | |
| |  \ `.___.'\  | || |  \  `--'  /  | || |  _| |_       | || |  _| |_       | || |  _| |___/ |  | || |  _| |___/ |  | | | | _| |_\/_| |_ | || | _/ /    \ \_ | || |  \ `.___.'\  | || |  _| |  | |_  | || |     _| |_    | || | _| |_\   |_  | || |  _| |___/ |  | |
| |   `._____.'  | || |   `.____.'   | || | |_____|      | || | |_____|      | || | |_________|  | || | |_________|  | | | ||_____||_____|| || ||____|  |____|| || |   `._____.'  | || | |____||____| | || |    |_____|   | || ||_____|\____| | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  ''')

while machine_is_on:
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if user_coffee=="espresso" or user_coffee=="latte" or user_coffee=="cappuccino":
        money(user_coffee)
        resource_checker(user_coffee)
    elif user_coffee.lower()=="off":
        machine_is_on = False
    elif user_coffee.lower()=="report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")
    else:
        print("Invalid Input,Machine is off now.")
        machine_is_on = False




'''
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

'''