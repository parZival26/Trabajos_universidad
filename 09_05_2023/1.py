import numpy as np # Importamos numpy


matriz1 = [[],[],[]] # Creamos una matriz vacia
matriz2 = [[],[],[]] # Creamos una matriz vacia

# Llenamos las matrices con numeros ingresados por el usuario
for i in matriz1:
    # Recorremos la matriz y le agregamos un numero entero ingresado por el usuario
    for j in range(0, 3):
        # Agregamos un numero entero ingresado por el usuario
        i.append(int(input(f"Ingrese un numero entero para la primer matriz: ")))

# Llenamos las matrices con numeros ingresados por el usuario
for i in matriz2:
    # Recorremos la matriz y le agregamos un numero entero ingresado por el usuario
    for j in range(0, 3):
        # Agregamos un numero entero ingresado por el usuario
        i.append(int(input(f"Ingrese un numero entero para la segunda matriz: ")))

# Sumamos las matrices
matriz3 = np.array(matriz1) + np.array(matriz2)

# Mostramos las matrices
print("La primer matriz es:")
for i in matriz1:
    print(i)

print("\nLa segunda matriz es:")
for i in matriz2:
    print(i)

print("\nLa suma de las matrices es:")
for i in matriz3:
    print(i)