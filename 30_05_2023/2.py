import unittest

def fibonacci(numero): # Se crea la funcion
    if numero < 2: # Caso base
        return numero
    else: 
        return fibonacci(numero-1) + fibonacci(numero-2) # Se llama a la funcion con el numero menos 1 y el numero menos 2
    
class Test(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(16), 987)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(0), 0)

contador = 0
while True: # Se imprime toda la serie hasta que el resultado del contador llegue a mil
    if fibonacci(contador) > 1000:
        break
    else:
        print(fibonacci(contador))
        contador +=1


unittest.main()