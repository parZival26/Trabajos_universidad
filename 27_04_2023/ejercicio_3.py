m = int(input("Ingrese un numero (m): "))
n = int(input("Ingrese un numero (n): "))

# Esta funcion calcula el factorial de un numero
def factorial(numero):
    contador = 1
    for i in range(numero):
        contador *= numero
        numero -= 1
    return contador

# Esta funcion calcula el coeficiente binomial
fx = m/((factorial(n))*(factorial(m-n)))
print(fx)