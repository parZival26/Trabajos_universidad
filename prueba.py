def suma_producto():
    a = float(input("Ingrese un numero a: "))
    b = float(input("Ingrese un numero b: "))
    suma = a + b
    producto = a * b
    print(f"""
La suma de los dos numero es: {suma}
EL producto de los dos numeros es: {producto}""")

def salario_neto():
    horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
    valor_hora = float(input("Ingrese el precio de la hora de trabajo: "))
    descuento_salud = (horas_trabajadas*valor_hora)*0.16
    valor_neto = (horas_trabajadas*valor_hora)-descuento_salud
    print(f"""
Su salario neto es de {valor_neto}
El descuento a la salud es de {descuento_salud}""")
          
def tour_valor():
    personas = int(input("Ingrese la cantidad de personas que van a asistir al tour: "))
    transporte = float(input("Ingrese el valor del transporte: "))
    hospedaje = float(input("Ingrese el valor del hospedaje: "))
    alimentacion = float(input("Ingrese el valor de la alimentacion: "))
    valor_total = (transporte+hospedaje+alimentacion)*personas
    print(f"El valor total del tour es de: {valor_total}")

def conversor_moneda():
    pesos = int(input("Ingrese la cantidad de COP: "))
    dolar = round(pesos/4810,2)
    euro = round(pesos/5200,2)
    peso_mexicano = round(pesos/259,2)
    peso_argentino = round(pesos/23,2)
    real_brazileño = round(pesos/918,2)
    print(f"""
Tienes {dolar} dolares
Tienes {euro} euros
Tienes {peso_mexicano} pesos Mexicanos
Tienes {peso_argentino} pesos Argentinos
Tienes {real_brazileño} reales brazileños
    """)

def suma_mayor():
    a = float(input("Ingrese un numero a: "))
    b = float(input("Ingrese un numero b: "))
    if a > b:
        suma = a + b
        print(f"El resultado es {suma}")
    else:
        print(f"{b} es mayor que {a} ")

def salario_mayor():
    horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
    valor_hora = float(input("Ingrese el precio de la hora de trabajo: "))
    if (valor_hora*horas_trabajadas) <= 2000000:
        descuento = (horas_trabajadas*valor_hora)*0.16
    else:
        descuento = (horas_trabajadas*valor_hora)*0.24
    valor_neto = (horas_trabajadas*valor_hora)-descuento
    print(f"""
Su salario neto es de {valor_neto}
El descuento es de {descuento}""")
          
def tour_avion():
    personas = int(input("Ingrese la cantidad de personas que van a asistir al tour: "))
    transporte = float(input("Ingrese el valor del transporte: "))
    avion = input("al viarjar en avion se le añade el costo de un seguro. Viaja en avion? si/no: ")
    seguro = 500000
    hospedaje = float(input("Ingrese el valor del hospedaje: "))
    alimentacion = float(input("Ingrese el valor de la alimentacion: "))
    if avion == "si":
        valor_total = (transporte+hospedaje+alimentacion+seguro)*personas
    elif avion == "no":
        valor_total = (transporte+hospedaje+alimentacion)*personas
    else:
        raise MiErrorPersonalizado("Solo se acepta si/no como respuesta")
    print(f"El valor total del tour es de: {valor_total}")

def calcular_imc():
    peso = float(input("Ingresa tu peso en Kg: ")) 
    estatura = float(input("Ingresa tu estatura en m: "))
    imc = round(peso/(estatura**2, 1))
    if imc < 18.5:
        print("Tienes un peso bajo")
    elif 18.6 < imc < 24.9:
        print("Felicidades tienes un IMC ideal")
    elif 25 < imc < 29.9:
        print("Tienes sobrepeso")
    elif 30 < imc <34.9:
        print("Tienes obecidad I")
    elif 35 < imc <39.9:
        print("Tienes obecidad II")
    elif 40 < imc < 49.9:
        print("Tienes obecidad III")
    elif imc > 50:
        print("Tienes obecidad IV")

def temperaturas():
    try:
        grados = float(input(f"Ingresa los grados en C°: "))
        opciones = input("Elige a que tipo de grados los quieres convertir F/K: ").capitalize()
        if opciones == "F":
            temperatura = round((grados*(9/5))+32, 2)
        elif opciones == "K":
            temperatura = round(grados+273.15,2)
        else:
            raise MiErrorPersonalizado("Elige una opcion valida F/K")
        print(f"La temperatura es de {temperatura} {opciones}°")
    except Exception as e:
        print(e)

def positivo_negativo():
    try:
        numero = int(input("Ingresa un numero para saber si es positivo o negativo: "))
        if numero > 0:
            print("El numero es positivo")
        elif numero < 0:
            print("El numero es negativo")
        else:
            print("El 0 es un numero neutro")       
    except Exception as e:
        print(e)

def notas():
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    if 0 <= nota1 <= 5 and 0 <= nota2 <= 5 and 0 <= nota3 <= 5:
        promedio = (nota1 + nota2 + nota3)/3
        if promedio >= 3:
            print(f"Felicidades pasaste con una nota de {promedio}")
        else:
            print(f"Reprobasete tu nota fue de {promedio} deberias estudiar mas")
    else:
        print("Solo se aceptan notas entre 0 y 5")

def salario():
    horas = int(input("Ingrese el numero de horas trabajadas en la semana: "))
    salario = float(input("Ingrese el valor de una hora de trabajo"))
    if horas > 40:
        horas_extra = horas -40
        salario_total = (salario * horas) + (horas_extra * salario)
    else:
        salario_total = (salario * horas)

    print(f"Tu salario total es de: {salario_total}$")

def par_impar():
    numero = int("Ingresa un numero para determinar si es par o no: ")
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

def mayor():
    num1= float("Ingresa un numero 1 para saber si es mayor: ")
    num2 = float("Ingresa un numero 2 para saber si es mayor: ")
    if num1 > num2:
        print(f"{num1} es mayor que {num2}")
    elif num1 == num2:
        print(f"{num1} es igual que {num2}")
    else:
        print(f"{num2} es mayor que {num1}")

def nombre():
    vocales = ['a','e','i','o','u']
    nombre = input("Ingresa tu nombre para saber si empieza por una vocal: ").lower()
    if nombre[0] in vocales:
        print("Tu nombre empieza por una vocal")
    else:
        print("Tu nombre empieza por una consonate")

def determinar_desempeño():
    try:
        nota = round(float(input("Ingresa La nota final de la materia: ")), 1)
        if 0 <= nota <=5:
            if 4.5 < nota <=5:
                print("Felicidades su desempeño fue excelente siga así")
            elif 4 <= nota <=4.5:
                print("Felicidades su desempeño fue Sobresaliente")
            elif 3 <= nota <=3.9:
                print("Su desempeño fue aceptable")
            else:
                print("Su desempeño es insuficiente podria mejorar")
        else:
            raise MiErrorPersonalizado("Solo se pueden ingresar notas entre 0 y 5")
    except Exception as e:
        print(e)

def menor_medio_mayor():
    try:
        numeros = sorted([ int(input(f"Ingresa el numero {i} para determinar su poscicion: ")) for i in range(1, 4)])
        print(f"el numero menor es {numeros[0]} el del medio es {numeros[1]} y el mayor es {numeros[2]}")
    except Exception as e:
        print(e)

def mes_por_numero():
    try:
        meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
        numero = int(input("Ingresa un numero para saber a que mes pertenece: "))
        if 1 <= numero <= 12 and type(numero) == int:
            print(f"El numero {numero} pertenece al mes de {meses[(numero-1)]}")
        else:
            raise MiErrorPersonalizado("Solo se aceptan numeros enteros entre 1 y 12")
    except Exception as e:
        print(e)

def ulc():
    try:
        horas_totales = int(input("Ingrese la cantidad de horas totales de la materia: "))
        horas_asistidas = int(input("Ingrese la cantidad de horas que asistio el estudiante: "))
        if (horas_asistidas/horas_totales) >= 0.7:
            print(f"El estudiante asistio al {(horas_asistidas/horas_totales)*100}% de las horas puede aprobar la materia")
        else:
            print(f"El estudiante asistio al {round((horas_asistidas/horas_totales)*100,1)}% de las horas NO puede aprobar la materia")
    except Exception as e:
        print(e)

def descuentos():
    valor_compra = int(input("Ingrese el valor de su compra: "))
    bono = 0
    valor_total = 0
    if valor_compra < 10000:
        valor_total = valor_compra
        print(f"El valor total es de {valor_total}")
        exit()
    elif 30000 > valor_compra >= 10000:
        valor_total = valor_compra - (valor_compra*0.05)
    elif 60000>valor_compra >= 30000:
        valor_total = valor_compra - (valor_compra*0.15)
    elif valor_compra >= 60000:
        valor_total = valor_compra - (valor_compra*0.5)
        bono = valor_compra*0.2
    if bono == 0:
        print(f"El total con el descuento es de {round(valor_total, 2)}")
    else:
        print(f"El total con el descuento es de {round(valor_total, 2)} y tiene un bono de {round(bono,2)}")

class MiErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

if __name__ == "__main__":
    descuentos()