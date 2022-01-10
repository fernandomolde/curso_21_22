import os
os.system('clear')

"""
Son funciones que admiten funciones como parámetros
y devuelven funciones
"""
def mi_decorador(funcion_a_decorar):
    def envoltorio(*args,**kwargs):
        print('------------ Empiezo a Decorar')
        c = funcion_a_decorar(*args,**kwargs)
        print(c)
        print('-------------Fin de la decoración')
        
        return c
    return envoltorio
    
@mi_decorador
def saludar():
    print('Hola Mundo!!')


def decora_sumar(funcion_que_suma):
    def identifica(*args):
        if not type(args) == tuple:
            lista = tuple(args)
            return funcion_que_suma(lista)
        else:
            return funcion_que_suma(args)
    return identifica
    

#saludar()

# resp = mi_decorador(saludar)
# resp()
@decora_sumar
def sumar(*args):
    return sum(args)

# def restar(a,b):
#     return a - b

print(sumar([1,2,3,4,5,6]))
