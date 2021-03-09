from restaurant import Restaurant

class IceCreamStand(Restaurant):

    def __init__ (self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavours = ['Vanilla', 'Chocolate', 'Strawberry']

    def order(self):
        for i in self.flavours:
            print(f"These are our flavours {i}")
    
        


