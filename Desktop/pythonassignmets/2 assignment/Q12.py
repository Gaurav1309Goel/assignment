l1 = [[11,12,13,14] , [15,16,17,18] , [19,20,21,22]]
l2 = [[23,24,25,26] , [27,28,29,30], [31,32,33,34]]
l3 = []
c=0
print l1
print l2
print
for i in range(len(l1)):
    l3.insert(i,[])
if len(l1) == len(l2):
    for a in range(len(l1)):
        if len(l1[a]) == len(l2[a]):
            for y in range(len(l1[a])):
                l3[a].append(l1[a][y]+l2[a][y])
        else:
            c = 1
            break

    if c ==0:
        print "SUM"
        print l3
    else:
        print "Error"
else:
    print "Error"

