import unittest

def numeros_recursividad(numero): # Se crea la funcion
    if numero < 0: # Caso base
        return numero # Se retorna el numero
    else: # Caso recursivo
        print(numero) # Se imprime el numero
        return numeros_recursividad(numero-1) # Se llama a la funcion con el numero menos 1
    

class Test(unittest.TestCase):
    def test_numeros_recursividad(self):
        self.assertEqual(numeros_recursividad(5), 0)


if __name__ == "__main__":
    numeros_recursividad(int(input("Ingrese un numero para imprimir con una funcion recursiva: ")))
    unittest.main()