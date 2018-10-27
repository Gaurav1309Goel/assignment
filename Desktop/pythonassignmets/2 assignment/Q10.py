l1 = [6,'a',8,9,"Pankti",3,"Pankti",8,3,1]
l2 = []
print l1
for i in range(0,len(l1)):
    c = 0
    for j in range(0,len(l2)):
        if l1[i] == l2[j]:
            c+=1
    if c==0:
            l2.append(l1[i])
print            
print "The list after removing the repeated numbers is :- ",            
print l2            

