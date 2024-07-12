import math

class Circulo:
    def __init__(self,raio):
        self.raio = raio
    def imprimir_raio(self):
        print(f"Raio: {self.raio}")

    def calcula_area(self):
        area = math.pi * (self.raio **2)
        print(f"Área do circulo{area: .2f}")
        return area
    
    def calculo_circuferencia(self):
        circuferencia = 2 * math .pi * self.raio
        print(f"circuferencia do circulo{circuferencia: .2f}")
        return circuferencia
circuferencia= Circulo(5)
circuferencia.imprimir_raio()
circuferencia.calcula_area()
circuferencia.calculo_circuferencia()
