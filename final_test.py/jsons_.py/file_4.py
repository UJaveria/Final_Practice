# Given a JSON file of orders (each with an id, item, amount), load it and compute the total amount across
# all orders.

import json

total = 0
with open("orders.json","r") as file : 
    data = json.load(file)
    for dic in data :
        total += dic["amount"]
print(f"Total amount : {total}")