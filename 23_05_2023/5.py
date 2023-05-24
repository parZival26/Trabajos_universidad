import unittest # se importa la libreria unittest


def conversor_rom(numero): # se define la funcion conversor_rom
    try: # se utiliza un try para capturar los errores
        texto = "" # se define la variable texto
        if 0 > numero or numero > 2050: # se define el rango de numeros que se aceptan
            raise ValueError # se lanza un error si el numero no esta en el rango
        else: # si el numero esta en el rango se ejecuta el codigo
            value = numero # se define la variable value
            while value > 0 :  # se ejecuta el codigo mientras value sea mayor a 0
                if value < 5: # si value es menor a 5 se ejecuta el codigo
                    texto += "I"
                    value -= 1
                elif 5 <= value <10: # si value es mayor o igual a 5 y menor a 10 se ejecuta el codigo
                    texto += "V" 
                    value -= 5
                elif 10 <= value < 50: # si value es mayor o igual a 10 y menor a 50 se ejecuta el codigo
                    texto += "X"
                    value -= 10
                elif 50 <= value < 100: # si value es mayor o igual a 50 y menor a 100 se ejecuta el codigo
                    texto += "L"
                    value -= 50
                elif 100 <= value < 500: # si value es mayor o igual a 100 y menor a 500 se ejecuta el codigo
                    texto += "C"
                    value -= 100
                elif 500 <= value <1000: # si value es mayor o igual a 500 y menor a 1000 se ejecuta el codigo
                    texto += "D"
                    value -= 500
                elif 1000 <= value : # si value es mayor o igual a 1000 se ejecuta el codigo
                    texto += "M"
                    value -= 1000

        return texto # se retorna el valor de texto
    except ValueError: # si se lanza un error se ejecuta el codigo
        print("Solo se aceptan numeros enteros menores a 2050 y mayores que 0")

class Test(unittest.TestCase): # se define la clase Test
    def test_conversor_rom(self): # se define la funcion test_conversor_rom
        self.assertEqual(conversor_rom(1), "I")
        self.assertEqual(conversor_rom(5), "V")
        self.assertEqual(conversor_rom(10), "X")
        self.assertEqual(conversor_rom(50), "L")
        self.assertEqual(conversor_rom(100), "C")
        self.assertEqual(conversor_rom(500), "D")
        self.assertEqual(conversor_rom(1000), "M")
        self.assertEqual(conversor_rom(2050), "MML")


if __name__ == "__main__":
    print(conversor_rom(int(input("Ingrese un numero no mayor a 2050 para saber su notacion en romano: ")))) # se imprime el resultado de la funcion conversor_rom
    unittest.main() # se ejecutan los test