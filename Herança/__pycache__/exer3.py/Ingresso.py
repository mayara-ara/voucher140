class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self,novo_preco):
        self.preco = novo_preco

    def mostrar_setor(self):
        return f"setor: {self.setor}"
    
    def __str__(self) -> str:
        return f"Preço: R${self.preco: .2f},setor: {self.setor}"