"""
Crear una clase Calificaciones.
Tendrá un método init que admitira como entrada una lista de forma ['Raul',9.2,5,4.5,7.9,1]
Tendrá un método 'calificar' que nos devolvera ['Raul','Notable']

T0D0:
 - Crear lista de alumnos a partir de un archivo (CSV,Long,fija,etc)
 - Crear lista a partir de base de datos
 - Crear lista a partir de JSON

"""

# 1-Crear la clase

from num_20_metodo_estatico import NotasInvalidasError


class calificaciones():
 # 2-Metodo Init
    def __init__(self,alum_notas = []) -> None:
 
            if alum_notas:
                self.__nombre = alum_notas[0]
                self.__notas = alum_notas[1:]
                self.__calificacion = self.calcula_calificacion()
          
            else:
                self.__nombre = ''
                self.__notas = []
                self.__calificacion = []
    
    def __str__(self) -> str:
        # return f'Alumno: {self.nombre} tiene de calificacion: {self.calificacion}'
            return f'Alumno: {self.__nombre} tiene la calificación {self.__calificacion}'

    def calcula_calificacion(self):
        calificacion = ''
        
        if self.__notas:
            notas_media = sum(self.__notas)/len(self.__notas)

            if notas_media < 5 :
                calificacion = 'suspenso'
            
            elif notas_media < 7:
                calificacion = 'bien'
                
            elif notas_media < 9:
                calificacion = 'notable'
            
            else:
                calificacion = 'sobresaliente'

        else:
            calificacion = None
            
        return calificacion

    
    @property
    def alumno(self):
        return self.__nombre

    

    @alumno.setter
    def alumno(self,nuevo_alumno):
        self.__nombre = nuevo_alumno
            
    @property
    def notas(self):
        return self.__notas 
    
    @notas.setter
    def notas(self,nuevas_notas):
       try:
           if self.valida_notas(nuevas_notas):
               self.__notas = nuevas_notas
               self.__calificacion = self.calcula_calificacion()
       except NotasInvalidasError:
           pass 

    @property
    def calificacion(self):
        return self.__calificacion

    @staticmethod
    def valida_notas(lista_notas):
        valido = True
        if lista_notas == []:
            # valido =  False
            raise NotasInvalidasError('la lista de notas esta vacia')
        for nota in lista_notas:
            if not type(nota) in (int,float) or not (0.0 <= nota <=10.0):
                valido = False

        return valido