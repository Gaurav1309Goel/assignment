def mymax(lst):
    if len(lst) == 1:
        return lst[0]
    elif  lst[0]>mymax(lst[1:]):
        return lst[0]
    else:
        return mymax(lst[1:])

lst = []
j = input("enter the lenght of list")
for i in range(0,j):
    a = input("enter the numbers")
    lst.append(a)

print mymax(lst)
