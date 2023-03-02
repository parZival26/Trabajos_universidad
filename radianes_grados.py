import math



def radianes_grados():
  print(f"""{"*"*86}
Este es un algoritmo que convierte los radianes a grados
{"*"*86}""")
  radianes = float(
    input("Cual es el angulo en radianes: "))  #Pregunta los radianes
  print(
    f"Tu angulo de {radianes} en radianes a grados seria {round((radianes * 180/math.pi), 2)}°"
  )  #Ejecuta el calculo y tambien trae una libreria para añadir el valor de Pi