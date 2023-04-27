import os

def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

ahorro = []
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio","agosto","septiembre","octubre","noviembre","diciembre"]

print("Bienvenido al programa de ahorro")

for i in meses:
    ahorro_mes = int(input(f"Ingrese el ahorro del mes {i}: "))
    ahorro.append(ahorro_mes)

diccionario = dict(zip(meses, ahorro))

clean_terminal()
for i in diccionario:
    print(f"El ahorro del mes {i} fue de {diccionario[i]}")

print(f"El ahorro total fue de {sum(ahorro)}")

"""
El algoritmo calcula el ahorro total de un año, ingresando el ahorro de cada mes.
Para ello, se crea una lista vacía llamada ahorro, y una lista con los meses del año.
Luego, se crea un bucle for que recorre la lista meses, y en cada iteración, se le pide al usuario que ingrese el ahorro del mes correspondiente.
A continuación, se crea un diccionario llamado diccionario, que contiene los meses como claves y el ahorro de cada mes como valores.
Por último, se muestra el ahorro de cada mes y el ahorro total.
"""
