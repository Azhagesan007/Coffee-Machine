

class MenuItem:
    """Menu Item of coffee machine."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=200,),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=150),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=300),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name} - ₹{item.cost}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                # print("yes")
                # print(item.name)

                return item.name
        print("Sorry that item is not available.")

    def find_cost(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                # temp = int(item.cost)
                # temp = "success"
                return item.cost
        # print

    def find_resource(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        required = []
        for item in self.menu:
            if item.name == order_name:
                # temp = int(item.cost)
                # temp = "success"
                for key in [item.ingredients["water"], item.ingredients["coffee"], item.ingredients["milk"]]:

                    required.append(key)

                return required
