"""
Son funciones que admiten funciones como parámetros
y devuelven funciones
"""
def mi_decorador(funcion_a_decorar):
    def envoltorio():
        print('------------ Empiezo a Decorar')
        c = funcion_a_decorar()
        print('-------------Fin de la decoración')

    return envoltorio
    
@mi_decorador
def saludar():
    print('Hola Mundo!!')

saludar()

# resp = mi_decorador(saludar)
# resp()

# def sumar(a,b):
#     return a + b

# def restar(a,b):
#     return a - b