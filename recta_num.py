# Este algoritmo no usa los puntos dados ya que presenta la opcion de ingresar los valores que el usuario quiera
print("Este es un algoritmo que calcula la ecuación de la recta que pasa por los puntos (x1, y1) y (x2, y2)")

x1 = float(input("Ingresa el valor de x1")) 
y1 = float(input("Ingresa el valor de y1")) 
x2 = float(input("Ingresa el valor de x2"))
y2 = float(input("Ingresa el valor de y2")) 

m = (x2-x1)/(y2-y1)
b = y1-(m*x1)

print(f"""La ecuación es:
y = {m}x + {b}""")