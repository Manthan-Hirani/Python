# def cube(a):
#     return (a*a*a)

# l = [1,2,3,4,5]
# print(map(lambda cube:cube*cube*cube,l))

# a = 100
# a_bin = bin(a)
# a_oct = oct(a)
# a_hex = hex(a)

# print(bin(a))
# print(oct(a))
# print(hex(a))

# print(a(a_bin))
# print(a(a_oct))
# print(a(a_hex))

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# for i in range(len(mytuple)):
#     print(next(myit))
# print(type(myit))
# a = [next(myit), next(myit), next(myit)]
# b = ("\n".join(a))
# print(type(next(myit)))
# print(b)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# def fib(num):
#     if(num <= 1):
#         return num
#     else:
#         return(fib(num-1) + fib(num-2))


# for i in range(1,6):
#     print(fib(i))

# a = "Hello Please reversr the word 'Commander' and print it"
# print(a)
# name = "Commander"
# replace = (name[::-1])
# b = a.replace(name, replace)
# print(b)

# l1 = ["a", "b", "c", "d", "a", "b"]

# s1 = set(l1)

# l2  = list(s1)

# print(l2)

# def myFunc(e):
#   return len(e)

# cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

# cars.sort(key=myFunc)

# print(cars)

# print(ord('['))
# print(ord(']'))

# num1 = 16

# print(f"{num1 :03d} ")
# print(f"{num1 :07d} ")

a = set((1, 5, 10111, 10, 3, 4))
b = {1, 5, 10111, 10, 3, 4}
print(a)
print(b)