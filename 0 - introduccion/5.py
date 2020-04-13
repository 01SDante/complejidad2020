'''
Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.
'''

lista1 = []
lista2 = []

c = input(
    'Ingrese una palabra carácter por carácter, para finalizar ingrese un carácter en blanco: ')

while (c != ''):
    if (len(c) == 1):
        lista1.append(c)
        lista2.append(c)
    else:
        print('El valor ingresado no es válido, por favor ingrese un carácter a la vez.')
    c = input('Ingrese el siguiente carácter: ')

lista2.reverse()

if (len(lista1) > 0 and lista1 == lista2):
    print('La palabra ingresada es palíndromo.')
else:
    print('La palabra ingresada no es palíndromo')
