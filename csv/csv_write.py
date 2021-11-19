import csv


ruta = '/home/fer/codigo/curso_21_22/csv/'



def csv_write():
    matriz = [
        [1,2,3,4,5],
        [3,4,5,6,7]
    ]
    with open(ruta + 'nuevo_1.csv','w') as csv_writer:
        escritor = csv.writer(csv_writer)
        escritor.writerow(['jueves']*10 + ['viernes'])
        escritor.writerow(['nada']*10 + ['fin'])
        escritor.writerows(matriz)

csv_write()