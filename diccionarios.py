# diccionario = {
#     'nombre': 'Fernando', 
#     'apellido1': 'Lopez',
#     'notas': [1,2,3,4,5]
# }

# diccionario['apellido2'] = 'Garcia'  # para añadir elementos al diccionario y tambien sirve para modificar.
# diccionario['apellido1'] = 'López'

# print(type(diccionario))
# print(diccionario['nombre'])
# print(diccionario['apellido1'])
# print(f"Nombre completo: {diccionario['nombre']} {diccionario['apellido1']}")



import pprint
vscode = {
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Archivo actual",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
vscode['configurations'][0]['type'] = 'Manolito'

pprint.pprint(vscode)