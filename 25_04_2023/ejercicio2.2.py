import csv

grades = []

with open('titiribi.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        grades.append(row)

grades.pop(0)

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

for i in notas:
    for j in notas[i]:
        notas[i][j] = list(map(float, notas[i][j]))

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

promedio_general = {
    "A" : round(sum(promedios["A"].values()) / len(promedios["A"].values()), 2),
    "B" : round(sum(promedios["B"].values()) / len(promedios["B"].values()), 2),
    "C" : round(sum(promedios["C"].values()) / len(promedios["C"].values()), 2)
}


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
Este algoritmo cal
"""