# Create a list of 5 grocery items, add two more, then remove one by name.
grocery_items = ["Breads","Rice","Eggs","Milk","Pasta"]
grocery_items.append("Cheese")
grocery_items.append("Honey")

print(f"grocer         : {grocery_items}")
# removing item
grocery_items.remove("Eggs")
print(f"After removing : {grocery_items}")