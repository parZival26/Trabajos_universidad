from datetime import datetime, date

def encuentra_año_nacimiento():
  print(f"""{"*"*86}
Este es un algoritmo que calcula tu edad
{"*"*86}""")  # Esta linea se encarga de crear los * para separa el texto
  dt = datetime.now()  #Busca la fecha actual
  año_actual = dt.year  #Obtiene el año actual
  año_nacimiento = int(
    input("Cual es tu año de nacimiento: "))  # Pregunta tu año de nacimiento
  print(
    f"Si naciste antes de {date.today()} tienes {año_actual - año_nacimiento} años si no tienes {año_actual - año_nacimiento -1} años "
  )  # Hace el calculo y lo muestra