temperatura = float(input("Ingresa la temperatura de hoy en °C: "))
if temperatura < 23:
    print("Hace Frio")
elif 30 > temperatura >= 23:
    print("Día normal")
else:
    print("Hace calor")