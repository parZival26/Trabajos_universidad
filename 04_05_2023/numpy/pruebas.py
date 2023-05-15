import numpy as np

sample_list = [1, 2, 3, 4, 5]
np_list = np.array(sample_list)# Convertir una lista a un arreglo
print(type(np_list))
print(type([1,2,3]))

range_list = np.arange(20, 5, -2)# Generar un arreglo con un rango
print(range_list)

zeros_list = np.zeros((3,2), float)# Generar un arreglo de ceros
print(zeros_list)

ones_list = np.ones(8000, float)# Generar un arreglo de unos
print(ones_list)

print(np_list.max())# Obtener el valor máximo de un arreglo
print(np_list.min())# Obtener el valor mínimo de un arreglo

print(np_list.armax())# Obtener el índice del valor máximo de un arreglo
print(np_list.amin())#  Obtener el índice del valor mínimo de un arreglo