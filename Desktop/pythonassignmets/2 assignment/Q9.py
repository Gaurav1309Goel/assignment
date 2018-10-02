d1 = (15,08,2051)
d2 = (13,08,2053)
print "Date 1 = ",d1
print "Date 2 = ",d2
print "The greater date is :- "
if d1[2] > d2[2]:
    print d1
elif d1[2] == d2[2]:
    if d1[1] > d2[1]:
        print d1
    elif d1[1] == d2[1]:
         if d1[0] > d2[0]:
            print d1
         elif d1[0] == d2[0]:
             print "Same dates"
         else:
             print d2
    else:
        print d2
else:
    print d2

    


