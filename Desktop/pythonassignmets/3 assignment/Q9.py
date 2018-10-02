def deep_copy(l):
    l1=[]
    for i in l:
        if type(i)=='list':
            return deep_copy(i)
        else:
            l1.append(i)
    return l1

l=[1,2,3,[3,4,[5,66,7,8,8,[0,9,8,4,6]]]]
print deep_copy(l)
def depth(l):
    if(not type(l) == list):
        return 0;
    else:
        d = []
        for e in range(len(l)):
            d.append(1 + depth(l[e]))
        return max(d)
print "This program will now give give the depth of the list that we have taken"
print depth(l)
