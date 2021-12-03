import fractions
import os


class Racional():
    numerador = float
    denominador = float

    def __init__(self,numerador,denominador):
        self.numerador = float(numerador)
        if denominador == 0:
            raise Exception('El denominador no puede ser 0')
        self.denominador = float(denominador)
 
    def maximo_comun_divisor(self,a,b):
        temporal = 0
        while b !=0:
            temporal = b
            b = a % b
            a = temporal
        return a

    def minimo_comun_multiplo(self,a,b):
        return (a* b) / self.maximo_comun_divisor(a,b)

    
    def suma(self):
        dividendo_1 = float (input ('Ingresa el valor de dividendo 1: '))
        dividendo_2 = float (input ('Ingresa el valor de dividendo 2: '))
        divisor_1 = float (input ('Ingresa el valor de divisor 1: '))
        divisor_2 = float (input ('Ingresa el valor de divisor 2: '))
        resultado=(divisor_1*dividendo_2+divisor_2*dividendo_1)/dividendo_2/dividendo_1
        print ('Valor de resultado: ' + repr (resultado))
        print ()
        os.system ('pause')

    def restar(self,otra,Fraccion):
        mcm = self.minimo_comun_multiplo(self.denominador, otra.denominador)
        diferencia_self = mcm/self.denominador
        diferencia_otra = mcm/self.denominador
        numerador_resultado = (diferencia_self*self.numerador) - \
        (diferencia_otra*self.numerador)
        return Fraccion(numerador_resultado, mcm)
       

    def multiplicar(self,otra,Fraccion):
          return Fraccion(self.numerador*otra.numerador, self.denominador*otra.denominador)
  

    def dividir(self):

        pass
    
    def imprima(self):
        print('El denominador es:')
        print('El numerador es:')




f = Racional()
print(f.suma())











    









# Constructor que admita numerador y denominador
# Constructor sin parámetros
# Metodos Getters y setters
# Metodos Suma,Resta,Multiplicación y División 