import json
from gramatica import Gramatica
from produccion import Produccion  

# Cargar el JSON
with open('gramatica.json') as json_file:
    datos = json.load(json_file)
    
producciones = []

for produccion in datos['producciones']:
    produccion = Produccion(produccion['simbolo'], produccion['produce'])
    producciones.append(produccion)

# Crear una instancia de Gramatica con los datos cargados del JSON
gramatica = Gramatica(datos['terminales'], datos['noTerminales'], datos['producciones'], datos['inicial'])

# Mostrar la información de la gramática
print(producciones)
print("Gramática:")
print(gramatica)