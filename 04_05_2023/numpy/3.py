import numpy as np

array_edades = np.array([int(input("Ingrese la edad de la persona {}: ".format(i+1))) for i in range(5)])# En esta linea de codigo se crea un array con las edades ingresadas por el usuario
promedio = round(np.mean(array_edades),2) # En esta linea de codigo se calcula el promedio de las edades
mediana = round(np.median(array_edades),2) # En esta linea de codigo se calcula la mediana de las edades
desviacion_estandar = round(np.std(array_edades),2) # En esta linea de codigo se calcula la desviacion estandar de las edades

print(f"El promedio de las edades es: {promedio}, la mediana es: {mediana}, y la desviacion estandar es: {desviacion_estandar} ")# En esta linea de codigo se imprime el promedio, la mediana y la desviacion estandar de las edades