import numpy as np # Importamos numpy

# Creamos una matriz vacia
matriz = [[],[],[],[],[]]

# Llenamos la matriz con numeros ingresados por el usuario
for i in range(0, 5):
    # Recorremos la matriz y le agregamos un numero entero ingresado por el usuario
    for j in range(0, 5):
        # Agregamos un numero entero ingresado por el usuario
        matriz[i].append(int(input(f"Ingrese un numero entero para la matriz: ")))
    
# Invertimos la matriz
matriz = np.array(matriz)

# Mostramos la matriz
print("La matriz invertida es:")
# Recorremos la matriz
for i in range(4, -1, -1):
    # Recorremos la matriz de forma inversa
    for j in range(4, -1, -1):
        print(matriz[i][j], end=' ')
    print()

