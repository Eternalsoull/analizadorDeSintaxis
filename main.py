import json
from gramatica import Gramatica
from produccion import Produccion  

# Cargar el JSON
with open('gramatica.json') as json_file:
    datos = json.load(json_file)
    
producciones = []
nuevas_producciones = []

for produccion in datos['producciones']:
    produccion = Produccion(produccion['simbolo'], produccion['produce'])
    producciones.append(produccion)
    
gramatica = Gramatica(datos['terminales'], datos['noTerminales'], datos['producciones'], datos['inicial'])

print("Gramática antes:")
print(gramatica)

# miramos las producciones para verificar si hay recursividad a la izquierda
#si hay al menos una produccion recursiva a la izquierda, entonces eliminamos la recursividad
if any(produccion.es_recursiva_izquierda() for produccion in producciones):
    nuevas_producciones= gramatica.eliminar_recursion_izquierda(producciones)

# Actualizar las producciones de la gramática


# Crear una instancia de Gramatica con los datos cargados del JSON

# Mostrar la información de la gramática
print("Producciones antes:")
for produccion in producciones:
    print(produccion)
print("Producciones después:")
for produccion in nuevas_producciones:
    print(produccion)
print(nuevas_producciones)
print("Gramática después:")
print(gramatica)