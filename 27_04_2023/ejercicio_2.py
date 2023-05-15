import random
import os

# Generar un numero aleatorio entre 0 y 50
numero = random.randint(0, 50)
# Limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')
# Se hace un ciclo infinito para que el usuario adivine el numero
while True:
    # Se pide al usuario que ingrese un numero
    intento = int(input("Adivina el numero: "))
    # Se valida que el numero ingresado sea igual al numero generado
    if intento == numero:
        print("Felicidades, adivinaste el numero")
        break
    # Se valida que el numero ingresado sea mayor o menor al numero generado
    elif numero > intento:
        print("El numero es mayor")
    # Se valida que el numero ingresado sea mayor o menor al numero generado
    elif numero < intento:
        print("El numero es menor")
    
