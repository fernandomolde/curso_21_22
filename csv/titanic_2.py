import os
import csv
import pprint

os.system('clear')

ruta = '/home/fer/codigo/curso_21_22/csv/'

# 1- leer el archivo (como diccionario)
def leer_archivo():
    csv_in = open(ruta + 'titanic.csv') 
    lector_dic = csv.DictReader(csv_in)
    lista_dict = list(lector_dic)
    csv_in.close()
    return lista_dict


# def procesar_csv():
#     pasajeros = leer_archivo()
#     mujeres = []
#     hombres = []
#     h_v = 0
#     h_m = 0
#     m_v = 0
#     m_m = 0
#     for p in pasajeros:
#          if p['Sex'] == 'female':
#             mujeres.append(p['Survived'])
#     else:                                                       #Paso 2 y 3 
#             hombres.append(p['Survived'])
#     h_v = hombres.count('1')
#     h_m = mujeres.count('0')
#     m_v = mujeres.count('1')
#     m_m = mujeres.count('0')
    
#     return (h_m, h_v, m_m, m_v)

# 4- Devuelve resultado

# resultado = procesar_csv()
# print(f'Hombre vivos : {resultado[1]} Hombres Muertos : {resultado[0]}' )
# print(f'Mujeres vivas : {resultado[3]} Mujeres Muertas : {resultado[2]}' )


lista_diccionario = leer_archivo()
def personas_20_30():
    hay_cabecera = False
    for i in lista_diccionario:
        if i['Age'] >= '20' and i ['Age'] <= '30' and i ['Survived'] == '1':
            with open (ruta + 'titanic_nombres.csv', 'a') as csv_writer:
                escribir = csv.writer(csv_writer)
                if not hay_cabecera:
                    escribir.writerow(["Nombre", "Clase", "Sexo"])
                    hay_cabecera = True
                else:
                    escribir.writerow([i["Name"],i["Pclass"],i["Sex"]])


personas_20_30()



    










