import os
import pprint

class telefono():
    marca = None
    modelo = None
    Color = None
    Peso = None
    Sistema_op = None
    Camara = None

    def encender(self):
        pass

    def apagar(self):
        pass

    def reiniciar(self):
        self.apagar()
        self.encender()

    def modo_avion(self):
        pass

    def llamar(self):
        pass

    def recibir_llamadas(self):
        pass

os.system('clear')
tele = telefono
tele.Color = 'Azul'
tele.marca = 'Xiami'
tele.Peso = '3,4Kg'
tele.Sistema_op = 'Android'
tele.modelo = 'Xiami 11'
tele.Camara = ''
print(tele.Color)
print(tele.marca)
print(tele.Peso)
print(tele.Sistema_op)
print(tele.modelo)