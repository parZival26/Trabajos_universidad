import math, unittest # se importa la libreria math y unittest

def conver_polar_carte(r,o): # se define la funcion conver_polar_carte
    return round(r * math.cos(o), 5), round(r*math.sin(o), 5) # se realizan los calculos y se retorna el resultado en cartesiano

class Test(unittest.TestCase): # se crean los test
    def test_conver_polar_carte(self): 
        self.assertEqual(conver_polar_carte(1,0), (1.0, 0.0))
        self.assertEqual(conver_polar_carte(1,(math.pi/2)), (0.0, 1.0))
        self.assertEqual(conver_polar_carte(1,(math.pi)), (-1.0, 0.0))

if __name__ == "__main__":
    print(conver_polar_carte(float(input("Ingrese el radio: ")), float(input("Ingrese el angulo: ")))) # se imprime el resultado de la funcion conver_polar_carte
    unittest.main() # se ejecutan los test
