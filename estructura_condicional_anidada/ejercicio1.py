persona = input("Que eres estudiante/docente/administrativo si no cumples ninguna de las anteriores escribe 'visitante': ").lower()

if persona == 'estudiante':
    codigo_asignado = int(input("Ingresa tu codigo de estudiante: "))
    print(f"Bienvenido estudiante, codigo:{codigo_asignado}")
elif persona == 'docente' or persona == 'administrativo':
    documento = int(input("Ingresa tu numero de documento: "))
    print(f"Bienvenido {persona}, documento: {documento}")
elif persona == 'visitante':
    nombre = input("Escribe tu nombre: ")
    apellido = input("Escribe tu apellido:")
    tipo_documento = input("Escribe tu tipo de documento: ")
    documento = int(input("Escribe tu documento: "))
    print(f"Bienvenido {nombre} {apellido}, {tipo_documento}: {documento}")


