
# Esta es la solución por pywombat

def factorial(valor):
    if valor ==1:
        return valor
    else:
        return valor * factorial(valor-1)

print(factorial(3))
print(factorial(5))
print(factorial(15))