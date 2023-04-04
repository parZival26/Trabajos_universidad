def precios(elemento):
    precio  = float(input(f"Ingresa el precio del {elemento}"))
    return precio

def cantidad(elemento):
    elementos_vendidos = int(input(f"Ingrese cuantos {elemento} se vendieron"))
    return elementos_vendidos

celular = (precios(elemento="celular"), cantidad(elemento="celular"))
talbet = 0
computador = 0