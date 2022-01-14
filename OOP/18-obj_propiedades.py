from datetime import date



class Persona():
    
    def __init__(self,nombre,apellido,fecha_nacimiento) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento 

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self,nombre):
        self.__nombre = nombre


    @property  #Getter
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter #Setter
    def fecha_nacimiento(self,fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

p = Persona('teo','sanchez','1-02-2000')
print(p.fecha_nacimiento)                   #Aqui estamos llamando a un Getter

p.fecha_nacimiento = '01/01/2000'
print(p.fecha_nacimiento)                   #Aqui estamos llamando a un Setter

