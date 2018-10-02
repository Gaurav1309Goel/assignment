def deep_copy(l):
    l2=[]
    for i in l:
        if type(i)=='list':
            return deep_copy(i)
        else:
            l2.append(i)
    return l2

l=[1,2,3,4,5,[3,4,[5,66,7,8,8,[0,9,8,4,6]]]]
print deep_copy(l)
