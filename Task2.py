#Task 2:

#The libraries is using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:
codes = [14, 15, 16, 17, 18, 18, 19, 20]


# Create a normal and comprehensive list that will display the codes.
codesN = []
for i in codes:
    codesN.append(i)
print("normal list that display the codes:", sodesN)

 #comprehensive list
codesC =[c for c in codes]
print("\nA comprehensio list that will dispaly in codes:", codesC)

# Create a normal and comprehensive list that will add the codes together for auditing purpose.
addCodesN = []
sumN = 0
for cc in codes:
    sumN = sumN + cc
addcodesN.append(sumN)
print("norml list:",addcodesN )


sumC = 0
addcodesC = [sumC: =sumC +ccComp for ccComp in codes]
print("\n comperhension", addcodesC)

#Create a normal and comprehensive list that will display only codes that are tracked by odd 
#numbers.

oddCodeN = []
for oN in codes:
    if oN % 2 != 0:
        oddCodesN.append(oC)
        print(oddCodeN)

       # CophrehensionList
        oddCodeC = [oC for oC in coes if oC%2 !=0]
        print("\nA comphrehension list displaye id:", oddCodeC)

        # Create a set to display the list of codes.
        setList = set(codes)
        print("set list to display of codes is:", setList)


        