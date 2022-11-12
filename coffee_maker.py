class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink ,required):
        """Returns True when order can be made, False if ingredients are insufficient."""
        i = 0
        can_make = True
        for item in ["water", "coffee", "milk"]:
            if required[i] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
            i += 1
        return can_make

    def make_coffee(self, order, required):
        """Deducts the required ingredients from the resources."""
        i = 0
        for item in ["water", "coffee", "milk"]:
            self.resources[item] -= required[i]
            i += 1
        print(f"Here is your {order} ☕️. Enjoy!")
        input("Press 'ENTER' to continue")
