def pattern(n):
    l = []
    for i in range(n):
        sl = []
        for j in range(i+1):
            if (j == 0 or j == i):
                sl.append(1)
            else:
                sl.append(l[i-1][j-1] + l[i-1][j])
        l.append(sl)
    # print(l)
    for i in range(n):
        print(' '*(n-i-1),end="")
        for j in range(i+1):
            print(l[i][j],end=" ")
        print()

n = int(input("How many lines do you want to print? "))
pattern(n)