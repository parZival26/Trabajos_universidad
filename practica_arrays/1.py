def ordenar_diccionarios(diccionario): # Se crea una funcion para ordenar los diccionarios
    diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda item:item[1])) # Se crea un diccionario ordenado con la funcion sorted y se le pasa como parametro el diccionario, la key y el lambda
    return diccionario_ordenado     # Se retorna el diccionario ordenado

def diccionario_invertido(diccionario): # Se crea una funcion para invertir los diccionarios
    diccionario_inver = dict(sorted(diccionario.items(), key=lambda item:item[1], reverse=True))  # Se crea un diccionario ordenado con la funcion sorted y se le pasa como parametro el diccionario, la key y el lambda para que lo ordene de mayor a menor  
    return diccionario_inver   # Se retorna el diccionario invertido


if __name__ == '__main__': # Se crea el bloque principal
    catidad = int(input("Ingrese la cantidad de personas: ")) # Se pide la cantidad de personas
    personas = {input("Ingrese el nombre de la persona: "): float(input("Ingrese la estatura de la persona: ")) for i in range(catidad)} # Se crea un diccionario con el nombre y la estatura de la persona

    ascendente = ordenar_diccionarios(personas) # Se llama a la funcion ordenar_diccionarios y se le pasa como parametro el diccionario personas
    print("La lista en forma ascendente es: ") # Se imprime la lista en forma ascendente
    for key in ascendente: # Se recorre el diccionario ascendente
        print(f"{key} mide: {ascendente[key]}") # Se imprime el nombre y la estatura de la persona

    descendente = diccionario_invertido(ascendente) # Se llama a la funcion diccionario_invertido y se le pasa como parametro el diccionario ascendente
    print("La lista en forma descendente es: ") # Se imprime la lista en forma descendente
    for key in descendente: # Se recorre el diccionario descendente
        print(f"{key} mide: {descendente[key]}") # Se imprime el nombre y la estatura de la persona