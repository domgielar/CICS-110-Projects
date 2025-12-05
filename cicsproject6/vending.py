# Author   : Dominik Gielarowiec    
# Email    : digelarowiec@umass.edu 
# Spire ID : 35150500


class VendingMachine:
    def __init__(self):
        self.vend = {}
    def add_item(self, name, price, quantity):
        self.vend[name] = {
            "price": price,
            "quantity": quantity,
            
        }
        print(self.vend)