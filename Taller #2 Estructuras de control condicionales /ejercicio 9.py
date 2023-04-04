bonificacion = int(input("Ingrese el valor de la bonificacion: "))
articulo = lambda articulo: print(f"puedes comprar {articulo}")

if bonificacion < 500000:
    articulo("el teclado gaming")
elif 1000000 > bonificacion >= 500000:
    articulo("la tableta digitalizadora")
elif 2000000 > bonificacion >= 1000000:
    articulo("el iPad")
else:
    articulo("el MacBook o un computador ASUS ROG.")
