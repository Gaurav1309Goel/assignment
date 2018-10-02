#for-loop
l=[1,234,3465]
sum = 0
for i in range(0,len(l)):
   sum+= l[i]
print sum
#while-loop
l=[1,234,3465]
sums = 0
i = 0
while(i<len(l)):
    sums+=l[i]
    i+=1
print sums
#recursive function
l=[1,234,3465]

def sums(l):
  if len(l) == 1:
      return l[0]
  else:
      return l[0] + sums(l[1:])
print sums(l)
