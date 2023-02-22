p = "Adani Group is an Indian multinational conglomerate, headquartered in Ahmedabad. It was founded by Gautam Adani in 1988 as a commodity trading business, with the flagship company ADANI Enterprises.other subsidiaries are Adani Ports, adani power, ADAni Wilmar etc."

plower = p.lower()
name = "adani"
pcount = plower.count(name)

print(f"Result = Adani appeared {pcount} times.")

i = 0
test = 0
while(i<pcount):
    start = plower.find("adani")
    # print(start)
    end = start + len(name)
    # print(end)
    print(p[start+test:end+test])
    i += 1
    test += end
    plower = plower[end:]
    # print(plower)
