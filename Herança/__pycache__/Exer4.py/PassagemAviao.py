from Passagem import Passagem

class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portao_de_embarque, checkin):
        super().__init__(preco, assento)
        self.portao_de_embarque = portao_de_embarque
        self.checkin = checkin

    def decolar(self):
        print("O avião está decolando.")

    def Chegar_checkin(self, confirmar_checkin):
        self.checkin = confirmar_checkin
        return (super().__str__() + 
                f", Portão de Embarque: {self.portao_de_embarque}, Check-in: {self.checkin}")

    def __str__(self):
        return (super().__str__() + 
                f", Portão de Embarque: {self.portao_de_embarque}, Check-in: {self.checkin}")
