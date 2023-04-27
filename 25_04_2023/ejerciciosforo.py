import random

def ejercicio_1():
    for i in range(10):
        print(i+1, end=" ")

def ejercicio_2():
    contador = 0
    while True:
        numero = int(input("Ingrese un numero para sumarlo o ingrese 0 para terminar: "))
        if numero < 0:
            print("Solo se aceptan numeros positivios")
            continue
        elif numero == 0:
            break
        else:
            contador += numero
    print(f"El resultado final es {contador}")

def ejercicio_3(numero):
    resultado = 1
    while numero > 0:
        resultado *= numero
        numero -= 1
    print(resultado)

def ejercicio_4():
    for i in range(10, 0, -1):
        print(i, end=" ")

def ejercicio_5():
    numero = 0
    while numero < 20:
        numero += 2
        print(numero, end=" ")

def ejercicio_6():
    contador = 0
    for i in range(101):
        contador += i
    print(f"El resultado de sumar los numeros del 1 al 100 es {contador}")

def ejercicio_7():
    numeros = [random.randint(1, 100) for i in range(10) ]
    print("Los 10 numeros aleatorios son los siguientes: ")
    for i in numeros:
        print(i, end=" ")

def ejercicio_8():
    for i in range(10):
        print(f" 9 X {i+1} = {9*(i+1)}")

def ejercicio_9():
    contador = 1
    for i in range(20):
        print(contador)
        contador += 2
        
def detector(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True


def ejercicio_10():
    primos = []
    for i in range(2, 101):
        numero = detector(i)
        if numero == True:
            primos.append(i)
    print(primos)
            

        

   
if __name__ == "__main__":
    pass


'''
En el primer ejercicio, se debe imprimir los numeros del 1 al 10, para ello se debe usar un for y la funcion print

En el segundo ejercicio, se debe pedir al usuario que ingrese numeros, y se deben ir sumando, hasta que el usuario ingrese 0, para ello se debe usar un while y la funcion input

En el tercer ejercicio, se debe pedir al usuario que ingrese un numero, y se debe imprimir el factorial de ese numero, para ello se debe usar un while y la funcion input

En el cuarto ejercicio, se debe imprimir los numeros del 10 al 1, para ello se debe usar un for y la funcion print

En el quinto ejercicio, se debe imprimir los numeros pares del 2 al 20, para ello se debe usar un while y la funcion print

En el sexto ejercicio, se debe imprimir la suma de los numeros del 1 al 100, para ello se debe usar un for y la funcion print

En el septimo ejercicio, se debe imprimir 10 numeros aleatorios, para ello se debe usar un for y la funcion print

En el octavo ejercicio, se debe imprimir la tabla del 9, para ello se debe usar un for y la funcion print

En el noveno ejercicio, se debe imprimir los numeros impares del 1 al 20, para ello se debe usar un for y la funcion print

En el decimo ejercicio, se debe imprimir los numeros primos del 1 al 100, para ello se debe usar un for y una funcion que detecte si un numero es primo o no
'''