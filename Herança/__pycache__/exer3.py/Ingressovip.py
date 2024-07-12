from Ingresso import Ingresso

class Ingressovip(Ingresso):
    def __init__(self,preco,setor,camarote,open_bar,open_food,estacionamento):
        super().__init__(preco,setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento= estacionamento

    def pegar_bebida(self):
        if self.open_bar:
            return f"{self.mostrar_setor()}- Bebida gratuita disponivel."
    
    def acessar_camarote(self):
        if self.camarote:
            return f"{self.mostrar_setor()}- Acesso ao camarote garantido."
        return f"{self.mostrar_setor} sem acesso ao camarote."
    
    def __str__(self):
        return (f'{super().__str__()}, Camarote: {"Sim" if self.camarote else "Não"}, '
                f'Open Bar: {"Sim" if self.open_bar else "Não"}, '
                f'Open Food: {"Sim" if self.open_food else "Não"}, '
                f'Estacionamento: {"Sim" if self.estacionamento else "Não"}')