def ecuacion(a, b, c):
    if (a != 0) and (b and c) > a:
        resolver = round(((b*2/(4*a**2))-(c/a))**1/2, 2)
        return resolver
    else:
        return ValueError("a no puede ser 0 y b y c tienen que ser mayores que a")
    
if __name__ == "__main__":
    letras = ['a', 'b', 'c']
    numeros = [float(input(f"Ingrea un numero {x}: ")) for x in letras]
    print(ecuacion(numeros[0], numeros[1], numeros[2]))
