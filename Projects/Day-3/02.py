class Person:

    def __init__(self,name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def showData(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old. I live in {self.address}.")

p = Person("Jhon Doe",30,"123 Main Street")
p.showData()