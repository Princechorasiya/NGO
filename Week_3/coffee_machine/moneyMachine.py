class MoneyMachine:

    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):

        print(f"Money: ${self.profit}")

    def process_money(self):
        print("Please enter the coins")
        for coin in self.COIN_VALUES:
            self.money_received += int(
                input(f"How many {coin}? ")) * self.COIN_VALUES[coin]

        return self.money_received

    def make_payment(self, cost):
        # ask for payment coin
        self.process_money()
        # check if money is sufficient
        if (self.money_received >= cost):
            change = round(self.money_received-cost, 2)

            print(f"Here is {self.CURRENCY}{change} in change.")
            self.money_received = 0
            self.profit += cost
            return True

        print("Sorry that's not enough money.Money refunded")
        self.money_recieved = 0
        return False
