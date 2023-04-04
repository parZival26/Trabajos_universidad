numero = int(input("Ingresa un numero para determinar si es primo: "))
es_primo = True

for i in range(2, int(numero/2)):
    if numero % i == 0 and numero < 0:
        es_primo =False
        break

print(es_primo)