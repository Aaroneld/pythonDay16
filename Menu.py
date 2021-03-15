class Menu:

    def __init__(self, menuItems):
        self.menuItems = menuItems

    def get_menu_items(self):
        nameList = ''
        for x in self.menuItems:
            nameList += f' {self.menuItems[x].getName()}'
        return nameList

    def find_drink(self, order_name):
        for x in self.menuItems:
            if self.menuItems[x].getName() == order_name:
                return self.menuItems[x]
        return None
