def agua_contaminada():
  print(f"""{"*"*86}
Este es un algoritmo que calcula cuanta agua en m^3 contamina una poblacion que usa 2 pilas por semestre, en un año
{"*"*86}""")  # Esta linea se encarga de crear los * para separa el texto
  pila = 175  #Cantidad de m^3 contaminados de agua
  n = float(input("Ingrese el numero de millon(es) habitantes: "))
  persona = pila * 4  #Cantidad de pilas que usa una persona en un año
  resultado = persona * n  #Cuanto contamina la poblacion en total
  print(
    f'En una ciudad con {n} millones de habitantes se contaminan {resultado} millones de metros cúbicos de agua'
  )
