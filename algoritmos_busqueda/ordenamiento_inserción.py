import random


def ordenamiento_por_insercion(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        poscicion_actual = i

        while lista[poscicion_actual-1] > valor_actual and poscicion_actual > 0:
            lista[poscicion_actual] = lista[poscicion_actual-1]
            poscicion_actual -= 1
            lista[poscicion_actual] = valor_actual



if __name__ == '__main__':
    tamaño_lista = int(input("Ingrese el tamaño de la lista: "))
    
    lista = [random.randint(0,100) for i in range(tamaño_lista)]
    print("lista: \n", lista)


    lista_ordenada = ordenamiento_por_insercion(lista)
    print("lista ordenada: \n", lista)
    
    
