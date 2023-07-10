class CoffeeMaker:
    """programs related to resources"""

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        for key in self.resources:
            print(f"{key}: {self.resources[key]}ml")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if (drink.ingredients[item] > self.resources[item]):
                print(f"Sorry there isn't enough of the {item}.")
                can_make = False

        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

        print(f"Here is your order {order.name} ☕️. Enjoy!")
