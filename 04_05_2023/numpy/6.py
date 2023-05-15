import numpy as np

array = np.array([int(input("Ingrese un numero: ")) for i in range(int(input("Ingrese la cantidad de numeros: ")))]) # En esta linea de codigo se crea un array con los numeros ingresados por el usuario
array_par = array[array % 2 == 0] # En esta linea de codigo se crea un array con los numeros pares
array_impar = array[array%2 != 0] # En esta linea de codigo se crea un array con los numeros impares


print(f"Array: {array}, Array par: {array_par}, Array impar: {array_impar}")
print(f"Hay {len(array_par)} numeros pares y su promedio es de {round(np.mean(array_par),2)}, {len(array_impar)} numeros impares y su promedio es de {round(np.mean(array_impar),2)}") # En esta linea de codigo se imprime la cantidad de numeros pares e impares y su promedio