#for-loop
#very important
l1=[1,234,3465]
sum = 0
for i in range(0,len(l1)):
   sum+= l1[i]
print sum
#while-loop
l1=[1,234,3465]
sums = 0
i = 0
while(i<len(l1)):
    sums+=l1[i]
    i+=1
print sums
#recursive function
l1=[1,234,3465]

def sums(l1):
  if len(l1) == 1:
      return l1[0]
  else:
      return l1[0] + sums(l1[1:])
print sums(l1)
