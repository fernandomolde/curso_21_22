import os
import settings




def buscar(ruta_de_busqueda,extension = '.py'):
    lista_archivo = []
    archivo = os.scandir(ruta_de_busqueda)
    for a in archivo:
            if a.name.endswith(extension):
                lista_archivo.append(a.name[:-3:])
    return lista_archivo     

def agrupar(lista_archivo, miembros):
    fila = ''
    for i in range(0,len(lista_archivo),miembros):
            temp = lista_archivo[i: i + miembros]
            fila += ','.join(temp)+ '\n'
    return fila
def escribir(cadena, archivo):
    nuevo = open(archivo,'w')    
    nuevo.write(cadena)
    nuevo.close()
    

ruta = settings.RUTA_BASE + settings.CODIGO + settings.MI_CARPETA
ruta_salida = settings.RUTA_BASE + settings.CODIGO + settings.MI_CARPETA

x = buscar(ruta)
f = agrupar(x,5)
escribir(f,ruta_salida + '/funciones_lista.txt')
print(f)