import unittest # se importa la libreria unittest


meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio','agosto','septiembre','octubre','noviembre','diciembre'] # se define la lista meses

def fecha(dia, mes, año):# se define la funcion fecha
    try: # se utiliza un try para capturar los errores
    
        if mes > 12 or mes < 0:  # si mes es mayor a 12 o menor a 0 se lanza un error
            raise Exception ("El mes no es valido")
        
        elif año < 0: # si año es menor a 0 se lanza un error
            raise Exception ("El año no es valido")
        
        elif (dia > 31 and mes in [1,3,5,7,8,10,12]) or dia < 0: # si dia es mayor a 31 y mes esta en la lista o dia es menor a 0 se lanza un error
            raise Exception ("El dia no es valido")
        
        elif dia > 30 and mes in [2,4,6,9,11]: # si dia es mayor a 30 y mes esta en la lista se lanza un error
            raise Exception ("El dia no es valido")

        else:
            return (f"{dia}/{mes}/{año}"), (f"{dia}/{meses[mes-1]}/{año}") # se retorna el valor de la fecha en los dos formatos


    except ValueError: # si se lanza un error se ejecuta el codigo
        print("La cadea es invalida escribe un numero entero")
    except Exception as e: # si se lanza un error se ejecuta el codigo
        print(e)


class Test(unittest.TestCase): # Se crean los test
    def test_fecha(self):
        self.assertEqual(fecha(1,1,2020)[0], "1/1/2020")
        self.assertEqual(fecha(1,1,2020)[1], "1/enero/2020")

if __name__ == "__main__":
    fecha1, fecha2 = fecha(int(input("Ingrese el dia: ")), int(input("Ingrese el mes: ")), int(input("Ingrese el año: "))) # se imprime el resultado de la funcion fecha
    print(f"""
formato 1: 
{fecha1}

formato 2: 
{fecha2}""")
    unittest.main()
    