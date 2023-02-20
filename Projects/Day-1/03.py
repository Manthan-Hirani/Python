p = "Adani Group is an Indian multinational conglomerate, headquartered in Ahmedabad. It was founded by Gautam Adani in 1988 as a commodity trading business, with the flagship company ADANI Enterprises.other subsidiaries are Adani Ports, adani power, ADAni Wilmar etc."

plower = p.lower()
pcount = plower.count("adani")

print(f"Result = Adani appeared {pcount} times.")

pInitialSplit = plower.split(" ")
pFinalSplit = p.split(" ")
for i in range(len(pInitialSplit)):
    if(pInitialSplit[i]=="adani"):
        # print(i)
        print(pFinalSplit[i])