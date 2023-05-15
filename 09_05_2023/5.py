import numpy as np # Importamos numpy

matriz = [[],[],[],[],[]] # Creamos una matriz vacia

for i in matriz: # Recorremos la matriz
    if matriz.index(i) == 4 or matriz.index(i) == 0: # Si estamos en la primera o ultima fila
        for j in range(5): # Recorremos la matriz
            i.append(1) # Agregamos un 1
    else:
        for j in range(5): # Recorremos la matriz
            if j == 0 or j == 4: # Si estamos en la primera o ultima columna
                i.append(1) # Agregamos un 1
            else:
                i.append(0) # Agregamos un 0

print(np.array(matriz))# Mostramos la matriz