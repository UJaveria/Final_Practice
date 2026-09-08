# Write a shipping-cost calculator that considers both weight ranges and membership status together

weight = float(input("Enter weigth : "))
status = input("Enter status membership/non-membership : ")

if weight > 0 :
    if weight <= 1 and status == "non-membership" :
        shipping_cost = 150
    elif weight <= 1 and status == "membership" :
        shipping_cost = 100
    elif weight <= 3 and status == "non-membership" :
        shipping_cost = 450
    elif weight <= 3 and status == "membership" :
        shipping_cost = 400
    elif weight <= 6 and status == "non-membership" :
        shipping_cost = 750
    elif weight <= 6 and status == "membership" :
        shipping_cost = 700
    elif weight > 6 and status == "non-membership" :
        shipping_cost = 1100
    elif weight > 6 and status == "membership" :
        shipping_cost = 1000

else :
    print("Invalid Input!")
print(f"Weight : {weight}\nStatus : {status}\nShipping_cost : {shipping_cost}")
