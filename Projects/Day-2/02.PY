num = int(input("How many number you want to add: "))
if (num > 11 or num < 1):
    print("Please enter number between 1 to 10")
else:
    ls = []
    new_ls = []
    # print(type(ls))
    for i in range(num):
        n = int(input(f"Enter number {i+1}: "))
        ls.append(n)
    print(ls)
    for i in range(len(ls)):
        if(ls[i]>500):
            break
        elif(ls[i]>150):
            continue
        elif(ls[i]%5==0):
            new_ls.append(ls[i])
    print(new_ls)
        