from typing import List


lista13 = (22,34,12,56)
lista34 = (22,34,12,56) 
iguales = False


if len(lista13) == len(lista34):    
    for i in range(len(lista13)):
        if lista13[i] == lista34[i]:
            iguales = True
        else:
            iguales: False
            break
if iguales:
    print("Son iguales")
else:
    print("No son iguales")


#-----------------------------------------


    
    
    











