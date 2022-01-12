def sumar(*args):
    lista = []
    # for i in range(len(args)):  
    #     if i == str:
    #             print(i)
    #     else:
    #         lista.append(i)
    #         return sumar
    for i in args:
        for elem in i.split(','):
            if elem.isdigit():
                lista.append(int(elem))
    for i in lista:
        print(i)

sumar('1,2,3,4')