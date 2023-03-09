texto = input("Ingrese su texot aqui: ")
lista = [i for i in texto if i != " "]


separador = ''
nuevo_texto = separador.join(lista)

print(f"""Tu texto sin espacios es:
{nuevo_texto}""")