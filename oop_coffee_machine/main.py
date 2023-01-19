from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()


def main():

    # Initialize values
    end_program = False

    # While loop to keep program running
    while not end_program:

        # Loop to prompt user and ensure correct input is submitted
        while True:
            order = input(f'What would you like? ({menu.get_items()}): ')
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
                coffee_machine.report()
                money_machine.report()
                break
        else:
            drink = menu.find_drink(order)
            
        # Ensure that there are enough resources for order first and if not state what is missing
        if not coffee_machine.is_resource_sufficient(drink):
            end_program = True
        else:
            cost = drink.cost

            if money_machine.make_payment(cost):
                coffee_machine.make_coffee(drink)
                
main()
