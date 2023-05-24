import unittest # se importa la libreria unittest

def promedio(lista): # se define la funcion promedio
    return sum(lista)/len(lista) # se retorna el promedio de la lista

class Test(unittest.TestCase): # se crean los test
    def test_promedio(self):
        self.assertEqual(promedio([1,2,3,4,5,6,7]), 4)
        self.assertEqual(promedio([1,2,3,4,5,6,7,8]), 4.5)
        self.assertEqual(promedio([-1,2,-3,4,-5,6,-7,8]), 0.5)

if __name__ == "__main__":
    lista = [] # se define la lista
    while True: # se ejecuta el codigo hasta que el usuario digite exit
        numero = input("Ingrese una cantidad de numeros para saber su promedio, escribe test para ejecutar los test o escriba exit para finalizar: ") 
        if numero == "exit": break
        elif numero == "test": unittest.main() # se ejecutan los test
        else: lista.append(int(numero)) # se agrega el numero a la lista

    print(f"El promedio es {promedio(lista)}")

    
        
