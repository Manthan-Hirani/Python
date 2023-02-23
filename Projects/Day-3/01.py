# 1.Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
# Note: There will be one solution for each input and do not use the same element twice.
#     • Input: numbers= [10,20,10,40,50,60,70], 
#     • target=50
#     • Output: 3, 4
target = 50

class MyClass:
    
    def match_target(numbers):
        for i in range(len(numbers)):
            if((numbers[i]+numbers[i+1]) == target):
                print (i+1, i+2)
                break

numbers = [10, 20, 10, 40, 50, 60, 70]
a = MyClass.match_target(numbers)
