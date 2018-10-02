lst=[]
w=input("enter the size of list")
for i in range(w):
    k=input("enter element")
    lst.append(k)
def next(lst,n):
    lst[n-1]+=1
    if(lst[n-1]>9 and n-2>=0):
      lst[n-1]%=10
      next(lst,n-1)
    elif(lst[n-1]>9):
      lst[n-1]%=10
      lst.insert(0,1)
    return lst
print next(lst,len(lst))
