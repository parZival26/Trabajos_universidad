def raiz(numero):
    try:
        if numero >= 0:
            numero = numero**1/2
            return round(numero, 2)
        else:
            return ValueError("El numero tiene que ser mayor o igual a 0")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print(raiz(float(input("Ingresa un numero para saber su raiz cuadrada: "))))