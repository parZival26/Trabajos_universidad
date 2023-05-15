import numpy as np

array_par = np.array([int(input("Ingrese un numero Par: ")) for i in range(int(input("Ingrese la cantidad de numeros: "))*2 ) if (i % 2 )== 0]) # En esta linea de codigo se crea un array con los numeros ingresados por el usuario
array_impar = np.array([int(input("Ingrese un numero impar: ")) for i in range(int(input("Ingrese la cantidad de numeros: "))*2) if i % 2 != 0]) # En esta linea de codigo se crea un array con los numeros ingresados por el usuario

array = np.concatenate((array_par,array_impar)) # En esta linea de codigo se concatenan los arrays

print(f"Array par: {array_par}, Array impar: {array_impar}, Array concatenado: {array}")