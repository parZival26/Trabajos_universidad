personas = int(input("Ingresa la cantidad de personas que van al evento: "))
bus_grande = 0
bus_mediano = 0
buseta = 0

print(f"Para llevar a {personas} personas necesita:")
while personas > 0:
    if  personas > 32:
        bus_grande +=1
        personas -= 40
    elif 32 >= personas > 24:
        bus_mediano +=1
        personas -= 32
    elif 24 >= personas >=1:
        buseta +=1
        personas -= 24

print(f"""Bus grande: {bus_grande}
Bus mediano: {bus_mediano}
Buseta: {buseta}""")