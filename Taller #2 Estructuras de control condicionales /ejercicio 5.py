lista = sorted([int(input("ingrese un numero: ")) for i in range(3)])
lista_inverted = lista[::-1]
print(f"""lista de menor a mayor: {lista}
lista de mayor a menor: {lista_inverted}""")
