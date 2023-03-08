#Este es un pequeño script con la intencion de medir el tiempo que tarda python en ejecutarlo
import time

objetivo  = int (input('Escoje un entero: '))
respuesta = 0
tiempo = time .time()

while respuesta**2 <objetivo:
    respuesta +=1

if respuesta**2 == objetivo:
    print(f"La raiz cuadrada de {objetivo} es {respuesta}")
    print(f"El tiempo de respuesta fue de {round(time.time() - tiempo, 4)}")
else:
    print(f"{objetivo} no tiene una raiz exacta")