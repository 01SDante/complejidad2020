'''
Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda y no en
la primera.
'''
lista1 = []
lista2 = []
c = 0

while (c <= 0):
    try:
        c = int(input('Ingresar cantidad de elementos: '))
        if (c <= 0):
            print(
                'El valor ingresado no es válido, por favor ingrese un entero mayor a 0.')
    except ValueError:
        print('El valor ingresado no es válido, por favor ingrese un entero mayor a 0.')

n = 0
print('\nCargar lista 1\n')
while (n < c):
    try:
        e = int(input('Ingresar un número: '))
        lista1.append(e)
        n = n + 1
    except ValueError:
        print('El valor ingresado no es válido, por favor ingrese un entero.')

n = 0
print('\nCargar lista 2\n')
while (n < c):
    try:
        e = int(input('Ingresar un número: '))
        lista2.append(e)
        n = n + 1
    except ValueError:
        print('El valor ingresado no es válido, por favor ingrese un entero.')

print('')

for i in lista2:
    if (lista1.count(i) == 0):
        lista1.append(i)

print(lista1)
