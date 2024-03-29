class Produccion:
    def __init__ (self, simbolo, produccion):
        self.simbolo = simbolo
        self.produccion = produccion
    
    def __str__(self):
        return "Simbolo: " + str(self.simbolo) + " -> " + "Produccion: " + str(self.produccion)
                    
    def es_recursiva_izquierda(self):
        for prod in self.produccion:
            if prod.startswith(self.simbolo):
                return True
        return False
    