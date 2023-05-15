matriz = [[],[],[],[]]   # Creamos una matriz vacia
matriz_trans = [] # Creamos una matriz vacia

for i in matriz:
    for j in range(5):
        i.append(input("Ingrese el carater deseado: "))

for i in range(len(matriz[0])): # Recorremos la matriz
    columna = [matriz[j][i] for j in range(len(matriz))] # Recorremos la matriz y le agregamos un numero entero ingresado por el usuario
    matriz_trans.append(columna) # Agregamos un numero entero ingresado por el usuario

# Mostramos la matriz
print("Matriz original: ")
for i in matriz:
    print(i)

# Mostramos la matriz transpuesta
print("Matriz Transpuesta: ")
for i in matriz_trans:
    print(i)