
perdieron = {} # Diccionario de pacientes que perdieron peso entre la pesada inicial y la intermedia
objetivo_cumplido = {} # Diccionario de pacientes que cumplieron el objetivo

cantidad = int(input("Ingrese la cantidad de pacientes: ")) # Se pide la cantidad de pacientes
pesos = ['inicial', 'intermedio', 'final'] # Lista de pesos
pacientes = {input("Nombre del paciente: "):([float(input(f"Ingrese el peso {i}: ")) for i in pesos], input("Ingrese si su objetivo es ganar/perder peso: ").lower(), float(input("Ingrese el objetivo de su peso final: "))) for i in range(cantidad)} # Se crea un diccionario con el nombre del paciente, los pesos, el objetivo y el objetivo de su peso final

for paciente in pacientes:
    print(f'El paciente {paciente} ha perdido {(pacientes[paciente][0][2] - pacientes[paciente][0][0])*-1} kg' if pacientes[paciente][0][2] - pacientes[paciente][0][0] <= 0 else f'El paciente {paciente} ha ganado {pacientes[paciente][0][2] - pacientes[paciente][0][0]} kg' ) # Se imprime si el paciente perdio o gano peso

for paciente in pacientes:
    if (pacientes[paciente][0][1] - pacientes[paciente][0][0]) < 0: # Se pregunta si el paciente perdio peso entre la pesada inicial y la intermedia
        perdieron[paciente] = (pacientes[paciente][0][1] - pacientes[paciente][0][0])*-1 # Se agrega el paciente y el peso perdido al diccionario perdieron

print(f"""
{len(perdieron)} Perdieron peso entre la pesada inicial y la intermedia y son los siguientes: """ if len(perdieron) > 0 else "Ningun paciente perdio peso entre la pesada incial y la pesada intermedia")
for i in perdieron:
    print(f"Paciente: {i} Peso perdido: {perdieron[i]}") # Se imprime el paciente y el peso perdido


      
for paciente in pacientes:
    if pacientes[paciente][1] == 'ganar' and pacientes[paciente][2] <= pacientes[paciente][0][2]: # Se pregunta si el objetivo del paciente es ganar peso y si el objetivo de su peso final es menor o igual a su peso final
        objetivo_cumplido[paciente] = pacientes[paciente] # Se agrega el paciente y sus datos al diccionario objetivo_cumplido
    elif pacientes[paciente][1] == 'perder' and pacientes[paciente][2] >= pacientes[paciente][0][2]: # Se pregunta si el objetivo del paciente es perder peso y si el objetivo de su peso final es mayor o igual a su peso final
        objetivo_cumplido[paciente] = pacientes[paciente] # Se agrega el paciente y sus datos al diccionario objetivo_cumplido

print(f"""
{len(objetivo_cumplido)} Cumplieron el objetivo y son los siguientes:""" if len(objetivo_cumplido) > 0 else "Ningun paciente cumplio el objetivo")
for i in objetivo_cumplido:
    print(f"Paciente: {i} Objetivo: {objetivo_cumplido[i][1]} Objetivo peso final: {objetivo_cumplido[i][2]}") # Se imprime el paciente, su objetivo y el objetivo de su peso final