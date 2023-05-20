import unittest

def normalize(text): # Se crea la funcion normalize que recibe un texto y retorna el mismo texto pero en minusculas y sin tildes
    text= text.lower()
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        text = text.replace(a, b)
    return text

def vocal_counter(frase): # Se crea la funcion vocal_counter que recibe una frase y retorna la cantidad de vocales que tiene
    frase = normalize(frase)
    counter = 0
    vocales = ('a', 'e', 'i','o','u')
    for i in frase:
        if i in vocales:
            counter +=1

    return counter


class Test(unittest.TestCase): # Se crean las pruebas unitarias
    def test_normalize(self):
        self.assertEqual(normalize("áéíóú"), "aeiou")
        self.assertEqual(normalize("ÁÉÍÓÚ"), "aeiou")

    def test_vocal_counter(self):
        self.assertEqual(vocal_counter("Hola, ¿cómo estás?"), 6)
        self.assertEqual(vocal_counter("Me encanta el chocolate"), 9)
        self.assertEqual(vocal_counter("El sol brilla en el cielo azul"), 11)


if __name__ == "__main__": # Se ejecuta el programa
    frase = input("Escribe una frase para saber cuantas vocales tiene o escribe 'test' para ejecutar las pruebas: ")
    if frase == 'test': unittest.main()
    else: print(f"La frase tiene {vocal_counter(frase)} vocales")