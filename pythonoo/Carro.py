class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,nivel=5,):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel

    def calcular_imposto(self):
        imposto = (self.valor * 2.5) /100
        return imposto

    def abastecer (self,qtdade_litros):
        self.nivel =self.nivel +  qtdade_litros

    def andar(self,km):
        consumo = km / 10.8
        self.nivel = self.nivel - consumo

    def verificar_nivel(self):
        return self.nivel


car1 = Carro("Jetta","Volks","Prata",2022,180000)
print(car1.calcular_imposto())
print("nivel de gasolina",car1.nivel,"litros")
car1.abastecer(45)
print("nivel de gasolina",car1.nivel,"litros")
car1.andar(250)
tanque = car1.verificar_nivel()
print(f"{tanque: .2f}")