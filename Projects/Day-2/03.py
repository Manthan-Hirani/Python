LikeData = [50,40,'Clay','Jessica',89]
# Output = [98,'Acissej','Yalc',04,05]

LikeData.reverse()
print(LikeData)

ls = []
for i in LikeData:
    if (type(i) == str):
        i = i[::-1]
        i = i.title()
        ls.append(i)
    if(type(i)==int):
        i = str(i)
        i = i[::-1]
        i = int(i)
        # if(len(i)<2):
        #     i.rjust(2,'0')
        ls.append(i)

print(ls)