from data import menu, resources


def main():

    # Initialize values
    end_program = False
    report = {}
    money = 0

    # Loop to add resource values to report
    for resource in resources:
        report[resource] = resources[resource]

    # Include money in report dictionary
    report['money'] = 0

    # While loop to keep program running
    while not end_program:

        # Loop to prompt user and ensure correct input is submitted
        while True:
            order = input('What would you like? (espresso/latte/cappuccino): ')
            if order not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
                print('Please enter a valid order.')
            else:
                break

        # Catch if a command was given rather than an order
        if order in ['off', 'report']:
            command = order
            if command == 'off':
                break
            elif command == 'report':
                print(report)
                break

        # Ensure that there are enough resources for order first and if not state what is missing
        for resource in resources:
            if resources[resource] < 0:
                print(f'Sorry there is not enough {resource} for this order.')
                end_program = True

        if end_program:
            break

        # Values returned from transaction function
        brew, change, profit = transaction(order)

        # Based on a false brew value, if customer did not submit enough coins
        if not brew:
            print(f'Sorry the ${change} you gave is less than the ${profit}.')
        else:
            # If customer submitted enough coins then the make_coffee function is initiated
            make_coffee(order)

            # Update report resources and money
            for resource in resources:
                report[resource] = resources[resource]
            money += profit
            report['money'] = money
            if change > 0:
                print(f'Here is your {order} and ${change:.2f} dollars in change. Enjoy!')
                #end_program = True
            else:
                print(f'Here is your {order}, enjoy!')
                #end_program = True


# This function will make the order the user inputted and will also update the resources
def make_coffee(order):
    water_needed = menu[order]['ingredients']['water']
    milk_needed = menu[order]['ingredients']['milk']
    coffee_needed = menu[order]['ingredients']['coffee']

    resources['water'] -= water_needed
    resources['milk'] -= milk_needed
    resources['coffee'] -= coffee_needed


# This function will take the users order and process the transaction based on the number of coins given
def transaction(order):
    cost = menu[order]['cost']

    print(f'Your total is ${cost}.')

    while True:
        try:
            quarters = float(input('Quarters: '))
            dimes = float(input('Dimes: '))
            nickles = float(input('Nickles: '))
            pennies = float(input('Pennies: '))
        except ValueError:
            print('Please enter valid amounts.')
        else:
            break

    amount_given = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)

    if amount_given < cost:
        return False, amount_given, cost
    elif amount_given == cost:
        change = 0
        return True, change, cost
    else:
        change = amount_given - cost
        return True, change, cost


main()
