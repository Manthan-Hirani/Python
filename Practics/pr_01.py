import math
num = int(input("Enter a number: "))
min = int(math.sqrt(num))
# print(f"{num},{min}")

# x = 0
# while(x<5):
#     min += 1
#     ans = int(math.pow(min,2))
#     print(f"{ans}",end=" ")
#     x += 1

for i in range(5):
    min += 1
    ans = int(math.pow(min,2))
    print(f"{ans}",end=" ")