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
    coro =[Gorrion(),Gallo()]
    def cantar(self):
        for p in self.coro:
            p.cantar()


c = CoroPajaros()
c.cantar()


