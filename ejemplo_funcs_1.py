def doble(numero):
    if type(numero) in [int,float,complex]:
        return numero * 2
    else:
            return None    
    
    # if type(numero) == int:
    #     return numero * 2
    
    
    # elif type(numero) == float:
    #     return numero * 2   
    # elif type(numero) == complex:
    #     return numero *2
    # else:
    #     return None


print(doble(3)) 
print(doble('jojoj'))
print(doble(2+8j))