# It is batter to use classname to PascalCase not camelCase or other.

class MyClass: #blueprint of an object
    x = 5 #Variable
    def __init__(self) -> None: # methods
        pass

a = MyClass()
print(a.x) #print the value of x which present in MyClass

class MyCar:
    def info(self, name,model):
        self.name = "ABC"
        self.model = "XYZ"

m1 = MyCar()
m1.name = "Oodi"
m1.model = "A"

m2 = MyCar()
m2.name = "Tesla"
m2.model = "A"

print(f"{m1.name} model no. {m1.model}")
print(f"{m2.name} model no. {m2.model}")
