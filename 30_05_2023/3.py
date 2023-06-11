import unittest

def potencia_recursiva(numero, potencia): # Se crea la funcion
    if potencia == 1: # Caso base
        return numero
    else: # Caso recursivo
        return numero * potencia_recursiva(numero, potencia-1) # Se llama a la funcion con el numero y la potencia menos 1
    
class Test(unittest.TestCase): # Pruebas
    def test_potencia_recursiva(self):
        self.assertEqual(potencia_recursiva(3,4), 81)
        self.assertEqual(potencia_recursiva(5,3), 125)
        self.assertEqual(potencia_recursiva(-2,3), -8)
    
print(potencia_recursiva(3,4))
unittest.main()