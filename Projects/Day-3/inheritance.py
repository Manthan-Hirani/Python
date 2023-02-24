class Employee():

    leaves = 15

    def __init__(self, id, name, possition):
        self.id = id
        self.name = name
        self.possition = possition

    def employeeDetails(self):
        return f"Name is {self.name} and he is a {self.possition}"
    
    @staticmethod
    def sum(a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return (a+b+c)
        elif a!=None and b!=None:
            return (a+b)
        else:
            return (a)

    @classmethod
    def changeLeaves(self,newleaves):
        self.newleaves = newleaves


e1 = Employee(1, "Manthan", "Developer")
e2 = Employee(2, "Chirag", "Developer")
e3 = Employee(3, "Ved", "Developer")
e4 = Employee(4, "Amisha", "HR")
e5 = Employee(5, "Meera", "HR")

