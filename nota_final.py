def nota_final():
  print(f"""{"*"*86}
Este es un algoritmo que se encarga de calcular tu nota final
{"*"*86}""")  # Esta linea se encarga de crear los * para separa el texto
  parcial = float(input(
    "Ingresa tu nota del Parcial: ")) * 0.2  #Se te pregunta tu nota parcial
  final = float(
    input("Ingresa tu nota del final: ")) * 0.3  #Se te pregunta tu nota final
  seguimiento = float(input("Ingrese su nota de seguimiento: ")
                      ) * 0.5  #Se te pregunta tu nota de seguimiento
  if 0 < parcial < 5 and 0 < seguimiento < 5 and 0 < final < 5:  #esta linea se encarga de que solo se puedan ingresar notas entre 0 y 5
    print(f"Su nota final es: {round((parcial+final+seguimiento), 1)} "
          )  #imprime la nota final y tambien se encarga de sumar las notas
  else:  #esta linea se encarga de que si no se cumple la condicion del if imprime el siguiente mensaje:
    print("solo se aceptan notas entre 0 y 5")
