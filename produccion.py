class Produccion:
    def init (self, simbolo, produccion):
        self.simbolo = simbolo
        self.produccion = produccion
        
    def str (self):
        return self.simbolo + " -> " + self.produccion