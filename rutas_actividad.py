import os
import settings


os.system('clear')

lista_archivo = []
archivo_salida = 'salida.txt'
ruta_salida = settings.RUTA_BASE + settings.CODIGO + settings.MI_CARPETA
miembros = 5
fila = ''
# Buscar los archivos
archivo = os.scandir(settings.RUTA_BASE + settings.CODIGO)
for a in archivo:
    if a.name.endswith('.py'):
        lista_archivo.append(a.name[:-3:])





# Agrupalos de 5 en 5 

for i in range(0,len(lista_archivo),miembros):
    temp = lista_archivo[i: i + miembros]
    fila += ','.join(temp) + '\n'

# Guardar archivos en el fichero 
nuevo = open(ruta_salida + '/lista_py.txt','w')    
nuevo.write(fila)
nuevo.close()


# 2º forma
nuevo = open(ruta_salida + '/lista_py.txt','w')  
for i in range(0,len(lista_archivo),miembros):
    temp = lista_archivo[i: i + miembros]
    nuevo.write(','.join(temp) + '\n')


nuevo.close()





