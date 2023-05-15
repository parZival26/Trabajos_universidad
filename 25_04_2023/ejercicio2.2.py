import csv

grades = []


# Leer el archivo y almacenar los datos en una lista
with open('titiribi.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        grades.append(row)

# Eliminar la primera fila que contiene los nombres de las columnas


# Crear un diccionario con las notas de cada estudiante
notas = {
    "A": {
        "Matematicas": list(i[1] for i in grades if i[0] == "A" ),
        "Español": list(i[2] for i in grades if i[0] == "A" ),
        "Ingles": list(i[2] for i in grades if i[0] == "A" )
    },
    "B": {
        "Matematicas": list(i[1] for i in grades if i[0] == "B" ),
        "Español": list(i[2] for i in grades if i[0] == "B" ),
        "Ingles": list(i[2] for i in grades if i[0] == "B" )
    },
    "C": {
        "Matematicas": list(i[1] for i in grades if i[0] == "C" ),
        "Español": list(i[2] for i in grades if i[0] == "C" ),
        "Ingles": list(i[2] for i in grades if i[0] == "C" )
    }
}

# Convertir las notas de cada estudiante en números flotantes
for i in notas:
    for j in notas[i]:
        notas[i][j] = list(map(float, notas[i][j]))

# Calcular los promedios de cada estudiante
promedios = {
    "A": {
        "Matematicas": round(sum(notas["A"]["Matematicas"]) / len(notas["A"]["Matematicas"]), 2),
        "Español": round(sum(notas["A"]["Español"]) / len(notas["A"]["Español"]), 2),
        "Ingles": round(sum(notas["A"]["Ingles"]) / len(notas["A"]["Ingles"]), 2),
    },
    "B": {
        "Matematicas": round(sum(notas["B"]["Matematicas"]) / len(notas["B"]["Matematicas"]), 2),
        "Español": round(sum(notas["B"]["Español"]) / len(notas["B"]["Español"]), 2),
        "Ingles": round(sum(notas["B"]["Ingles"]) / len(notas["B"]["Ingles"]), 2)
    },
    "C": {
        "Matematicas": round(sum(notas["C"]["Matematicas"]) / len(notas["C"]["Matematicas"]), 2),
        "Español": round(sum(notas["C"]["Español"]) / len(notas["C"]["Español"]), 2),
        "Ingles": round(sum(notas["C"]["Ingles"]) / len(notas["C"]["Ingles"]), 2)
    }
}


# Calcular los promedios generales de cada colegio
promedio_general = {
    "A" : round(sum(promedios["A"].values()) / len(promedios["A"].values()), 2),
    "B" : round(sum(promedios["B"].values()) / len(promedios["B"].values()), 2),
    "C" : round(sum(promedios["C"].values()) / len(promedios["C"].values()), 2)
}

# Inicializar las variables que almacenarán los mejores promedios y los mejores diccionarios
mejor_promedio_matematicas = 0
mejor_promedio_ingles = 0
mejor_promedio_espanol = 0
mejor_diccionario_matematicas = ""
mejor_diccionario_ingles = ""
mejor_diccionario_espanol = ""

# Iterar sobre las áreas y las materias
for area in promedios.keys():
    for materia, promedio in promedios[area].items():
        # Actualizar el mejor promedio y el mejor diccionario si es necesario
        if materia == "Matematicas" and promedio > mejor_promedio_matematicas:
            mejor_promedio_matematicas = promedio
            mejor_diccionario_matematicas = area
        elif materia == "Ingles" and promedio > mejor_promedio_ingles:
            mejor_promedio_ingles = promedio
            mejor_diccionario_ingles = area
        elif materia == "Español" and promedio > mejor_promedio_espanol:
            mejor_promedio_espanol = promedio
            mejor_diccionario_espanol = area

# Imprimir los resultados
print(f"""Los Mejores Promedios son los siguientes:
Matematicas: {mejor_promedio_matematicas} del colegio {mejor_diccionario_matematicas}
Ingles: {mejor_promedio_ingles} del colegio {mejor_diccionario_ingles}
Español: {mejor_promedio_espanol} del colegio {mejor_diccionario_espanol}
General: {max(promedio_general, key=promedio_general.get)} con un promedio de {max(promedio_general.values())}""")


"""
Este algoritmo calcula el promedio de cada materia por cada colegio, luego calcula el promedio general de cada colegio y finalmente imprime el mejor promedio de cada materia y el mejor promedio general.
para eso se utilizan 3 diccionarios, uno para las notas, otro para los promedios de cada materia por colegio y otro para los promedios generales por colegio.
con el diccionario de notas se calculan los promedios de cada materia por colegio y se almacenan en el diccionario de promedios, luego con el diccionario de promedios se calculan los promedios generales por colegio y se almacenan en el diccionario de promedios generales.
con el diccionario de promedios se calculan los mejores promedios de cada materia y con el diccionario de promedios generales se calcula el mejor promedio general.
con el diccionario de promedios se calculan los mejores promedios de cada materia y con el diccionario de promedios generales se calcula el mejor promedio general.

"""