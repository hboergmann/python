# Rekursion Fakultät
def factorial(n):
    if n == 1:
        return (1)
    else:
        return (n * factorial(n - 1))
            
n = int(input("Bitte Zahl eingeben: "))
print(factorial(n))
       

