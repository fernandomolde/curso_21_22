import os
import pprint

class Coche():
    matricula = None
    numero_de_puertas = None
    color = None
    motor_en_marcha = False

    def __init__(self,matricula, numero_puertas, color):    #Metodo
        self.matricula = matricula
        self.numero_de_puertas = numero_puertas
        self.color = color
        

    def __str__(self):                   #Metodo
        return f'Matricula : {self.matricula}\nNúmero de puertas: {self.numero_de_puertas}\nColor: {self.color}'
    
    def arrancar(self):
        self.motor_en_marcha = True
    def parar(self):
        self.motor_en_marcha = False

os.system('clear')
bmw = Coche('9090-KKK',3,'Azul')
print(bmw)
bmw.arrancar()
print('Motor : ',bmw.motor_en_marcha)

bmw.color = 'Verde'
bmw.matricula = '1234-llk'
bmw.numero_de_puertas = 4
bmw.precio = 20000
bmw.marca = 'BMW'
bmw.modelo = 'Panda'

print(bmw.color)
print(bmw.numero_de_puertas)
print(bmw.matricula)
print(bmw.precio)
# pprint.pprint(dir(bmw))
# pprint.pprint(bmw.__class__)
# pprint.pprint(bmw.__dict__)
print(bmw)
bmw.parar()
print('Motor :',bmw.motor_en_marcha)
