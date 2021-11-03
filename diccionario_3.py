from typing import ItemsView, Iterable


d1 = dict ([('campo1','valor1'),
            ('campo2','valor2'),               
            ('campo3','valor3'),
            ('campo4','valor4'),
            ('campo5','valor5'),                
            ('campo6','valor6')])

d1['fruta'] = ['manzana','pera','uva']
v1 = d1['fruta']
v1.append('platano')
v1.append('sandia')
d1['fruta'] = v1


print(d1['fruta'])
print(d1)

#Borrar elemento

del(d1['campo1'])
print(d1)

# Obtener todas las claves

claves = d1.keys()
print(claves)

# Obtener todos los valores
valores = d1.values()
print(valores)

# Iterar sobre un diccionario

for k in d1:
    print(d1[k])


for k,v in d1.Items():
    print(f'clave: {k} valor: {v}')

# Limpiar en diccionario

d1.clear()
print(d1)

# Elementos del diccionario
print(d1.items())

# Extraer elementos del diccionario
# elem = d1.pop('fruta')
d1['ultimo'] = 'FIN'
elem = d1.popitem()
print(elem)
print(d1)
