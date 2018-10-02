#for loop
c = 1
a = 2
b = 5
for i in range(0,b):
  c=c*a
print c

#while 
j = 4
d = 2
c = 1
i = 0
while i < d:
    c = c*j
    i = i + 1
print c


#recursive function
e = 7
f = 7
c = 1
def power(f,e):
    if f == 1:
        return 1
    elif e == 1:
        return f
    else:
        return f*power(f,e-1)
print power(f,e)
