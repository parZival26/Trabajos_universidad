import os

libros = []



def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')

def salir():
    clear_terminal()
    for i in libros:
        print(i,"\n")
    continuer = input("Desea continuar? (S/N): ").lower()
    if continuer == "s":
        clear_terminal()
    elif continuer == "n":
        clear_terminal()
        print("Gracias por usar la libreria")
        exit()


def paginas():
    while True:
        try:
            paginas = int(input("Ingrese la cantidad de paginas del libro: "))
            if paginas > 0:
                return paginas/2
            else:
                print("Error: La cantidad de paginas debe ser mayor a 0")
        except Exception as e:
            print("Error: ", e)



class Libro:

    def __init__(self, nacionalidad, paginas, mes):
        self.mes = mes
        self.nacionalidad = nacionalidad
        self.paginas = paginas 
        self.valor = round(self.precio()["Valor_original"], 2)
        self.valor_cop = self.precio()["COP"]
        self.iva = self.precio()["IVA"]
        self.iva_cop = self.precio()["IVA COP"]
        self.descontar = round((self.descuento()["descuento"])*(self.valor), 2)
        self.descontar_cop = round((self.descuento()["descuento"])*(self.valor_cop))
        self.final = round((self.valor + self.iva)-(self.descontar), 2)
        self.final_cop = round((self.valor_cop + self.iva_cop)-(self.descontar_cop))

    def descuento(self):
        """
        Devuelve un diccionario que contiene el descuento correspondiente al mes actual y la estación del año.
        """
        if self.mes in [12, 1, 2]:
            return {"descuento": 0.1785, "estacion": "Invierno"}
        elif self.mes in [3, 4, 5]:
            return {"descuento": 0.1235, "estacion": "Primavera"}
        elif self.mes in [6, 7, 8]:
            return {"descuento": 0.1005, "estacion": "Verano"}
        elif self.mes in [9, 10, 11]:
            return {"descuento": 0.875, "estacion": "Otoño"}
        else:
            raise ValueError("El mes no es válido")



    def precio(self):
        nacionalidades = {
            "ar": {
                "hojas": lambda paginas: paginas,
                "iva": 0.21,
                "values": {
                    "low": {"price": 0.36, "cop": 20.76},
                    "medium": {"price": 0.54, "cop": 20.76},
                    "high": {"price": 0.98, "cop": 20.76},
                },
            },
            "am": {
                "hojas": lambda paginas: paginas,
                "iva": 0.09,
                "values": {
                    "low": {"price": 2, "cop": 4526},
                    "medium": {"price": 4, "cop": 4526},
                    "high": {"price": 6, "cop": 4526},
                },
            },
            "eu": {
                "hojas": lambda paginas: paginas,
                "iva": 0.25,
                "values": {
                    "low": {"price": 0.4, "cop": 4960},
                    "medium": {"price": 0.8, "cop": 4960},
                    "high": {"price": 0.1, "cop": 4960},
                },
            },
        }

        nacionalidad_data = nacionalidades.get(self.nacionalidad[:2])
        if not nacionalidad_data:
            raise ValueError("La nacionalidad no es válida")

        hojas = nacionalidad_data["hojas"](self.paginas)

        if hojas < 100:
            valor_type = "low"
        elif hojas <= 300:
            valor_type = "medium"
        else:
            valor_type = "high"

        valor = hojas * nacionalidad_data["values"][valor_type]["price"]
        iva = round(valor * nacionalidad_data["iva"], 2)
        cop_rate = nacionalidad_data["values"][valor_type]["cop"]
        return {
            "Valor_original": valor,
            "COP": round(valor * cop_rate),
            "IVA": iva,
            "IVA COP": round(iva * cop_rate),
        }


        
    def __str__(self):
        return f"El valor original es de {self.valor} y su valor final es de {self.final} \nEl valor original en COP es de {self.valor_cop} y su valor final en COP es de {self.final_cop} \nEl descuento es de {self.descontar} y el descuento en COP es de {self.descontar_cop} \nEl IVA es de {self.iva} y el IVA en COP es de {self.iva_cop} \nLa estacion del año es {self.descuento()['estacion']}"

if __name__ == "__main__":
    try:
        clear_terminal()
        print("Bienvenido a la libreria")
        while True:
            nacionalidad = input("Ingrese la nacionalidad del autor del libro Argentina(AR) / America(AM) / Europa(EU) \nO dijite 'salir': ").lower()
            if nacionalidad == "ar" or nacionalidad == "am" or nacionalidad == "eu":
                libro = Libro(nacionalidad, paginas(), mes=int(input("Ingrese el mes de compra: ")))
                print(libro, "\n")
                libros.append(libro)
            elif nacionalidad == "salir":
                salir()
            else:
                print("Error: La nacionalidad no es valida")
                continue


    except Exception as e:
        print("Error: ", e)



"""
El programa comienza importando los módulos necesarios, os y datetime. También define dos variables, libros y mes. La primera se utiliza para almacenar la información de los libros y la segunda para almacenar el mes actual.

A continuación, se definen tres funciones auxiliares:

clear_terminal(): esta función se utiliza para borrar la pantalla de la terminal, de modo que la salida de la consola sea más clara.
salir(): esta función se utiliza para mostrar la información de los libros y preguntar al usuario si desea continuar o salir del programa.
paginas(): esta función se utiliza para pedir al usuario la cantidad de páginas de un libro y luego devolver la mitad de este número.
A continuación, se define la clase Libro, que tiene los siguientes atributos:

nacionalidad: el país de origen del libro, en formato ISO 3166-1 alpha-2.
paginas: la cantidad de páginas del libro.
mes: el mes actual.
valor: el precio original del libro.
valor_cop: el precio original del libro en pesos colombianos.
iva: el impuesto al valor agregado (IVA) aplicado al precio original.
iva_cop: el IVA aplicado al precio original en pesos colombianos.
descontar: el descuento aplicado al precio original.
descontar_cop: el descuento aplicado al precio original en pesos colombianos.
final: el precio final del libro, después de aplicar los descuentos y el IVA.
final_cop: el precio final del libro en pesos colombianos, después de aplicar los descuentos y el IVA.
La clase Libro tiene los siguientes métodos:

descuento(): este método devuelve un diccionario que contiene el descuento correspondiente al mes actual y la estación del año.
precio(): este método calcula el precio del libro, según su nacionalidad y la cantidad de páginas. Devuelve un diccionario que contiene el precio original, el IVA, el precio original en pesos colombianos y el IVA en pesos colombianos.
__str__(): este método devuelve una cadena que representa el objeto Libro, mostrando su precio original, su precio final, los descuentos y el IVA.
Por último, en el bloque if __name__ == "__main__": se ejecuta el programa principal. El programa comienza limpiando la pantalla y luego muestra un mensaje de bienvenida. A continuación, entra en un bucle que le pide al usuario que ingrese información sobre un libro. Luego, se crea una instancia de la clase Libro con la información ingresada y se agrega a la lista libros. Si el usuario decide salir del programa, se llama a la función salir().
"""