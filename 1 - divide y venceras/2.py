'''
Dados dos números: a y b. Calcule ab, usando sólo multiplicaciones sucesivas.
'''


def pot(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * pot(a, b - 1)


a = int(input('Ingresar base: '))
b = int(input('Ingresar potencia: '))

print(pot(a, b))
