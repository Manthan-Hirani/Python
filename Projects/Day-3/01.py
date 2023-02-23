target = 50

class MyClass:
    
    def match_target(numbers):
        for i in range(1,len(numbers)):
            if((numbers[i-1]+numbers[i]) == target):
                print (i, i+1)

numbers = [10, 20, 10, 40, 50, 60, 70]
a = MyClass.match_target(numbers)
