"""Trabajo sobre csv
Es importante transformar el csv en un diccionario ya qeu es mas facil de manipular"""
import csv

def read_csv(ruta):
    with open(ruta, 'r') as csvfile:
        #delimiter= es la forma en la que viene separado los datos
        #normalmente viene por , o ;
        reader = csv.reader(csvfile, delimiter=',')
        haeder = next(reader) #Obtenemos las llaves para el diccionario
        data = []
        for row in reader:
            iterable = zip(haeder, row) #Creamos los pares
            country_dic = {key: item for key, item in iterable} #Creamos el diccionario
            data.append(country_dic) #Añadimos el diccionario a la lista de dicts

        return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    #print(data)
    print(data[0])
