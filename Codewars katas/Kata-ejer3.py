# https://www.codewars.com/kata/565b9d6f8139573819000056

def decode(message):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYXZ'
    inversa = alfabeto[::-1]
    salida = ''
    for letra in message:
       if letra.isalpha():
            idx = alfabeto.index(letra)
            salida += inversa[idx]
    else:
        salida +=letra
        return salida 
   

 

