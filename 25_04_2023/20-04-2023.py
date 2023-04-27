import random
import math

#Esta funcion le pregunta al usuario si desea continuar con el programa
def continuar():
    while True:
        opcion = input("Desea continuar? (S/N): ")
        if opcion == "S" or opcion == "s":
            return True
        elif opcion == "N" or opcion == "n":
            return False
        else:
            print("Opcion no valida")
            continue

#Esta funcion calcula el factorial de un numero
def factorial(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero = numero - 1
    print(f"El factoriales {factorial}")

#Esta funcion genera 10 numeros aleatorios usando la libreria random
def num_aleatorio():
    print("Los 10 numeros aleatorios son los siguientes:")
    lista = [random.randint(1, 100) for i in range(10)]
    print(lista)

#Esta funcion calcula las tablas de un numero ingresado por el usuario atraves de un parametro
def tablas(numero):
    print(f"La tabla del {numero} es la siguiente:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


#Esta funcion calcula los primeros 20 numeros impares sumando en un ciclo for 2 a 2
def impar():
    print("Los 20 primeros numeros impares son los siguientes:")
    numero = 1
    for i in range(20):
        print(numero)
        numero += 2
        
                
#Esta funcion se encarga de guardar en una lista los numeros primos entre 1 y 100
def primos():
    print("Los numeros primos entre 1 y 100 son los siguientes:")
    lista = []
    for numero in range(2, 101):
        if detector(numero) == False:
            continue
        else:
            lista.append(numero)
    print(lista)
        
#Esta funcion detecta si un numero es primo o no usando un ciclo for para recorrer los numeros entre 2 y la mitad del numero ingresado
def detector(numero):
    for i in range(2, (math.ceil(numero/2))):
        if numero % i == 0:
           return False
    return True
    

        


if __name__ == "__main__":
    # Menu principal
    while True:
        opcion = input("""
Bienvenido/a

(1) Saber el factorial de un numero
(2) Generar 10 numeros aleatorios
(3) Saber las tablas de un numero
(4) Saber los primeros 20 numeros impares
(5) Los numeros primos entre 1 100

salir

Elige una opcion: """)

        # Opciones del menu
        # Si la opcion es 1, se ejecuta la funcion factorial
        if opcion == "1":
            numero = int(input("Ingrese un numero para saber su factorial: "))
            factorial(numero)
            if continuar() == False:
                break
            else:
                continue
        #Si la opcion es 2, se ejecuta la funcion num_aleatorio
        elif opcion == "2":
            num_aleatorio()
            if continuar() == False:
                break
            else:
                continue
        #Si la opcion es 3, se ejecuta la funcion tablas
        elif opcion == "3":
            numero = int(input("Ingrese un numero para saber su tabla: "))
            tablas(numero)
            if continuar() == False:
                break
            else:
                continue
        #Si la opcion es 4, se ejecuta la funcion impar
        elif opcion == "4":
            impar()
            if continuar() == False:
                break
            else:
                continue
        #Si la opcion es 5, se ejecuta la funcion primos
        elif opcion == "5":
            primos()
            if continuar() == False:
                break
            else:
                continue
        #Si la opcion es salir, se sale del programa
        elif opcion == "salir":
            break
        #Si la opcion no es ninguna de las anteriores, se imprime un mensaje de error
        else:
            print("Opcion no valida")
            continue