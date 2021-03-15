class CoffeeMaker:

    def __int__(self, menu, resources, moneyMachine):
        self.menu = menu
        self.resources = resources
        self.moneyMachine = moneyMachine

    def report(self):
        print(self.resources)

    def is_resource_sufficient(self, menuItem):
        for ingredient in menuItem.ingredients:
            if self.resources[ingredient] < menuItem.ingredients[ingredient]:
                return False
        return True

    def make_coffee(self, order):
        if self.is_resource_sufficient(order):
            for ingredient in order.ingredients:
                self.resources[ingredient] -= order.ingredients[ingredient]
            self.moneyMachine.add_payment(order.cost)
            return f'Here is your {order.name}!'
