class MenuItem:

    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

    def __str__(self):
        print(self.name)
        print(self.cost)
        print(self.ingredients)

    def get_name(self):
        return self.name