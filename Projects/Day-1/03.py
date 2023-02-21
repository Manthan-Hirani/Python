p = "Adani Group is an Indian multinational conglomerate, headquartered in Ahmedabad. It was founded by Gautam Adani in 1988 as a commodity trading business, with the flagship company ADANI Enterprises.other subsidiaries are Adani Ports, adani power, ADAni Wilmar etc."

plower = p.lower()
name = "adani"
pcount = plower.count(name)

print(f"Result = Adani appeared {pcount} times.")

# pInitialSplit = plower.split(" ")
# pFinalSplit = p.split(" ")
# for i in range(len(pInitialSplit)):
#     if(pInitialSplit[i]=="adani"):
#         # print(i)
#         print(pFinalSplit[i])

# for i in range(len(p)):
#     start = plower.find(name)
#     end = len(name)
#     start = end
#     print(p[start:end])

# i = 0
# test = 0
# while(i<pcount):
#     start = plower.find("adani")
#     # print(start)
#     end = start + len(name)
#     # print(end)
#     print(p[start+test:end+test])
#     i += 1
#     test += end
#     plower = plower[end:]
#     # print(plower)

for i in range(pcount):
    start = plower.find(name)
    end = start + len(name)
    print (p[start:end])
    plower = plower[end:]
    p = p[end:]