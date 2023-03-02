def resistencia():
  print(f"""{"*"*86}
Este es un algoritmo que se encarga de encontar la resistencia total de un circuito en paraleo que tiene dos resistencias R1 y R2
{"*"*86}""")  # Esta linea se encarga de crear los * para separa el texto
  r1 = float(input("Cual es la primer resistencia: "))
  r2 = float(input("Cual es la segunda resistencia: "))
  print(
    f"La resistencia totdal del circuito es: {1/((1/r1)+(1/r2))}"
  )  # Esta linea se encarga de imprimir el resultado y a la vez ejecutar la formula
