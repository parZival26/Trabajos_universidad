procesador_intel = {'core i3': 94.49, 'core i5': 273.38, 'core i7': 395.01, 'i3': 94.49,  'i5': 273.38, 'i7': 395.01}
procesador_ryzen = {'ryzen 3':66.11, 'ryzen 5': 80.98, 'ryzen 7': 360.36, 'ryzen 9': 490.90}

tipo_procesador =  input("Elige que tipo de procesador quieres intel o ryzen: ").lower()
if tipo_procesador == "intel":
    tipo_generacion = input("""Elige un tipo de procesador:
    (1) core i3
    (2) core i5
    (3) core i7
    """)
    if tipo_generacion in procesador_intel.keys():
        print(f"El equipo tiene un valor de {round((procesador_intel[tipo_generacion])*5060, 2)} COP")
    else:
        raise IndexError(f"El procesador {tipo_generacion} no se encuentra en el catalogo")
elif tipo_procesador == "ryzen":
    tipo_generacion = input("""Elige un tipo de procesador:
    (1) ryzen 3
    (2) ryzen 5
    (3) ryzen 7
    (4) ryzen 9
    """)
    if tipo_generacion in procesador_ryzen.keys():
        print(f"El equipo tiene un valor de {round((procesador_ryzen[tipo_generacion])*5060, 2)} COP")
    else:
        raise IndexError(f"El procesador {tipo_generacion} no se encuentra en el catalogo")
    
else:
    raise Exception("Elige solo marcas entre intel y ryzen")