class Privileges:
    def __init__(self, priv="none"):
        self.priv = priv

    def showPriv(self):
        return print(f"You have these {self.priv} privileges")