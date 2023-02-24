class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class child(Parent):
    def __init__(self, name, age, id, pwd):
        self.id = id
        self.pwd = pwd
        Parent.__init__(self, name, age)

    def info(self):
        print("Details of Child: ")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.id}")


p1 = Parent("Nitin", 50)
print(f"Parent Name is {p1.name}")
print(f"Parent Age is {p1.age}")

c1 = child("Manthan", 21, 130060, "mn212")
print(f"Parent name is {p1.name} and Child name is {c1.name}")
c1.info()
