l1 = [[11,12,13] , [15,16,17] , [19,20,21]]
l2 = [[23,24,25] , [27,28,29] , [31,32,33]]
l3 = []
c = 0
print l1
print l2
print
for i in range(len(l1)):
    l3.insert(i,[])
    for j in range(len(l1[i])):
        l3[i].insert(j,0)
for i in range(len(l1)):
    if len(l1[i]) == len(l2):
        for j in range(len(l2[0])):
            for k in range(len(l2)):
                l3[i][j] += l1[i][k] * l2[k][j]
    else:
        c = 1
        break
if c == 0:
    print "PRODUCT"
    print l3
  
else:
   print "Error"
    
    


