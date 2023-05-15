vector_1 = [int(input(f"Ingrese el numero {i+1}: "))for i in range(3)] # Esta linea de codigo pide al usuario 3 numeros y los guarda en una lista
vector_2 = [(i+20)/2 for i in vector_1] # Esta linea de codigo crea un vector con los elementos del vector 1
print(vector_2) # Esta linea de codigo imprime el vector