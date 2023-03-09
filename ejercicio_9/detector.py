import read_csv

data = read_csv.read_csv('./Libro.csv')


data = list(filter(lambda x: (int(x['salario'])+((int(x['horas_extra']))* (int(x['valor_hora_extra'])))) >= 2000000, data))
print(data)

