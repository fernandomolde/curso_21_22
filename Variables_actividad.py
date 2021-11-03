PRECIO_SEMANA = 100 
PRECIO_DIA = 42
DIAS = 7

def parking(dias):
    #1.- Calcular las semanas
    semanas = dias//DIAS
    #2.- Calcular los dias restantes
    dias_restantes = dias % DIAS
    #3.- Coste por semanas
    coste_semanal = semanas * PRECIO_SEMANA
    #4.- Coste por dias
    coste_dias = dias_restantes * PRECIO_DIA
    #5.- Cáculo del total
    total = coste_dias + coste_semanal

    return total

print(parking(1)) 
     
        






