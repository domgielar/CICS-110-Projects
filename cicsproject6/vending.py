# Author   : Dominik Gielarowiec    
# Email    : digelarowiec@umass.edu 
# Spire ID : 35150500


class VendingMachine:
    def __init__(self):
        self.vend = {}
        self.balance = 0.0
        self.total_sales = 0.0
        self.sales_history = []

    def add_item(self, name, price, quantity):
        if name in self.vend:
            new_quantity = self.vend[name]["quantity"] + quantity
        else:
            new_quantity = quantity
        self.vend[name] = {
            "price": price,
            "quantity": new_quantity,}
        print(f"{quantity} {name}(s) added to inventory")

    def get_item_price(self, name):
        if name not in self.vend:
            print("Invalid item")
            return None
        return self.vend[name]["price"]

    def get_item_quantity(self, name):
        if name not in self.vend:
            print("Invalid item")
            return None
        return self.vend[name]["quantity"]

    def list_items(self):
        if not self.vend:
            print("No items in the vending machine")
            return
        print("Available items:")
        for item in sorted(self.vend.keys()):
            price = self.vend[item]["price"]
            qty = self.vend[item]["quantity"]
            print(f"{item} (${price}): {qty} available")

    def insert_money(self, amount):
        if amount in (1.0, 2.0, 5.0):
            self.balance = round(self.balance + amount, 2)
            print(f"Balance: {self.balance}")
        else:
            print("Invalid amount")

    def purchase(self, name):
        if name not in self.vend:
            print("Invalid item")
            return
        price = self.vend[name]["price"]
        qty = self.vend[name]["quantity"]
        if qty == 0:
            print(f"Sorry {name} is out of stock")
            return
        if self.balance < price:
            print(f"Insufficient balance. Price of {name} is {price}")
            return
        self.vend[name]["quantity"] -= 1
        self.balance = round(self.balance - price, 2)
        self.total_sales = round(self.total_sales + price, 2)
        self.sales_history.append((name, price))
        print(f"Purchased {name}")
        print(f"Balance: {self.balance}")

    def output_change(self):
        if self.balance > 0:
            print(f"Change: {self.balance}")
            self.balance = 0.0
        else:
            print("No change")

    def remove_item(self, name):
        if name not in self.vend:
            print("Invalid item")
            return
        del self.vend[name]
        print(f"{name} removed from inventory")

    def empty_inventory(self):
        self.vend.clear()
        print("Inventory cleared")

    def get_total_sales(self):
        return self.total_sales

    def stats(self, N):
        if not self.sales_history:
            print("No sale history in the vending machine")
            return
        records = self.sales_history[-N:]
        count = len(records)
        print(f"Sale history for the most recent {count} purchase(s):")
        summary = {}
        for item, price in records:
            if item not in summary:
                summary[item] = {"count": 0, "total": 0.0}
            summary[item]["count"] += 1
            summary[item]["total"] = round(summary[item]["total"] + price, 2)
        for item in sorted(summary.keys()):
            total = summary[item]["total"]
            c = summary[item]["count"]
            print(f"{item}: ${total} for {c} purchase(s)")
