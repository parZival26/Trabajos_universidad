numero = int(input("Ingresa el numero NEGATIVO que quieres pasar a positivo: "))

if numero > 0:
    print("Ingresa un numero negativo")
else: 
    print(f"Tu numero en forma positiva es {(numero)*(-1)}")