d = { 

}

frase = 'Una tarde,Una mañana'
inicio = 0
trozo = ''
numero_coma = frase.count(',') +1
for i in range(numero_coma):
        frase.replace(',',' ')
        final = frase.find(',',inicio) 
        print(numero_coma)
        print(final)