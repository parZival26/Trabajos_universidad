primarios = ['amarillo', 'azul', 'rojo']
secundarios = ['naranja', 'verde', 'violeta']
try:
    pregunta = input("Elige si quieres mezclar un color primario con un color primario /p o secundario /s: ")
    if pregunta == 'p':
        color1 = input("Elige un color amarillo, azul o rojo: ")
        color2 = input("Elige un color amarillo, azul o rojo: ")
        if color1 and color2 in primarios:
            if color1 == color2:
                print(f"el resultado de mezclar {color1} y {color2} es: {color1}")
            elif (color1 == "amarillo" and color2 == "azul") or (color1 == "azul" and color2 == "amarillo"):
                print(f"el resultado de mezclar {color1} y {color2} es: verde")
            elif (color1 == "amarillo" and color2 == "rojo") or (color1 == "rojo" and color2 =="amarillo"):
                print(f"el resultado de mezclar {color1} y {color2} es: naranja")
            elif (color1 == "azul" and color2 == "rojo") or (color1 == "rojo" and color2 == "azul"):
                print(f"el resultado de mezclar {color1} y {color2} es: violeta")
        else:
            raise IndexError(f"El color no se encuentra en la lista de colores primarios ")

    elif pregunta == 's':
        color1 = input("Elige un color amarillo, azul o rojo: ")
        color2 = input("Elige un color naranja, verde, violeta: ")
        if (color1 in primarios) or (color2 in secundarios):
            if (color1 == "amarillo"):
                if color2 =="naranja":
                    print(f"el resultado de mezclar {color1} y {color2} es: amarillo anaranjado")
                elif color2 == "verde":
                    print(f"el resultado de mezclar {color1} y {color2} es: amarillo verdoso")
                elif color2 == "violeta":
                    print(f"el resultado de mezclar {color1} y {color2} es: neutral")

            elif (color1 == "azul"):
                if color2 =="naranja":
                    print(f"el resultado de mezclar {color1} y {color2} es: neutral")
                elif color2 == "verde":
                    print(f"el resultado de mezclar {color1} y {color2} es: Azul verdoso")
                elif color2 == "violeta":
                    print(f"el resultado de mezclar {color1} y {color2} es: Azul violáceo")

            elif (color1 == "rojo"):
                if color2 =="naranja":
                    print(f"el resultado de mezclar {color1} y {color2} es: rojo anaranjado")
                elif color2 == "verde":
                    print(f"el resultado de mezclar {color1} y {color2} es: neutral")
                elif color2 == "violeta":
                    print(f"el resultado de mezclar {color1} y {color2} es: rojo violáceo")
        else:
            raise IndexError(f"El color no se encuentra en la lista de colores primarios ")

    else:
        raise Exception("Solo se aceptan opciones p o s")
except Exception as e:
    print(e)