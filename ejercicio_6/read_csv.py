import csv

def read_csv(ruta):
    with open(ruta, 'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            data_dict = {key: value for key, value in iterable}
            data.append(data_dict)
        return data
    
data = read_csv('./Libro.csv')

if __name__ == '__main__':
    data = read_csv('./Libro.csv')
    print(data)