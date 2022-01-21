"""
Crear una clase Calificaciones.
Tendrá un método init que admitira como entrada una lista de forma ['Raul',9.2,5,4.5,7.9,1]
Tendrá un método 'calificar' que nos devolvera ['Raul','Notable']

"""

# 1-Crear la clase
class calificaciones():
 # 2-Metodo Init
    def __init__(self,alum_notas = []) -> None:
 
            if alum_notas:
                self.nombre = alum_notas[0]
                self.notas = alum_notas[1:]
                self.calificacion = self.calcula_calificacion()
          
            else:
                self.nombre = ''
                self.notas = []
                self.calificacion = []
    
    def __str__(self) -> str:
        # return f'Alumno: {self.nombre} tiene de calificacion: {self.calificacion}'
            return f'Alumno: {self.nombre} tiene la calificación {self.calificacion}'

    def calcula_calificacion(self):
        calificacion = ''
        
        if self.notas:
            notas_media = sum(self.notas)/len(self.notas)

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



Alum_1 = calificaciones(['Raul',9.2,5,4.5,7.9,1])
print(Alum_1)