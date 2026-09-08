# Design an Inventory class storing items in an internal dict, with add_item, remove_item,
# total_value, and a __str__ that prints a formatted receipt-style summary of every item and	its
# subtotal

class Inventory :
    def __init__(self):
        self.inventory_dict = {"Watch" : 5000}

    def add_items(self, item, price) :
        self.inventory_dict.update({item : price})
        return self.inventory_dict

    def remove_item(self,item) :
        try :
            self.inventory_dict.pop(item)
            return self.inventory_dict
        except :
            return "Item does not exist"

    def total_value(self) :
        totals = 0
        for key,val in self.inventory_dict.items() :
            totals += val
        return f"{totals}"

    def __str__(self):
        print("===== RECEIPT =====")
        for key,val in self.inventory_dict.items() :
            print(key,":",val)
        print("-------------------")
        print(f"Subtotals : {self.total_value()}")
    
# i1 = Inventory()
# print(i1.add_items("Phone",50000))
# print(i1.add_items("Laptop",150000))
# print(i1.remove_item("Laptop"))
# print(i1.total_value())
# i1.__str__()