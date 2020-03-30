'''
Construya un algoritmo que sume todos los elementos en posición par de una lista.
'''
lista = []
c = 0
n = 0
sum = 0

while (c <= 0):
    try:
        c = int(input('Ingresar cantidad de elementos: '))
        if (c <= 0):
            print(
                'El valor ingresado no es válido, por favor ingrese un entero mayor a 0.')
    except ValueError:
        print('El valor ingresado no es válido, por favor ingrese un entero mayor a 0.')


print('\nCargar lista\n')
while (n < c):
    try:
        e = int(input('Ingresar un número: '))
        lista.append(e)
        n = n + 1
    except ValueError:
        print('El valor ingresado no es válido, por favor ingrese un entero.')

print('')

# range(i, f, p)    <-- i = inicio, f = fin, p = paso
# range(5)          <-- f = 5
# range(0, 5)       <-- i = 0, f = 5
# range(0, 5, 2)    <-- i = 0, f = 5, p = 2

for i in range(len(lista)):
    if(i % 2 == 0):
        sum += lista[i]

print(sum)
