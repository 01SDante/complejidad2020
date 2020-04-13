'''
Construir una función recursiva que, dado un número entero, devuelva como resultado el
factorial del mismo.
'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


n = int(input('Ingresar un número entero: '))

print(factorial(n))
