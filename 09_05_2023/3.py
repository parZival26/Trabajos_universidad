import random # Importamos la libreria random para generar numeros aleatorios


matrix = [] # Creamos una matriz vacia

filas = int(input("Ingrese la cantidad de filas de la matriz: ")) # Pedimos la cantidad de filas de la matriz
columnas = int(input("Ingrese la cantidad de columnas de la matriz: ")) # Pedimos la cantidad de columnas de la matriz

# Llenamos la matriz con numeros aleatorios
for i in range(filas):
    # Recorremos la matriz y le agregamos un numero aleatorio
    matrix.append([])
    # Agregamos un numero aleatorio
    for j in range(columnas):
        matrix[i].append(random.randint(50, 100))

# Le pedimos al usuario un numero para buscar en la matriz
numero = int(input("Ingrese un numero entero para saber si se encuentra en la matriz: "))
# Creamos una variable para saber si el numero se encuentra en la matriz
encontrado = False

# Mostramos la matriz
for i in matrix:
    print(i)

# Recorremos la matriz
for i in range(len(matrix)):
    # Recorremos la matriz
    for j in range(len(matrix[i])):
        # Si el numero se encuentra en la matriz
        if matrix[i][j] == numero:
            # Mostramos la posicion del numero en la matriz
            print(f"El numero {numero} se encuentra en la posicion [{i}, {j}]")
            encontrado = True
            break

# Si el numero no se encuentra en la matriz
if encontrado == False:
    print(f"El numero {numero} no se encuentra en la matriz")