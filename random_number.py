import random

lista = []

def random_number_range(a, b, x):
    for i in range(x):
        num = random.randint(a, b)
        lista.append(num)


if __name__ == '__main__':
    minimo = int(input('Minimo: '))
    maximo = int(input('Maximo: '))
    if minimo >= maximo:
        print('Minimo no puede ser mayor o igual a maximo')
    else:
        cantidad = int(input('Cantidad: '))
        random_number_range(minimo, maximo, cantidad)
        print(lista)
