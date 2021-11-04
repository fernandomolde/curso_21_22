from pprint import pprint

archivo = 'listas.py'
listas = open(archivo)
# lineas = listas.readlines()   Para leer todas las lineas
# for l in lineas:
#     pprint(l)

# listas.close()

# pprint(lineas)

for linea in listas:   # Para leer linea por linea
    pprint(linea)

listas.close()