import unittest

def calculadora(x, y, operador): # Se crea la funcion calculadora que recibe 3 parametros, 2 numeros y un operador
    if operador == '+' or operador == 'suma': # Se analiza el operador y se retorna el resultado de la operacion
        return x + y
    
    elif operador == '-' or operador == 'resta':
        return x-y
    
    elif operador == '*' or operador == 'multiplicacion' or operador == 'x':
        return x * y
    
    elif operador == '/' or operador == 'division':
        return x / y
    
    elif operador == '**' or operador == 'exponenciación':
        return x**y
    
    else: return 'El operador no es valido' # Si el operador no es valido se retorna un mensaje


class Test(unittest.TestCase): # Se crean las pruebas unitarias
    def test_calculator(self):
        self.assertEqual(calculadora(1, 2, '+'), 3)
        self.assertEqual(calculadora(1, 2, '-'), -1)
        self.assertEqual(calculadora(1, 2, '*'), 2)
        self.assertEqual(calculadora(1, 2, '/'), 0.5)
        self.assertEqual(calculadora(1, 2, '**'), 1)
        self.assertEqual(calculadora(1, 2, 'suma'), 3)
        self.assertEqual(calculadora(1, 2, 'resta'), -1)
        self.assertEqual(calculadora(1, 2, 'multiplicacion'), 2)
        self.assertEqual(calculadora(1, 2, 'division'), 0.5)
        self.assertEqual(calculadora(1, 2, 'exponenciación'), 1)
        self.assertEqual(calculadora(1, 2, 'x'), 2)
        self.assertEqual(calculadora(1, 2, 'y'), 'El operador no es valido')

if __name__ == "__main__":
    resultado = calculadora(float(input("Ingrese el primer numero: ")), float(input("Ingrese el segundo numero: ")), input("Ingrese la operacion (+  -  *  /  **): ")) # Se pide al usuario los numeros y el operador
    if resultado == 'El operador no es valido':
        print(resultado) # Si el operador no es valido se imprime el mensaje")
    else:
        print(f"El resultado de la operacion es {resultado}") # Se imprime el resultado en consola

    pruebas = input("Desea ejecutar las pruebas unitarias? (y/n): ") # Se pregunta al usuario si desea ejecutar las pruebas unitarias
    if pruebas == 'y':
        unittest.main()
    else: pass

    