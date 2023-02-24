class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
# print("Rodger is a {}".format(Rodger.__class__.attr1)) # or we can use "print(f"Rodger is a {Rodger.attr1}")"
# print("Tommy is also a {}".format(Tommy.__class__.attr1)) # or we can use "print(f"Tommy is also a {Tommy.attr1}")"

# print(f"I am {Rodger.attr1}")
# print(f"My name is {Rodger.name}")
# print(f"I am {Tommy.attr1}")
# print(f"My name is {Tommy.name}")

print("Rodger is a {}".format(Rodger.attr1))

# Accessing instance attributes
# print("My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))
