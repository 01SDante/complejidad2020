'''
Haz un programa que almacene 5 elementos en una variable del tipo lista, la modifique para que
cada componente sea igual al cuadrado del componente original. El programa mostrara la lista
resultante por pantalla.
'''
n = 0
lista1 = []
lista2 = []

while (n < 5):
    try:
        e = int(input('Ingresar un número entero: '))
        lista1.append(e)
        n = n + 1
    except ValueError:
        print('El valor ingresado no es válido, por favor intente de nuevo.')

for i in lista1:
    lista2.append(pow(i, 2))

print(lista2)
