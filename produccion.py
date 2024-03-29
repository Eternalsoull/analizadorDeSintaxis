class Produccion:
    def __init__ (self, simbolo, produccion):
        self.simbolo = simbolo
        self.produccion = produccion
    
    def __str__(self):
        return self.simbolo + " -> " + self.produccion
            
    def es_recursiva_izquierda(self):
        #si la produccion es de la forma A -> A...
        if self.simbolo == self.produccion[0]:
            return True
        else:
            return False