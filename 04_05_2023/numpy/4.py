import numpy as np

array_1 = np.array([int(input("Ingrese un numero: ")) for i in range(int(input("Ingrese la cantidad de numeros: "))) if i >= 0])# En esta linea de codigo se crea un array con los numeros ingresados por el usuario
array_2 = np.flip(array_1) # En esta linea de codigo se invierte el array

print(f"Array 1: {array_1}, Array Invertido: {array_2}")