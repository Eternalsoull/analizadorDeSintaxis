import json
class Gramatica:
    def _init_(self, terminales, noTerminales, producciones, inicial):
        self.terminales = terminales
        self.noTerminales = noTerminales
        self.producciones = producciones
        self.inicial = inicial
        
    def _str_(self):
        return "Terminales: " + str(self.terminales) + "\nNo terminales: " + str(self.noTerminales) + "\nProducciones: " + str(self.producciones) + "\nInicial: " + str(self.inicial)
    
    def _repr_(self):
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
        
