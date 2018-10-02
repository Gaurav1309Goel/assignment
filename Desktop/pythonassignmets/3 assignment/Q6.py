def fibonacci(a):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)

b = input("enter any number")
print fibonacci(b)

