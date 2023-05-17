import random
import time


def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return (match)

def busqueda_binaria(lista, comienzo, final, objetivo):

    if comienzo > final:
        return False
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio-1, objetivo)

    

if __name__ == "__main__":
    tamaño_lista = int(input("Ingresa el tamaño de la lista: "))
    objetivo = int(input("Que numero deseas encontrar: "))


    lista = sorted([random.randint(0, 100) for i in range(tamaño_lista)])

    inicio = time.time()
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    final = time.time()
    tiempo_binario = final - inicio

    inicio = time.time()
    encontrado2 = busqueda_lineal(lista, objetivo)
    final = time.time()
    tiempo_lineal = final - inicio



    print(f'El objetivo {objetivo} fue encontrado' if encontrado else 'No se encontro el objetivo', f'Tiempo binario {tiempo_binario}')
    print(f'El objetivo {objetivo} fue encontrado' if encontrado2 else 'No se encontro el objetivo', f'Tiempo binario {tiempo_lineal}')