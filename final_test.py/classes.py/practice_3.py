# Create a Person class with name and age; add a method is_adult() returning True/False.

class Person :
    def __init__(self, name, age):
        self.name = name 
        self.age  = age 

    def is_adult(self) :
        if self.age >= 18 :
            return f"Is {self.name} adult : {True}"
        else :
            return f"Is {self.name} adult : {False}"

# p1 = Person("Maha",20)
# print(p1.is_adult())
# p2 = Person("Ria",10)
# print(p2.is_adult())