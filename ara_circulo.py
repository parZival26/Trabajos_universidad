import math

diametro = input("Ingresa el diametro de un circulo para calcular su area: ")
radio = diametro/2
area = math.pi * (radio**2)

print(f"El area es: {area}")