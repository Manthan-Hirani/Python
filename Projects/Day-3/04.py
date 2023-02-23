class InsertionSort:

    def sorting(ls):
        for i in range(len(ls)):
            temp = ls[i]
            j = i-1
            while (ls[j] > temp and j >= 0):
                ls[j+1] = ls[j]
                j -= 1
            ls[j+1] = temp
        return ls

    def add(ls,a):
        ls.append(a)
        # ls.sort()
        InsertionSort.sorting(ls)

    def rem(ls,a):
        ls.remove(a)


lst = [5, 4, 10, 1, 6, 2]
print("Unsorted list: ",lst)
first = InsertionSort.sorting(lst)
print("Sorted list: ",first)
aor = input("Do you want to add or delete items from list [Y/N]: ")
if (aor == 'Y' or aor == 'y'):
    ad = input("Do you want to add or delete [A/D]: ")

    if (ad == 'A' or ad == 'a'):
        a = int(input("which number do you want to add?: "))
        InsertionSort.add(lst,a)
        print(first)
    elif (ad == 'D' or ad == 'd'):
        a = int(input("which element do you want to remove?: "))
        InsertionSort.rem(lst,a)
        print(first)
    else:
        print("Please Enter valid Input")

elif (aor == 'N' or aor == 'n'):
    print("No problem, The list remains same")
    print(first)

else :
    print("Please Enter valid Input")
