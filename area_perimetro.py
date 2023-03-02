print(f"""{"*"*86}
Este es un algoritmo que calcula el area y el perimetro de un rectangulo
{"*"*86}""")  # Esta linea se encarga de crear los * para separa el texto
base = int(input("Ingresa la base: "))
altura = int(input("Ingresa la altura: ")) 

print(f"""El area del rectangulo es {base*altura} m² y su perimetro es {(base*2)+(altura*2)}""")
