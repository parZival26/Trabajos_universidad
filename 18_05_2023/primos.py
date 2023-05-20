import math 

def primo_range(numero):
    primo = True

    for i in range(2, (numero)):
        if numero % i == 0:
            primo = False
            break

    return primo


if __name__ == "__main__":
    primos = []
    for i in range(2, 101):
        if primo_range(i): primos.append(i)

    print(primos)
