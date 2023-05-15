base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Se hace un ciclo para multiplicar la base por si misma el numero de veces que indique el exponente
resultado = base
# El ciclo le resta 1 al exponente para que no se multiplique la base por si misma el numero de veces que indique el exponente
for i in range(exponente-1):
    resultado *= base

# Se imprime el resultado
print(resultado)