import os
import csv
import pprint
os.system('clear')

ruta = '/home/fer/codigo/curso_21_22/csv/'

def leer_csv_normal():
    with open(ruta + 'archivos.csv') as csv_in:         # leer archivo csv normal
        filas = csv_in.readlines()
        for f in filas:
            print(f[:-1:].split(','))

# leer_csv_normal()

def leer_con_csv():                                     # leer archivo con csv
    campos = []
    filas = []

    csv_in = open(ruta + 'archivos.csv') 
    lector = csv.reader(csv_in)
    campos = next(lector)

    for f in lector:
        filas.append(f)

    csv_in.close()
    return campos,filas

# c,f = (leer_con_csv())
# pprint.pprint(c)
# pprint.pprint(f)

def leer_with():
    filas = []
    campos = []
    
    with open(ruta + 'archivos.csv') as csv_in:     #leer con WITH 
        lector = csv.reader(csv_in)
        campos = next(lector)
        for f in lector:
            filas.append(f)

    return campos, filas

# c,f = leer_with()
# pprint.pprint(c)
# pprint.pprint(f)



def leer_dict():                                # csv con diccionario
    csv_in = open(ruta + 'archivos.csv') 
    lector_dic = csv.DictReader(csv_in)
    
    lista_dict = list(lector_dic)

    csv_in.close()
    return lista_dict

pprint.pprint(leer_dict())