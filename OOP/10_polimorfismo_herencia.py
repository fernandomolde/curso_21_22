class Pajaro():
    def cantar(self):
        print('Los pájaros tienen cantos diferentes')

class Gorrion(Pajaro):
    def cantar(self, con_padre = False):
        if con_padre:
            super().cantar()
        print('Gorrión pio,pio')
    
class Gallo(Pajaro):
    def cantar(self, con_padre = False):
        if con_padre:
            super().cantar()
        print('Gallo kikirikiii')
    

# g = Gorrion()
# g.cantar()

# gallo = Gallo()
# gallo.cantar()

class CoroPajaros():

    def __init__(self,lista_pajaros) -> None:
        self.coro = lista_pajaros
    def cantar(self):
        titulo = True
        for p in self.coro:
            p.cantar(titulo)
            titulo = False

lista_pajaros = ['p',1,'l']     #[Gallo(),Gallo(),Gorrion()]
c = CoroPajaros(lista_pajaros)
c.cantar()


