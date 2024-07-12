import math


class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC
    
    def get_maior_lado(self):
        return max(self.ladoA,self.ladoB,self.ladoC)
    
    def calcular_area (self):
        s = self.calcular_perimetro() / 2
        area = math.sqrt(s * (s - self.ladoA)*(s - self.ladoB)*(s -self.ladoC))
        return area
    

ladoA=float(input("informe o comprimento do lado A do trinagulo: "))
ladoB=float(input("informe o comprimento do lado B do triangulo:  "))
ladoC=float(input("informe o comprimento do lado C do triangulo: "))

triangulo=Triangulo(ladoA , ladoB , ladoC)

print(f"perimetro do triangulo: {triangulo.calcular_perimetro()}")
print(f"A area do triangulo: {triangulo.calcular_area()}")
print(f"maio lado do triangulo: {triangulo.get_maior_lado()}")


