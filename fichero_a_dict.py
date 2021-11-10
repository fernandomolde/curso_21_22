import os  
import pprint 

os.system('clear')

ruta = '/home/fer/codigo/curso_21_22/viernes/programacion/python/funciones_miercoles.txt'

dic_salida = {}

clave = 0

#Leer Archivo
with open(ruta) as archivo:
    for l in archivo:
        # Procesar fila a fila
        fila = l[:-1:].split(',')
        #Recorrer lista y llenar dict
        for nombre in fila:
            dic_salida[clave] = nombre
            clave +=1

pprint.pprint(dic_salida)