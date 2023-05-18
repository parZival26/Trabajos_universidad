import random



def ordenamiento_mezcla(lista):


    if len(lista) > 1:
        medio = len(lista)//2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        i = 0
        j = 0

        k=0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k +=1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j+=1
            k+=1

        return lista



if __name__ == '__main__':
    tamaño_lista = int(input("Ingrese el tamaño de la lista: "))
    
    lista = [random.randint(0,100) for i in range(tamaño_lista)]
    print("lista: \n", lista)


    lista_ordenada = ordenamiento_mezcla(lista)
    print("lista ordenada: \n", lista)
