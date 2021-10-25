def limpiar(cadena):
    aux = cadena
    aux = aux.replace(" ","")
    aux = aux.replace(".","")
    aux = aux.replace(",","")
    aux = aux.replace(":","")
    aux = aux.replace("á","a")
    aux = aux.replace("é","e")
    aux = aux.replace("í","i")
    aux = aux.replace("ó","o")
    aux = aux.replace("ú","u")
    return aux


def palindromo(cadena):
    aux = limpiar(cadena)
    return aux == aux[::-1]



    print(palindromo('ana'))
    print(palindromo('sometamos o matemos'))




