resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

menu = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
}

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

def check_resources(drink):
    for item in ["water", "milk", "coffee"]:
        if resources[item] < menu[drink][item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

def process_payment(cost):
    print("Insert coins.")
    total = int(input("Quarters: ")) * 0.25
    total += int(input("Dimes: ")) * 0.10
    total += int(input("Nickels: ")) * 0.05
    total += int(input("Pennies: ")) * 0.01
    return total

def make_coffee(drink):
    for item in ["water", "milk", "coffee"]:
        resources[item] -= menu[drink][item]
    resources["money"] += menu[drink]["cost"]
    print(f"Here is your {drink}. Enjoy!")

def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Machine turning off.")
            break
        elif choice == "report":
            print_report()
        elif choice in menu:
            if check_resources(choice):
                payment = process_payment(menu[choice]["cost"])
                if payment >= menu[choice]["cost"]:
                    change = round(payment - menu[choice]["cost"], 2)
                    if change > 0:
                        print(f"Here is ${change} in change.")
                    make_coffee(choice)
                else:
                    print("Sorry, not enough money. Money refunded.")
        else:
            print("Invalid choice.")
coffee_machine()
