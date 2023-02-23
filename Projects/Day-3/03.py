class Person:

    def __init__(self,name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def showData(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old. I live in {self.address}.")

class Student(Person):

    def __init__(self, name, age, address,sid):
        super().__init__(name, age, address)
        self.sid = sid

    def showData(self):
        print(f"Hi, my name is {self.name} and I am a student with ID{self.sid}.")

p = Person("Jhon Doe",30,"123 Main Street")
p.showData()
s = Student("Jhon Doe",30,"123 Main Street",12345)
s.showData()