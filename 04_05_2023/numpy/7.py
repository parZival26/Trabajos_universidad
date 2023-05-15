import numpy as np # Importamos numpy como np

# En esta linea de codigo se crea un array con los nombres ingresados por el usuario
nombres = np.array([])
generos = np.array([])
edades = np.array([])

for i in range(int(input("Ingrese la cantidad de personas: "))): # En esta linea de codigo se crea un ciclo para pedir los datos de las personas
    nombre = input("Ingrese el nombre de la persona: ") # En esta linea de codigo se pide el nombre de la persona
    # En esta linea de codigo se crea un ciclo para validar que el genero ingresado sea F o M
    while True:
        genero = input("Ingrese el genero de la persona F/M: ").upper()
        if genero == 'f' or 'm':
            break
        else:
            continue

    edad = int(input("Ingrese la edad de la persona: ")) # En esta linea de codigo se pide la edad de la persona

    # En esta linea de codigo se agregan los datos ingresados a los arrays
    nombres = np.append(nombres, nombre)
    generos = np.append(generos, genero)
    edades = np.append(edades, edad)


counter = 0 # En esta linea de codigo se crea un contador para contar la cantidad de hombres
for i in generos:
    if i == 'M':
        counter += 1

# En esta linea de codigo se valida si hay hombres o no
if counter == 0:
    print("No hay hombres")
else: # En esta linea de codigo se imprime la cantidad de hombres
    print("Hay {} Hombre/s".format(counter))

counter = 0 # En esta linea de codigo se crea un contador para contar la cantidad de mujeres mayores de edad
contador = 0 # En esta linea de codigo se crea un contador para recorrer el array de edades
for i in generos:
    if i == 'F' and edades[contador] >= 18: # En esta linea de codigo se valida si el genero es F y si la edad es mayor o igual a 18
        counter += 1
    contador += 1

if  counter == 0: # En esta linea de codigo se valida si hay mujeres mayores de edad
    print("No hay mujeres mayores de edad")
else: # En esta linea de codigo se imprime la cantidad de mujeres mayores de edad
    print(f"Hay {counter} mujer/es mayores de edad")

contador = 0 # En esta linea de codigo se crea un contador para recorrer el array de edades
promedio = np.array([]) # En esta linea de codigo se crea un array para guardar las edades de los hombres
for i in generos:
    if i == 'M':
        promedio= np.append(promedio, edades[contador]) # En esta linea de codigo se agregan las edades de los hombres al array
    contador += 1

if np.size(promedio) == 0: # En esta linea de codigo se valida si hay hombres o no
    print("No hay hombres para saber el promedio")
else: # En esta linea de codigo se imprime el promedio de las edades de los hombres
    print(f"El promedio de edades de los hombres {np.mean(promedio)}")

def mujer_menor_edad(nombres, generos, edades): # En esta linea de codigo se crea una funcion para saber la mujer de menor edad
    nombres_F = np.array([]) # En esta linea de codigo se crea un array para guardar los nombres de las mujeres
    edades_F = np.array([])

    contador = 0 # En esta linea de codigo se crea un contador para recorrer el array de edades
    for i in generos:
        if i == 'F':
            nombres_F = np.append(nombres_F, nombres[contador]) # En esta linea de codigo se agregan los nombres de las mujeres al array
            edades_F = np.append(edades_F, edades[contador]) # En esta linea de codigo se agregan las edades de las mujeres al array
        contador += 1

    if np.size(nombres_F) == 0 or np.size(edades_F) == 0: # En esta linea de codigo se valida si hay mujeres o no
        print("No hay mujeres en la lista o no se registraron edades para mujeres.")
    else: # En esta linea de codigo se imprime el nombre de la mujer de menor edad
        menor = np.argmin(edades_F) # En esta linea de codigo se busca la posicion de la edad menor
        print(f"La mujer de menor edad es {nombres_F[menor]}")

mujer_menor_edad(nombres, generos, edades) # En esta linea de codigo se llama a la funcion mujer_menor_edad

    