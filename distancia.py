import math


class distancia:

    def __init__(self,x2,x1,y2,y1):
        self.x2 = x2
        self.x1 = x1
        self.y2 = y2
        self.y1 = y1

    def calcular_distancias(self):

        d = math.pow(self.x2-self.x1,2)
        s = math.pow(self.y2-self.y1,2)
        r = math.sqrt(d+s)

        return r







