# Create a Car class with make, model, year; add a method info() that returns a formatted
# description string.

class Car :
    def __init__(self,make,model,year):
        self.make = make
        self.model= model
        self.year = year

    def info(self) :
        return f"Make : {self.make}\nModel: {self.model}\nYear : {self.year}"

# c1 = Car("Toyota","Corolla","2022")
# print(c1.info())