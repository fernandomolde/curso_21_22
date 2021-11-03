
#1.- Pedir el input de la fecha de nacimiento


#2.- Dividir la fecha en dd,mm,aaa

#3.- Componer el mensaje de salida

def fecha_nacimiento():
    meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Noviembre','Diciembre']
    fecha = input('Dime cuando naciste (dd/mm/aaaa): ')
    partes = fecha.split('/')
    mes  = int(partes[1]) - 1
    mensaje = ' Naciste el dia ' + partes[0] + ' del mes ' + meses[mes] + ' del año ' + partes[2]
    return mensaje
    

print(fecha_nacimiento())

def fecha_nacimiento_2 ():
    meses = { 1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre', 12:'Diciembre' }
    fecha = input('Dime cuando naciste (dd/mm/aaaa): ')
    partes = fecha.split('/')
    mes  = int(partes[1]) - 1
    mensaje = ' Naciste el dia ' + partes[0] + ' del mes ' + meses[mes] + ' del año ' + partes[2]
    return mensaje

print(fecha_nacimiento_2())