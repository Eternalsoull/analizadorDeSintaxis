import json
from gramatica import Gramatica  

# Cargar el JSON
with open('gramatica.json') as json_file:
    datos = json.load(json_file)

# Crear una instancia de Gramatica con los datos cargados del JSON
gramatica = Gramatica(datos['terminales'], datos['noTerminales'], datos['producciones'], datos['inicial'])

# Mostrar la información de la gramática
print("Gramática:")
print(gramatica)