#Este es un script que busca la raiz cuadrada de un numero con un margen de error {paso} con el fin de entender el porque float no es del todo presciso 

objetivo = int(input("Escoge un numero: "))
epsilon = 0.01
paso = epsilon ** 2
respuesta = 0.0

while abs(respuesta **2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    print(respuesta)

if abs(respuesta **2 - objetivo) >= epsilon:
    print(f"No se encontro la raiz cuadrada de {objetivo}")

else:
    print(f"la raiz cuadrada de {objetivo} es {respuesta}")