def funcion(p1,p2,p3=0, *args, **kwargs):
    print(p1,p2,p3)
    print(args)
    print(kwargs)


funcion(1,2,3,4,5,6,7,7,nombre = 'teo', dia='viernes')