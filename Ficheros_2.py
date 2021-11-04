import os 
os.system('clear')

ruta = os .getcwd()         #Carpeta de trabajo actual
print(ruta)


# with open('listas.py') as arch:
#     l = arch.read()
#     print(l)


contenido = os.scandir(ruta)            # Te escanea una carpeta
for f in contenido:
    print(f.name)