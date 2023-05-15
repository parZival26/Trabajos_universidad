numero = int(input("Ingrese un numero entero positivo: "))
# Se valida que el numero sea positivo
if numero < 0:
    raise ValueError("El numero debe ser positivo")
else:
    # Se hace un ciclo para sumar los numeros impares hasta el numero ingresado
    resultado = 0
    for i in range(1, numero):
        if i % 2 == 0:
            continue
        else:
            resultado += i

print(f"El resultado es: {resultado}")  