from num_20_metodo_estatico import calificaciones
import unittest as ut

class TestCalificaciones(ut.TestCase):
    def test_existencia(self):
        cal = calificaciones()
        self.assertNotEqual(cal,None)
    
    def test_constructor_vacio_propiedades_vacias(self):
        cal = calificaciones()
        self.assertEqual(cal.alumno,'')
        self.assertEqual(cal.notas,[])


    def test_constructor_recibe_valores_establece_props(self):
        cal = calificaciones(['Raul',9.2,5,4.5,7.9,1])
        self.assertEqual(cal.alumno,'Raul')
        self.assertEqual(cal.notas,[9.2,5,4.5,7.9,1])

    def test_metodo_str_devuelve_alumno_calificaciones(self):
        cal = calificaciones(['Raul',9.2,5,4.5,7.9,1])
        cadena = cal.__str__()
        self.assertEqual(cadena,'Alumno: Raul tiene la calificación bien')

    def test_calcula_calificacion_vacio_devuelve_None(self):
        cal = calificaciones()
        self.assertEqual(cal.calcula_calificacion(),None)
    

    def test_calcula_calificacion_vacio_devuelve_calificacion(self):
        cal = calificaciones(['Raul',9.2,5,4.5,7.9,1])
        self.assertEqual(cal.calcula_calificacion(),'bien')
        self.assertEqual(cal.calificacion,'bien')
    
    
    def test_asigna_valores_alumno_nulo(self):
        cal = calificaciones()
        cal.nombre = 'Paco'
        self.assertEqual(cal.nombre,'Paco')
    
    def test_validar_notas_incorrectas(self):
        lista_notas = [1,22]
        self.assertEqual(calificaciones.valida_notas(lista_notas),False)

    def test_validar_notas_incorrectas_cadena(self):
        lista_notas = [1,'hola']
        self.assertEqual(calificaciones.valida_notas(lista_notas),False)

    def test_validar_notas_correctas(self):
        lista_notas = [5,6.2,7,8,9,10]
        self.assertEqual(calificaciones.valida_notas(lista_notas),True)