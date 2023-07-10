from menu import Menu

from coffeeMaker import CoffeeMaker
from moneyMachine import MoneyMachine


coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would u like to have {options}:")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        # latte
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            # print("sufficient")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
