class Francia():
    def __str__(self) -> str:
        return 'Francia'

    def capital(self):
        print('La capital de Francia es Paris')
    def idioma(self):
        print('El idioma oficial es el Frances')


class Portugal():

    def __str__(self) -> str:
        return 'Portugal'

    def capital(self):
        print('La capital de Portugal es Lisboa')
    def idioma(self):
        print('El idioma oficial es el Portugués')


class Aduana():
    def pasar(self,origen,destino):
        print(f'Ahora estoy en {origen}')
        print(f'Ahora estoy en {destino}')
        origen.capital()
        origen.idioma()
        print('----------------')
        destino.capital()
        destino.idioma()


fr = Francia()
por = Portugal()
paises = [fr,por]

audana = Aduana()    

audana.pasar(fr,por)
print('*****************************')
audana.pasar(por,fr)
print('******************************')