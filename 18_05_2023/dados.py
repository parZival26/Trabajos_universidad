import random, os, unittest # Se importan las librerias

def continuar(): # Se crea una funcion por si el usuario desea continuar la cual se ejecuta de forma infinita hasta que el usuario elija una opcion valida
    while True:
        opcion = input("Desea continuar S/N: ").lower()
        if opcion == 's':
            return True
        elif opcion == 'n':
            return False
        else:
            continue


def clean(): # Funcion para limpiar la terminal tanto en widows como en linux usado la libreria OS
    os.system('cls')
    os.system('clear')

def dado(tiradas): # Funcion para crear un dado la cual se ejecuta segun el numero de tiradas pasadas por el argumento y retorna una lista
    resultados = []
    for i in range(tiradas):
        resultados.append(random.randint(1,6))
    return resultados

def opcion_1(dado1): # Validacion del dado
    numeros_pares = 0
    numeros_impares = 0
    for i in dado1: # Se recorre la lista del dado1 y se revisa si el indice es par o no y se suma segun cual sea
        if i % 2 == 0:
            numeros_pares +=1
        else:
            numeros_impares +=1
    return numeros_impares, numeros_pares

def opcion_2(dado1, dado2): # Validacion si los dados son pares
    par = 0
    for i in range(min(len(dado1), len(dado2))): # Se recorre ambos dados segun el dado con menos tiradas y se analiza primero si los dados segun el indice es par 
        if dado1[i] % 2 == 0 and dado2[i] % 2 ==0:
            par +=1
    return par

def opcion_3(dado1, dado2): # Validacion si la tirada es igual 
    iguales = 0
    for i in range(min(len(dado1), len(dado2))): # Se recore ambas listas segun la longitud de la mas pequeña 
        if dado1[i] == dado2[i]: # Si es igual le suma 1 al contador
            iguales +=1
    return iguales
    
def opcion_4(dado1, dado2): # Se analiza las veces en que el dado es par y el primer y segundo dado son iguales
    par_igual = 0
    for i in range(min(len(dado1), len(dado2))): # Se recore el dado de menor longitud
        if dado1[i] % 2 == 0 and dado2[i] == dado1[i]: # Solo se analiza el primer dado ya que siempre tiene que ser igual al segundo, si la condicion se cumple se le suma 1
            par_igual +=1
    return par_igual

class Test(unittest.TestCase): # Se crean las pruebas unitarias
    def test_dado(self):
        self.assertEqual(len(dado(10)), 10)
        self.assertEqual(len(dado(20)), 20)
        self.assertEqual(len(dado(30)), 30)
        self.assertEqual(len(dado(40)), 40)
        self.assertEqual(len(dado(50)), 50)
    
    def test_opcion_1(self):
        self.assertEqual(opcion_1([1,2,3,4,5,6,7,8,9,10]), (5,5))
        self.assertEqual(opcion_1([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]), (8,7))
        self.assertEqual(opcion_1([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]), (8,7))

    def test_opcion_2(self):
        self.assertEqual(opcion_2([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5]), 2)
        self.assertEqual(opcion_2([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10]), 5)
        self.assertEqual(opcion_2([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]), 5)
        self.assertEqual(opcion_2([2,5,5,4,6,6,3,4,1,3,3,3,3,4,2,2,3,5,2,4], [1,1,2,2,3,4,4,1,4,2,2,3,5,4,1,1,1,4,6,5]), 4)

    
    def test_opcion_3(self):
        self.assertEqual(opcion_3([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5]), 5)
        self.assertEqual(opcion_3([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10]), 10)
        self.assertEqual(opcion_3([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]), 10)
    
    def test_opcion_4(self):
        self.assertEqual(opcion_4([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5]), 2)
        self.assertEqual(opcion_4([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10]), 5)
        self.assertEqual(opcion_4([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]), 5)



if __name__ == '__main__':


    while True: # Se ejecuta de una forma infinita hasta que el usuario elija una opcion para terminar el programa
        clean()
        opcion = int(input("""
1. Lanzar un dado 10 veces y contar la frecuencia de las caras con números pares y la frecuencia de las caras con números impares.
2. Lanzar dos dados 10 veces y contar las veces que la cara de los dados fue un numero par.
3. Lanzar dos dados 20 veces y contar las veces en que la cara de los dos dados es el mismo numero.
4. Lanzar dos dados 20 veces y contar las veces en que la cara de los dos dados es par y es el mismo numero.
5. Ejecutar pruebas
6. Salir
        
Elige una opcion: """)) # Opciones del usuario
        
        if opcion == 1: # Opcion 1
            clean() # Se limpia la terminal
            impar, par = opcion_1(dado(10)) # se definen la variables
            print(f"La frecuencia de las tiradas pares fue {par} veces y la de las tiradas impares fue {impar} veces") # Imprime en cosola
            if continuar(): continue # si se desea continuar o terminar el programa
            else: break

        elif opcion ==2:
            clean() # Se limpia la terminal
            resultado = opcion_2(dado(10), dado(10)) # Se define la variable y se ejcuta la funcion
            print(f"Las veces en que la cara de los dos dados fue un numero par son {resultado}") # Se imprime en consola
            if continuar(): continue  # si se desea continuar o terminar el programa
            else: break


        elif opcion ==3:
            clean() # Se limpia la terminal
            resultado = opcion_3(dado(20), dado(20)) # Se define la variable y se ejcuta la funcion
            print(f"Las veces en que la cara de los dos dados fueron iguales son {resultado}") # Se imprime en consola
            if continuar(): continue # si se desea continuar o terminar el programa
            else: break


        elif opcion ==4:
            clean() # Se limpia la terminal
            resultado = opcion_4(dado(20), dado(20)) # Se define la variable y se ejcuta la funcion
            print(f"Las veces en que la cara de los dos dados fueron iguales y pares son {resultado}") # Se imprime en consola
            if continuar(): continue # si se desea continuar o terminar el programa
            else: break

        elif opcion == 5:
            unittest.main() # Se ejecutan las pruebas

        elif opcion == 6:
            break # Se termina el programa
        else: continue # Si el usuario elige una opcion invalida se le pide que elija una opcion valida
