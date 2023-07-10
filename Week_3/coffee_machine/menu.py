
class MenuItem:
    """defines the menu items """

    def __init__(self, name, cost, water, coffee, milk):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "coffee": coffee,
            "milk": milk
        }

# menu
# multiple menu items


class Menu:
    "Defines the menu"

    def __init__(self):
        self.menu = [
            MenuItem("latte", 2.5, 200, 24, 150),
            MenuItem("espresso", 1.5, 50, 18, 0),
            MenuItem("cappuccino", 3, 250, 24, 50),
        ]

    def get_items(self):
        """returns the name of items in the menu"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if (item.name == order_name):
                return item
        else:
            print("This item is not in menu")
