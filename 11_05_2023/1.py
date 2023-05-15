tupla = tuple(input("Ingrese la palabra {}: ".format(i+1)) for i in range(5)) # El usuario ingresa 5 palabras y se guardan en una tupla
for i in tupla:
    print(f"Palbra {tupla.index(i)+1} {i}") # Se imprime la palabra y su indice en la tupla