class Produccion:
    def init (self, simbolo):
        self.simbolo = simbolo
        self.produccion = []
        
    def str (self):
        return self.simbolo + " -> " + self.produccion