lista = [int(input(f"Ingrese el numero {i+1}: ")) for i in range(5)] # Esta linea de codigo pide al usuario 5 numeros y los guarda en una lista
print(lista) # Esta linea de codigo imprime la lista
print(f"La lista invertida es {list(reversed(lista))}") # Esta linea de codigo imprime la lista invertida