def fib(n):
    if n<2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Bitte Zahl eingeben: "))
print(fib(n))


