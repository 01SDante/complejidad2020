'''
Dados dos números enteros n y m, construir una función recursiva que calcule el mínimo
común múltiplo entre ambos.
'''


def mcd(n, m):
    if m != 0:
        return mcd(m, n % m)
    else:
        return n


def mcm(n, m):
    if n == 0 or m == 0:
        return 0
    else:
        return (n * m) / mcd(n, m)


n = int(input('Ingresar n: '))
m = int(input('Ingresar m: '))

print(mcm(n, m))
