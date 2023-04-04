mes = input("Ingrese un mes para saber su estacion: ").lower()
estacion  = lambda x: print(f"La estacion es {x}")

if mes in ("noviembre", "diciembre", "enero"):
    estacion("invierno")
elif mes in ("febrero", "marzo", "abril"):
    estacion("primavera")
elif mes in ("mayo", "junio", "julio"):
    estacion("verano")
elif mes in ("agosto", "septiembre", "octubre"):
    estacion("otoño")
else:
    raise ValueError("Elige un mes valido")