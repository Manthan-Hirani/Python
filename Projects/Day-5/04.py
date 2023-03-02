stack = [1, 2, 3, 4, 5, 6]
print(stack)

def push(stack,index,number):
    stack.insert(index, number)

def pop(stack,index):
    stack.pop(index)

push(stack,1,15)
print(stack)
pop(stack,1)
print(stack)