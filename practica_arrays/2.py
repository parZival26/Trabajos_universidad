import numpy as np

notas_definitivas = [] # Lista de notas definitivas
perdio_materia = {} # Diccionario de estudiantes que perdieron la materia
habilito_materia = {} # Diccionario de estudiantes que habilitaron la materia
gano_materia = {} # Diccionario de estudiantes que ganaron la materia

cantidad = int(input("Ingrese la cantidad de estudiantes: ")) # Se pide la cantidad de estudiantes
estudiantes = {input("Ingrese el nombre del estudiante: "): round(np.mean([float(input(f"Ingrese la nota {i+1} del estudainte: ")) for i in range(5)]),1) for i in range(cantidad)} # Se crea un diccionario con el nombre del estudiante y la nota definitiva

for notas in estudiantes: # Se recorre el diccionario estudiantes
    notas_definitivas.append(estudiantes[notas]) # Se agrega la nota definitiva a la lista notas_definitivas

    if estudiantes[notas] < 3: # Se pregunta si la nota definitiva es menor a 3
        perdio_materia[notas] = estudiantes[notas] # Se agrega el estudiante y la nota definitiva al diccionario perdio_materia
        if 2 <= estudiantes[notas] < 3: # Se pregunta si la nota definitiva esta entre 2 y 3
            habilito_materia[notas] = estudiantes[notas] # Se agrega el estudiante y la nota definitiva al diccionario habilito_materia
    else: # Si la nota definitiva es mayor o igual a 3
        gano_materia[notas] = estudiantes[notas] # Se agrega el estudiante y la nota definitiva al diccionario gano_materia


mejor_promedio = max(gano_materia) # Se obtiene el estudiante con el mejor promedio

print(f""" 
Los Promedios fueron los siguientes:
{estudiantes}


""") # Se imprime el diccionario estudiantes

print(f"El mejor estudiante fue {mejor_promedio} con un promedio de {gano_materia[mejor_promedio]}") # Se imprime el estudiante con el mejor promedio


print(f"""
Los Estudiantes que perdieron la materia fueron los siguientes:
{perdio_materia}


""") # Se imprime el diccionario perdio_materia
      
print(f"""
Los Estudiantes que habilitaron la materia fueron los siguientes:
{habilito_materia}


""") # Se imprime el diccionario habilito_materia

print(f"""
Los Estudiantes que ganaron la materia fueron los siguientes:
{gano_materia}

{len(gano_materia)} Estudiantes ganaron la materia
""") # Se imprime el diccionario gano_materia y la cantidad de estudiantes que ganaron la materia



