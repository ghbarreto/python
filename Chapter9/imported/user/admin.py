from user import User
from priv import Privileges

class Admin(User):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.privileges = Privileges()

    def showAd(self):
        return print(f"You are not an admin {self.name} {self.last_name}")


