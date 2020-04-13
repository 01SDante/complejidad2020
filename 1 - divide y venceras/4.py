'''
Dos amigos matan el tiempo de espera en la cola del cine jugando a un juego muy sencillo:
uno de ellos piensa un número natural positivo y el otro debe adivinarlo preguntando
solamente si es menor o igual que otros números. Diseñar un algoritmo eficiente para adivinar
el número.
'''
n1 = int(input('Ingresar número 1: '))
n2 = int(input('Ingresar número 2: '))


def adivinar(n1, n2):
    if n1 == n2:
        return print('Ganaste.')
    elif n1 <= n2:
        print('El número es menor o igual.')
        n2 = int(input('Ingresar número 2: '))
        return adivinar(n1, n2)
    else:
        return print('Perdiste.')


adivinar(n1, n2)
