año = int(input("Ingrese un año para saber si es bisiesto: "))
if (año % 4 == 0):
    if año % 100 == 0:
        if año % 400 ==0:
            print("El año es un año bisiesto (tiene 366 días).")
        else:
             print("El año no es un año bisiesto (tiene 365 días). ")
    else:
        print("El año es un año bisiesto (tiene 366 días).")    
else:
    print("El año no es un año bisiesto (tiene 365 días). ")