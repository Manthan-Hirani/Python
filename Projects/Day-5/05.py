'''1. To Print the Next 5 Perfect Squares After the Number.
For Example : Enter the Number : 15
The Next 5 Perfect Squares are :
16 25 36 49 64'''

# import math

# def myfunc(num):
#     sqrt = int(math.sqrt(num))
#     for i in range(sqrt+1,sqrt+6):
#         if(i == sqrt+5):
#             print(int(math.pow(i,2)))
#         else:
#             print(int(math.pow(i,2)),end=" ")

# myfunc(15)

'''2. To Print Possible Series of Sum Of Consecutive Numbers.
The Consecutive Series Of Sum 15 :
1+2+3+4+5
4+5+6'''

# def myfunc(n):
#     for i in range(1,15):
#         for j in range(i,n):
#             ls = list(range(i, j+1))
#             if sum(ls) == n:
#                 # print(ls)
#                 for k in ls:
#                     print(k,"+",end=" ")
#                 print()

# n = 15
# myfunc(n)
