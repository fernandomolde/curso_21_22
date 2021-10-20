# lista = [1,2,3,4,5,6,7,8,9,0]

# personas = ['Fernando', 'Alan', 'Jose']

# nueva_lista = lista + personas



# for x in nueva_lista:
#         print(x)

# ceros = [0] * 5
# x=ceros[2]
# print(x)
# print(ceros)

# numeros = [0,1,2,3,4,5,6,7,8,9,]
# print(numeros[::-1])
# total = 0
# v1 = [1,2]
# v2 = [7,8]

# for x in range(len(v1)):
#     total += v1[x] * v2[x]

# print(total)

origen = [1,2,3,4,5, 'Jose', 'Alan', 'Fernando']
numeros = []
alumnos = []

for x in origen:
    if type(x) == str:
        alumnos.append(x)
    else:
        numeros.append(x)
print(origen)
print(alumnos)
print(numeros)


    