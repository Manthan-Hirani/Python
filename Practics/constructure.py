'''
Without using __init__ function
'''

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

'''
With Using __init__ function
# Constructor
'''

class MyCar:
    def __init__(self, name,model): # __init__ is a constructor
        self.name = name
        self.model = model

m1 = MyCar("Oodi","A") # Compalsuray give 3 aargument. one argument is self(m1) itself

m2 = MyCar("Tesla","A") # Compalsuray give 3 aargument. one argument is self(m2) itself

print(f"{m1.name} model no. {m1.model}")
print(f"{m2.name} model no. {m2.model}")