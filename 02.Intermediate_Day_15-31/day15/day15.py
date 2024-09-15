MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_on = True
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0


def report():
    """Shows the resources"""
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


# todo need to learn function more check day 15, 14, 12, 11
# def record_resource(command):
#     coffee -= MENU[command]['ingredients']['coffee']
#     money += MENU[command]['cost']
#     water -= MENU[command]['ingredients']['water']
#     milk -= MENU[command]['ingredients']['milk']

# todo need to learn function more check day 15, 14, 12, 11
# def resource_check(water, milk, coffee):
#     if water < MENU[command]['ingredients']['water']:
#         print("not enough water. try again later")
#     elif coffee < MENU[command]['ingredients']['coffee']:
#         print("not enough coffee. try again later")
#     elif milk < MENU[command]['ingredients']['milk']:
#         print("not enough milk. try again later")


def coin_calc():
    """calculate change"""
    print('Please insert coins')
    quarters = float(input('How many quarters?: '))*0.25
    dimes = float(input('How many dimes?: '))*0.10
    nickles = float(input('How many nickles?: '))*0.05
    pennies = float(input('How many pennies?: '))*0.01
    total_f = quarters + dimes + nickles + pennies
    return total_f


while machine_on:
    command = input("Welcome. What would you like? (espresso/latte/cappuccino): ").lower()

    if command == 'report':
        report()
    elif command == 'off':
        machine_on = False
    elif command == 'espresso':
        if water < MENU[command]['ingredients']['water']:
            print("not enough water. try again later")
        elif coffee < MENU[command]['ingredients']['coffee']:
            print("not enough coffee. try again later")
        else:
            total = coin_calc()
            if total < MENU[command]['cost']:
                print('Sorry that\'s not enough money. Money refunded.')
            else:
                change = round(total - MENU[command]['cost'], 2)
                print(f'Here is ${change} in change. ')
                print(f'Here is your {command}☕😊. Enjoy! ')

                money += MENU[command]['cost']
                water -= MENU[command]['ingredients']['water']
                coffee -= MENU[command]['ingredients']['coffee']
    elif command == 'latte':
        if water < MENU[command]['ingredients']['water']:
            print("not enough water. try again later")
        elif coffee < MENU[command]['ingredients']['coffee']:
            print("not enough coffee. try again later")
        elif milk < MENU[command]['ingredients']['milk']:
            print("not enough milk. try again later")
        else:
            total = coin_calc()
            if total < MENU[command]['cost']:
                print('Sorry that\'s not enough money. Money refunded.')
            else:
                change = round(total - MENU[command]['cost'], 2)
                print(f'Here is ${change} in change. ')
                print(f'Here is your {command}😊☕. Enjoy! ')

                money += MENU[command]['cost']
                water -= MENU[command]['ingredients']['water']
                milk -= MENU[command]['ingredients']['milk']
                coffee -= MENU[command]['ingredients']['coffee']
    elif command == 'cappuccino':
        if water < MENU[command]['ingredients']['water']:
            print("not enough water. try again later")
        elif coffee < MENU[command]['ingredients']['coffee']:
            print("not enough coffee. try again later")
        elif milk < MENU[command]['ingredients']['milk']:
            print("not enough milk. try again later")
        else:
            total = coin_calc()
            if total < MENU[command]['cost']:
                print('Sorry that\'s not enough money. Money refunded.')
            else:
                change = round(total - MENU[command]['cost'], 2)
                print(f'Here is ${change} in change. ')
                print(f'Here is your {command}☕😊. Enjoy! ')

                money += MENU[command]['cost']
                water -= MENU[command]['ingredients']['water']
                milk -= MENU[command]['ingredients']['milk']
                coffee -= MENU[command]['ingredients']['coffee']
    else:
        print('Invalid command. Please type again.')
