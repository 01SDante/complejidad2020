'''
Cargar dos listas con la misma cantidad de elementos. Luego mezclarlas, cargándolas
ordenadas en otra lista.
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

lista3 = lista1 + lista2
lista3.sort()
print(lista3)
