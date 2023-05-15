arreglo_1 = [int(input(f"Ingrese el numero para el vector 1{i+1}: ")) for i in range(5)] # Esta linea de codigo pide al usuario 5 numeros y los guarda en una lista
arreglo_2 = [int(input(f"Ingrese el numero para el vector 2{i+1}: ")) for i in range(5)] # Esta linea de codigo pide al usuario 5 numeros y los guarda en una lista
arreglo_3 = [(arreglo_1[i] * arreglo_2[i]) for i in range(len(arreglo_1))] # Esta linea de codigo multiplica los elementos de los vectores
arreglo_final = [arreglo_1, arreglo_2, arreglo_3] # Esta linea de codigo crea una lista con los vectores
print(arreglo_final) # Esta linea de codigo imprime la lista