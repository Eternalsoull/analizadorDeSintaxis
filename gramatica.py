from produccion import Produccion
class Gramatica:
    def __init__(self, terminales, noTerminales, producciones, inicial):
        self.terminales = terminales
        self.noTerminales = noTerminales
        self.producciones = producciones
        self.inicial = inicial
        
        
        
    def __str__(self):
        return "Terminales: " + str(self.terminales) + "\nNo terminales: " + str(self.noTerminales) + "\nProducciones: " + str(self.producciones) + "\nInicial: " + str(self.inicial)
    
    def __repr__(self):
        return self._str_()
    
    def verificarPalabra(self, palabra):
        return self.verificarPalabraRecursivo(palabra, self.inicial)
    
    
    
    def verificarPalabraRecursivo(self, palabra, simbolo):
        # si la palabra esta vacia, entonces el simbolo debe ser no term
        if len(palabra) == 0:
            return simbolo in self.noTerminales
        else:
            # recorrer las producciones
            for produccion in self.producciones:
                # si el simbolo de la produccion es el simbolo actual
                if produccion.simbolo == simbolo:
                    # si el primer caracter de la palabra es terminal
                    if palabra[0] in self.terminales:   
                        # si el primer caracter de la produccion es el primer caracter de la palabra
                        if produccion.produccion[0] == palabra[0]:
                            return self.verificarPalabraRecursivo(palabra[1:], produccion.produccion)
                    else:
                        if self.verificarPalabraRecursivo(palabra, produccion.produccion):
                            return True
            return False
    
    
    def eliminar_recursion_izquierda(self, producciones):
        nuevas_producciones = []
        producciones_recursivas = []
        producciones_no_recursivas = []
        simbolos_recursiva = []
        for produccion in producciones:
            if produccion.es_recursiva_izquierda():
                producciones_recursivas.append(produccion)
            else:
                producciones_no_recursivas.append(produccion)
                
        simbolo_recursiva = ''
        for produccion_recursiva in producciones_recursivas:
            simbolos_recursiva.append(produccion_recursiva.simbolo)
            simbolo_recursiva = produccion_recursiva.simbolo
            simbolo_nuevo = simbolo_recursiva + "'"
            self.noTerminales.append(simbolo_nuevo)
            # guardo el simbolo que se va a reemplazar para buscarlo en las producciones no recursivas
            for produccion_no_recursiva in producciones_no_recursivas:
                if produccion_no_recursiva.simbolo == simbolo_recursiva:
                    
                    alfa = produccion_recursiva.produccion[1:]
                    beta = produccion_no_recursiva.produccion
                    nuevaProduccion1= Produccion(simbolo_recursiva, beta + simbolo_nuevo)
                    nuevaProduccion2= Produccion(simbolo_nuevo, alfa + simbolo_nuevo)
                    nuevaProduccion3= Produccion(simbolo_nuevo, 'λ')
                    nuevas_producciones.append(nuevaProduccion1)
                    nuevas_producciones.append(nuevaProduccion2)
                    nuevas_producciones.append(nuevaProduccion3)     
            else:
                nuevas_producciones.append(produccion)    
        
        self.producciones = nuevas_producciones
        print("Simbolos recursivos: ", simbolos_recursiva)  
        #imprimir los no terminales
        print("No terminales: ", self.noTerminales)
        #imprimimos todas las producciones
        print("Producciones todas: " )
        for produccion in self.producciones:
            print(produccion)   
        return nuevas_producciones

