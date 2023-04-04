orden  = []
valor_total = 0
menu = ('jugo', 'panserotti', 'pizza')

print("Ingresa tu orden y cuando acabes escribe exit para finalizar tu pedido")
while True:
    alimento = input("Ingresa el alimento que deseas: ").lower()
    if alimento == "exit":
        break
    elif alimento in menu:
        cantidad = int(input(f"Ingresa las unidades de {alimento} que deseas: "))
        orden.append({alimento: cantidad})
    else:
        print(f"{alimento} no esta en el menu")
    

for i in orden:
    if 'jugo' in i.keys():
        if i['jugo'] >= 2:
            i['valor'] = (2000*(i['jugo']))-(2000*(i['jugo']))*0.10
        else:
            i['valor'] = (2000*(i['jugo']))
        valor_total += i['valor']
    elif 'panserotti' in i.keys():
        if i['panserotti'] >= 2:
            i['valor'] = (3500*(i['panserotti']))-(3500*(i['panserotti']))*0.15
        else:
            i['valor'] = (3500*(i['panserotti']))
        valor_total += i['valor']
    elif 'pizza' in i.keys():
        if 5 > i['pizza'] >= 2:
            i['valor'] = (6000*(i['pizza']))-(6000*(i['pizza']))*0.10
        elif i['pizza'] >= 5:
            i['valor'] = (6000*(i['pizza']))-((6000*(i['pizza']))*0.3)
        else:
            i['valor'] = (6000*(i['pizza']))
        valor_total += i['valor']

    print(i)


print(f"Valor total: {valor_total}")