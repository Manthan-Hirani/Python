class A:
	def __init__(self, n='Rahul'):
		self.name = n


class B:
    def __init__(self, roll):
        A.__init__(self, n='Rahul')
        self.roll = roll


object = B(23)
print(object.name)
