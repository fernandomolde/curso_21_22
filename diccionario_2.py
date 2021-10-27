from pprint import pp, pprint

variable = [('campo1','valor1'),
            ('campo2','valor2'),                #Crea un diccionario
            ('campo3','valor3'),
            ('campo4','valor4'),
            ('campo5','valor5'),                #Crea un diccionario
            ('campo6','valor6')]


dic = dict(variable)
pprint(dic.items())

# for k in dic:
#     print(dic[k])

for k,v in dic.items():
    print(k,v)

claves = dic.keys()
valores = dic.values()
pprint(claves)
pprint(valores)

for i in claves:
    print(i)
    
