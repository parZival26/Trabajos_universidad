elementos = {'c':'Carbono', 'h':'Hidrogeno', 'o':'Oxigeno', 'n':'Nitrogeno', 'p':'Fosforo', 's':'Azufre'}

def elemento(element):
    if element in elementos.keys():
        return f"El elemento es {elementos[element]}"
    else:
        return "Elemento no contemplado"

if __name__ == '__main__':
    print(elemento(input("Ingresa el simbolo del elemento deseado: ").lower()))