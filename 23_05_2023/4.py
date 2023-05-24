import unittest # se importa la libreria unittest


def valor_abs(numero): # se define la funcion valor_abs
    try: # se utiliza un try para capturar los errores
        numero = float(numero) # se define la variable numero
        if numero > 0: # si numero es mayor a 0 se retorna el valor de numero
            return numero
        else: # si numero es menor a 0 se retorna el valor de numero multiplicado por -1
            return numero*-1
    except ValueError: # si se lanza un error se ejecuta el codigo
        print("El valor tiene que ser numerico")

class Test(unittest.TestCase): # Clase de los test
    def test_valor_abs(self):
        self.assertEqual(valor_abs(5), 5)
        self.assertEqual(valor_abs(-5), 5)
        self.assertEqual(valor_abs(-3.5), 3.5)
        self.assertEqual(valor_abs("hola"), None)


if __name__ == "__main__": 
    print(valor_abs(float(input("Ingrese un numero para saber su valor absoluto: ")))) # se imprime el resultado de la funcion valor_abs
    unittest.main() # se ejecutan los test