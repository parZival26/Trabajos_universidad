def calcular_promedio(lista):
    try:
        if sum(lista) > 10:
            promedio = round((sum(lista)/len(lista)))
            return f"El promedio fue de {promedio}"
        else:
            return ValueError("No se puede determinar el promedio de goles de este jugador")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    pregunta = lambda i : int(input(f"Ingresa la cantidad de goles en el {i} partido: "))
    goles = [ pregunta(i+1) for i in range(3) ]
    print(calcular_promedio(goles))