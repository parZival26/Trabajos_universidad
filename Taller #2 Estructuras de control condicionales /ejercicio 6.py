def ecuacion(a, b, c):
    if (b and c != 0) and b > a:
        resolver = round((-b+a)/(2*b*c), 2)
        return resolver
    else:
        return ValueError("La ecuación solo puede resolverse si la variable b y c son diferentes de cero y si b es mayor que a.")
    
if __name__ == "__main__":
    letras = ['a', 'b', 'c']
    numeros = [float(input(f"Ingrea un numero {x}: ")) for x in letras]
    print(ecuacion(numeros[0], numeros[1], numeros[2]))
