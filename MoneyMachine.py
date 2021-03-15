class MoneyMachine:

    profit = 0

    def add_payment(self, amount):
        self.profit += amount
        return True

    def report(self):
        return self.profit


