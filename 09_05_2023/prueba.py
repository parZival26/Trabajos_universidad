matriz = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't']]
matriz_trans = [[],[],[],[],[]]
counter = 0
for i in matriz_trans:
    for j in range(4):
        i.append(matriz[j][counter])
    counter +=1
print(matriz_trans)