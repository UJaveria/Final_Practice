# Validate an age input: must be numeric, positive, and under 120— print a specific message for each 
# distinct kind of invalid input.

try :
    age = int(input("Enter age : "))
    if age >= 0 and age <= 120 :
        print("Entered age is valid!")
    elif age < 0 : 
        print("Age can't be negative.")
    elif age > 120 :
        print("Age can't be greater than 120.")
except  :
    print("Invalid Input!")