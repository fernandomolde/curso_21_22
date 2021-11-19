#Programa que pida al usuario los siguientes datos:
#- Nombre
#- Apellido
#- Fecha de nacimiento
#- Telefono


#Tiene que pedir datos hasta que el usuario diga que ya terminó.
#Los datos se guardan en un diccionario
#Al final se muestra el diccionario
#----------------------------------------------------------------------



import pprint
import os
import csv

def pedir_personas():
    seguir = True
    lista_personas = []

    while seguir:
        pprint.pprint('introduzca datos. (n para terminar)')
        nombre = input('Nombre:')
        apellido = input ('Apellido1:')
        fecha_nac = input('Fecha de nacimiento:')
        telefono = input('Teléfono:')
        mi_dic = {'nombre': nombre, 'apellido': apellido, 'fecha_nac': fecha_nac, 'telefono': telefono}
        
        lista_personas.append(mi_dic)
        
        respuesta = input('¿Desea Continuar s/n?')
        if respuesta.upper() == 'N':
            seguir = False
        os.system('clear')

    return lista_personas

def guardar_csv(contenido, destino):
    with open(destino, 'w',newline = '') as f:
        escritor = csv.DictWriter(f,fieldnames=list(contenido[0].keys()))
        escritor.writeheader()
        escritor.writerows(contenido)

cont = pedir_personas()
ruta = '/home/fer/codigo/curso_21_22/csv/personas.csv' 

guardar_csv(cont,ruta)
pprint.pprint(pedir_personas())





# dic = {}

# def datos_personales():
    
#     for i in range(3):
#         nombre = input('Introduce el nombre')
#         if nombre  == str('stop'):
#             break
#         else:
#             dic['nombre'] = nombre
#         apellidos = input('Introduce los apellidos')
#         if apellidos == str('stop'):
#             break
#         else:
#             dic['apellidos'] = apellidos                                          #Ejemplo 2
#         fecha = input('Introduce tu fecha de nacimiento: (xx/xxx/xx')
#         if fecha == str('stop'):
#             break
#         else: 
#             dic['fecha'] = fecha
#         telefono = input('Introduce tu numero de telefono: ')
#         if telefono == str('stop'):
#             break
#         else:
#             dic['telefono'] = telefono

# for i in range(3):
    
#     nombre = str(input('nombre'))
#     if nombre == 'stop':
#         break
#     else:
#         dic['nombre'] = nombre
#     apellido = str(input('apellido'))
#     if apellido == 'stop':
#         break
#     else:   
#         dic['apellido'] = apellido
#     fecha = str(input('Fecha de nacimiento : (xx/xx/xx)'))                     # Ejemplo 1  
#     if fecha == 'stop':
#         break
#     else:
#         dic['fecha'] = fecha
#     telefono = str(input('Telefono: '))
#     if telefono == 'stop':
#         break
#     else:
#         dic['telefono'] = telefono
# datos_personales()