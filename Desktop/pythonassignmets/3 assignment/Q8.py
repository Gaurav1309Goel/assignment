def log2(n):
    if n` == 1:
        return 0
    elif n%2 == 0:
        return 1 + log2(n/2)
    else:
        return  log2(n+1)

a = input("enter the value of n ")
print log2(a)

