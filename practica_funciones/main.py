import csv
from tabulate import tabulate

def read_csv(name_file):
    answer = [] # Lista de diccionarios
    with open(name_file, 'r', newline='') as csvfile: # newline='' para que no agregue una linea vacia
        spamreader = csv.reader(csvfile) # spamreader es un objeto iterable
        header = next(spamreader) # Obtiene la primera fila
        for row in spamreader: # Recorre el objeto iterable
            converted_row = [] # Lista de valores convertidos
            for value in row: # Recorre cada valor de la fila
                try: # Intenta convertir el valor a int
                    converted_value = int(value) # Si no se puede convertir, se asigna el valor original
                except ValueError: # Si no se puede convertir a int, se asigna el valor original
                    converted_value = value # Si no se puede convertir a int, se asigna el valor original
                converted_row.append(converted_value) # Se agrega el valor convertido a la lista de valores convertidos
            answer.append(dict(zip(header, converted_row))) # Se agrega el diccionario a la lista de diccionarios
    return answer # Retorna la lista de diccionarios
            
def tablas(lista_dict):
    encabezados = lista_dict[0].keys() # Obtiene los encabezados
    filas = [[fila[encabezado] for encabezado in encabezados] for fila in lista_dict] # Obtiene los valores de cada fila
    tabla = tabulate(filas, headers=encabezados, tablefmt='fancy_grid') # Crea la tabla
    return tabla # Retorna la tabla

def porcentaje(value, total):
    return round((value*100)/total,5) # Retorna el porcentaje

def ordenador(lista):
    return sorted(lista, key = lambda x: list(x.values())[0], reverse=True) # Retorna la lista ordenada

def obtener_nombre(id_pais, name_file): 
    for object in read_csv(name_file): # Recorre el archivo
        if object['Id'] == id_pais: # Si el id del pais es igual al id del pais del archivo
            return object['Nombre'] # Retorna el nombre del pais
    return 'ID de país no válido' # Si no se encuentra el pais, retorna un mensaje de error

def opcion_1(): 
    while True: # Ciclo infinito
        mes = int(input("Ingrese el mes en valor numerico: ")) # El usuario ingresa el mes en valor numerico
        if mes not in range(1,6): # Si el mes no esta en el rango
            print("El mes no se encuentra registrado") # Se imprime un mensaje de error
            continue # Se continua con el ciclo
        else: break # Si el mes esta en el rango, se rompe el ciclo
    
    print(tablas(read_csv("paises.csv"))) # Se imprime la tabla de paises
    while True: # Ciclo infinito
        pais = int(input("Ingrese el Id del pais: ")) # El usuario ingresa el id del pais
        if pais not in range(1,8): # Si el id del pais no esta en el rango
            print("El pais ingresado no se encuentra registrado") # Se imprime un mensaje de error
            continue # Se continua con el ciclo
        else: # Si el id del pais esta en el rango
            break

    registro = read_csv("registro_mensual.csv") # Se lee el archivo registro_mensual.csv
    answer = None # Se inicializa la variable answer
    for i in registro: # Se recorre el archivo
        if i['mes'] == mes and i['pais'] == pais: # Si el mes y el pais son iguales a los ingresados por el usuario
            answer = i # Se asigna el diccionario a la variable answer
    
    if answer == None: # Si la variable answer no se modifico
        return "No hay registro" # Se retorna un mensaje de error
    else: # Si la variable answer se modifico
        return answer # Se retorna la variable answer

def opcion_2():
    registro = read_csv("registro_mensual.csv") # Se lee el archivo registro_mensual.csv
    while True: # Ciclo infinito
        opcion = input("Elige una opcion para visulizar el total de muertes acumuladas o casos nuevos acumulados según el continente o país (C/P): ").lower() # El usuario ingresa la opcion
        if opcion == "c": # Si la opcion es c
            print(tablas(read_csv("continentes.csv"))) # Se imprime la tabla de continentes
            continentes = read_csv("continentes.csv") # Se lee el archivo continentes.csv
            while True: # Ciclo infinito
                continente = int(input("Ingrese el continente en valor numerico: ")) # El usuario ingresa el continente en valor numerico
                if continente not in range(1,4): # Si el continente no esta en el rango
                    print("El continente no se encuentra registrado") # Se imprime un mensaje de error
                    continue # Se continua con el ciclo
                else: break # Si el continente esta en el rango, se rompe el ciclo

            casos_nuevos = sum([i["casos_nuevos"] for i in registro if i["continente"] == continente]) # Se suman los casos nuevos
            muertes_nuevas = sum([i["muertes_nuevas"] for i in registro if i["continente"] == continente]) # Se suman las muertes nuevas

            return obtener_nombre(continente, "continentes.csv"), casos_nuevos, muertes_nuevas  # Se retorna el nombre del continente y los casos y muertes nuevos
            

        elif opcion == "p":
            print(tablas(read_csv("continentes.csv")))
            while True:
                continente = int(input("Ingrese el continente en valor numerico: "))
                if continente not in range(1,4):
                    print("El continente no se encuentra registrado")
                    continue
                else: break

            paises = read_csv("paises.csv")
            pais_continente = [i["Id"] for i in paises if i["continente"] == continente]

            print(tablas([i for i in paises if i["continente"] == continente]))
            while True:
                pais = int(input("Ingrese el pais en valor numerico: "))
                if pais not in pais_continente:
                    print("El pais no se encuentra registrado")
                    continue
                else: break

            casos_nuevos = sum([i["casos_nuevos"] for i in registro if i["pais"] == pais])
            muertes_nuevas = sum([i["muertes_nuevas"] for i in registro if i["pais"] == pais])

            return obtener_nombre(pais, "paises.csv"), casos_nuevos, muertes_nuevas

        else:
            continue

def opcion_3():
    registro = read_csv("registro_mensual.csv") # Se lee el archivo registro_mensual.csv
    while True: # Ciclo infinito
        mes = int(input("Ingrese el mes en valor numerico: ")) # El usuario ingresa el mes en valor numerico
        if mes not in range(1,6): # Si el mes no esta en el rango
            print("El mes no se encuentra registrado") # Se imprime un mensaje de error
            continue # Se continua con el ciclo
        else: break # Si el mes esta en el rango, se rompe el ciclo
    
    casos_nuevos = sum([i["casos_nuevos"] for i in registro if i["mes"] == mes]) # Se suman los casos nuevos
    muertes_nuevas = sum([i["muertes_nuevas"] for i in registro if i["mes"] == mes]) # Se suman las muertes nuevas

    print(f"En el mes {mes} hubieron {casos_nuevos} casos y {muertes_nuevas} muertes nuevas en total") # Se imprime el total de casos y muertes nuevos

def opcion_4():
    registro = read_csv("registro_mensual.csv") # Se lee el archivo registro_mensual.csv
    paises = read_csv("paises.csv") # Se lee el archivo paises.csv
    casos_nuevos = sum([i["casos_nuevos"] for i in registro ]) # Se suman los casos nuevos
    muertes_nuevas = sum([i["muertes_nuevas"] for i in registro ]) # Se suman las muertes nuevas
    poblacion = sum([i["poblacion"] for i in paises]) # Se suman las poblaciones
    while True: # Ciclo infinito
        opcion = input("Elige una opcion para visulizar el porcentaje de muertes acumuladas o casos nuevos acumulados a nivel global M/C: ").lower() # El usuario ingresa la opcion
        if opcion == "m": # Si la opcion es m
            print(f"El porcentaje de muertes acumuladas a nivel global es de {porcentaje(muertes_nuevas, poblacion)}%") # Se imprime el porcentaje de muertes acumuladas
            break # Se rompe el ciclo
        elif opcion == "c": # Si la opcion es c
            print(f"El porcentaje de casos nuevos acumulados a nivel global es de {porcentaje(casos_nuevos, poblacion)}%") # Se imprime el porcentaje de casos nuevos acumulados
            break # Se rompe el ciclo
        else: continue # Si la opcion no es m o c, se continua con el ciclo

def opcion_5():
    paises_muertes_porcentaje = [] # Lista de diccionarios
    paises_casos_porcentaje = [] # Lista de diccionarios
    registro = read_csv("registro_mensual.csv") # Se lee el archivo registro_mensual.csv
    paises = read_csv("paises.csv") # Se lee el archivo paises.csv

    for j in paises: # Se recorre el archivo paises.csv
        casos_nuevos = sum([i["casos_nuevos"] for i in registro if i["pais"] == j["Id"]]) # Se suman los casos nuevos
        muertes_nuevas = sum([i["muertes_nuevas"] for i in registro if i["pais"] == j["Id"]]) # Se suman las muertes nuevas
        paises_muertes_porcentaje.append({j["Nombre"]: porcentaje(muertes_nuevas,j['poblacion'])}) # Se agrega el diccionario a la lista de diccionarios
        paises_casos_porcentaje.append({j["Nombre"]: porcentaje(casos_nuevos,j["poblacion"])}) # Se agrega el diccionario a la lista de diccionarios
    
    return paises_casos_porcentaje, paises_muertes_porcentaje # Se retorna las listas de diccionarios

def opcion_6():
    paises_casos_porcentaje, paises_muertes_porcentaje = opcion_5() # Se obtienen las listas de diccionarios
    return ordenador(paises_casos_porcentaje), ordenador(paises_muertes_porcentaje) # Se retorna las listas de diccionarios ordenadas

def main():
    while True: # Ciclo infinito
        print("""
1. Mostrar el total de muertes acumuladas y casos nuevos acumulados en un mes y país específico.
2. Mostrar el total de muertes acumuladas y casos nuevos acumulados según el continente o país.
3. Mostrar el total de muertes acumuladas y casos nuevos acumulados en un mes específico.
4. Mostrar el porcentaje de muertes acumuladas y casos nuevos acumulados a nivel global.
5. Mostrar el porcentaje de muertes acumuladas y casos nuevos acumulados a nivel global por país.
6. Mostrar el porcentaje de muertes acumuladas y casos nuevos acumulados a nivel global por país ordenado de mayor a menor.
7. Salir
        """) # Se imprime el menu
        option = int(input("Elige una opcion: ")) # El usuario ingresa la opcion
        if option == 1: # Si la opcion es 1
            answer = opcion_1() # Se llama a la funcion opcion_1
            if answer == "No hay registro": # Si la variable answer es igual a "No hay registro"
                print("No hay registro") # Se imprime un mensaje de error
            else:  
                print(f"En el mes {answer['mes']} en el pais {answer['pais']} hubieron {answer['casos_nuevos']} casos nuevos y {answer['muertes_nuevas']} muertes nuevas") # Se imprime el total de casos y muertes nuevos

        elif option == 2: # Si la opcion es 2
            answer = opcion_2() # Se llama a la funcion opcion_2
            print(f"En {answer[0]} hubieron {answer[1]} casos nuevos y {answer[2]} muertes nuevas") # Se imprime el total de casos y muertes nuevos

        elif option == 3: # Si la opcion es 3
            opcion_3() # Se llama a la funcion opcion_3
        elif option == 4: # Si la opcion es 4
            opcion_4() # Se llama a la funcion opcion_4
        elif option == 5: # Si la opcion es 5
            paises_casos_porcentaje, paises_muertes_porcentaje = opcion_5() # Se obtienen las listas de diccionarios
            while True: # Ciclo infinito
                opcion = input("Elige una opcion para visulizar el porcentaje de muertes acumuladas o casos nuevos acumulados a nivel global M/C: ").lower() # El usuario ingresa la opcion
                if opcion == "m": # Si la opcion es m
                    for i in paises_muertes_porcentaje: # Se recorre la lista de diccionarios
                        print(f"{tuple(i.keys())[0]} tiene un porcentaje de muertes acumuladas de {tuple(i.values())[0]}%") # Se imprime el nombre del pais y el porcentaje de muertes acumuladas
                    break # Se rompe el ciclo

                elif opcion == "c": # Si la opcion es c
                    for i in paises_casos_porcentaje: # Se recorre la lista de diccionarios
                        print(f"{tuple(i.keys())[0]} tiene un porcentaje de casos nuevos acumulados de {tuple(i.values())[0]}%") # Se imprime el nombre del pais y el porcentaje de casos nuevos acumulados
                    break # Se rompe el ciclo
                else: # Si la opcion no es m o c
                    print("Opcion no valida") # Se imprime un mensaje de error
                    continue # Se continua con el ciclo
        elif option == 6: # Si la opcion es 6
            paises_casos_porcentaje, paises_muertes_porcentaje = opcion_6() # Se obtienen las listas de diccionarios ordenadas
            paises = read_csv('paises.csv') # Se lee el archivo paises.csv
            while True: # Ciclo infinito
                opcion = input("Elige una opcion para visulizar el porcentaje de muertes acumuladas o casos nuevos acumulados a nivel global M/C: ").lower() # El usuario ingresa la opcion
                if opcion == "m": # Si la opcion es m
                    for i in paises_muertes_porcentaje: # Se recorre la lista de diccionarios
                        print(f"{tuple(i.keys())[0]} tiene un porcentaje de muertes acumuladas de {tuple(i.values())[0]}% con respecto a una poblacion de {[j['poblacion'] for j in paises if j['Nombre'] == tuple(i.keys())[0]][0]}") # Se imprime el nombre del pais y el porcentaje de muertes acumuladas
                    break # Se rompe el ciclo
 
                elif opcion == "c": # Si la opcion es c
                    for i in paises_casos_porcentaje: # Se recorre la lista de diccionarios
                        print(f"{tuple(i.keys())[0]} tiene un porcentaje de casos nuevos acumulados de {tuple(i.values())[0]}% con respecto a una poblacion de {[j['poblacion'] for j in paises if j['Nombre'] == tuple(i.keys())[0]][0]}") # Se imprime el nombre del pais y el porcentaje de casos nuevos acumulados
                    break # Se rompe el ciclo
                else: # Si la opcion no es m o c
                    print("Opcion no valida")  # Se imprime un mensaje de error
                    continue # Se continua con el ciclo
        elif option == 7: # Si la opcion es 7
            exit() # Se cierra el programa

        else: # Si la opcion no es 1, 2, 3, 4, 5, 6 o 7
            print("Opcion no valida") # Se imprime un mensaje de error
            continue # Se continua con el ciclo

if __name__ == "__main__": # Si el archivo es el principal
    main() # Se llama a la funcion main1|


"""
Entrada:
    opcion 1:
    el usuario ingresa el mes en valor numerico ademas del id del pais
    opcion 2:
    el usuario ingresa el continente en valor numerico y el id del pais
    opcion 3:
    el usuario ingresa el mes en valor numerico
    opcion 4:
    el usuario no ingresa nada
    opcion 5:
    el usuario no ingresa nada
    opcion 6:
    el usuario no ingresa nada
Proceso:
    opcion 1:
    se lee el archivo registro_mensual.csv y se filtra por mes y pais
    opcion 2:
    se lee el archivo registro_mensual.csv y se filtra por continente y pais
    opcion 3:
    se lee el archivo registro_mensual.csv y se filtra por mes
    opcion 4:
    se lee el archivo registro_mensual.csv y se suman los casos y muertes
    opcion 5:
    se lee el archivo registro_mensual.csv y se suman los casos y muertes por pais
    opcion 6:
    se lee el archivo registro_mensual.csv y se suman los casos y muertes por pais
Salida:
    opcion 1:
    se muestra el total de muertes acumuladas y casos nuevos acumulados en un mes y país específico.
    opcion 2:
    se muestra el total de muertes acumuladas y casos nuevos acumulados según el continente o país.
    opcion 3:
    se muestra el total de muertes acumuladas y casos nuevos acumulados en un mes específico.
    opcion 4:
    se muestra el porcentaje de muertes acumuladas y casos nuevos acumulados a nivel global.
    opcion 5:
    se muestra el porcentaje de muertes acumuladas y casos nuevos acumulados a nivel global por país.
    opcion 6:
    se muestra el porcentaje de muertes acumuladas y casos nuevos acumulados a nivel global por país ordenado de mayor a menor.
"""