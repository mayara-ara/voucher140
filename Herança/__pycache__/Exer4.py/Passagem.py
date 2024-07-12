class Passagem:
    def __init__(self,preco,assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self,novo_preco):
        self.preco = novo_preco

    def escolher_assento(self,novo_assento):
        self.assento = novo_assento

    def __str__(self):
        return f"Preço :{self.preco},Assento {self.assento}"