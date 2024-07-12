from Passagem import Passagem

class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print("O ônibus está sendo abastecido.")

    def __str__(self):
        return (super().__str__() + 
                f", Placa: {self.placa}, Leito: {self.leito}")

