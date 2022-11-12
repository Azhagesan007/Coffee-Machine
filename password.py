class Password:
    """User Login credential"""
    def __init__(self):
        self.enter = {
            "007": {
                "Name": "Azhagesan",
                "Password": "7732",
            },
            "143": {
                "Name": "R&D",
                "Password": "77088"
            },
            "7776": {
                "Name": "Bala Chandran",
                "Password": "4354"
            },
            "369": {
                "Name": "Kalai Selvi",
                "Password": "963"
            }
        }


class Login:
    """User Login"""

    def __init__(self):
        self.password = Password()

    def user_login(self, user):
        temp = self.password
        enter = temp.enter
        temp_pass = enter.get(user, "None")
        if temp_pass == "None":
            print("No User Found")
            input("Press 'ENTER' to continue")
            return "no"
        else:
            name = enter[user]["Name"]
            pin = enter[user]["Password"]
            temp_pin = input(f"Welcome {name}\nPlease enter your pin no:\n")
            if temp_pin == pin:
                print("login Successful")
                print("What do you want to do?")
                comment = input("Off the machine or put the machine under maintenance:\n").lower()
                # if comment == "maintenance":
                #     return main
                # elif comment == "off":
                #     return "off"
                return comment
            else:
                print("wrong password")
                input("Press 'ENTER' to continue")
