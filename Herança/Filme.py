##super class##
class Filme:
    def __init__(self,nome,duracao):
        self._nome =nome
        self.__duracao =duracao

    def setNome(self,novo_nome):
        self._nome = novo_nome

    def getNome(self):
        return self._nome
    
    def play(self):
        print(f"{self._nome} começou.....")

    def getDuracao(self):
        return self.__duracao
    

###subclass
class Drama(Filme):
    def __init__(self, nome, duracao,ator):
        super().__init__(nome, duracao)
        self.ator = ator

    def play(self):
        print(f"{self._nome} começou a chorar....")

class Acao(Filme):
    def __init__(self, nome, duracao,explosivos):
        super().__init__(nome, duracao,)
        self.explosivos = explosivos 

    def play(self):
        print(f" {self._nome}começou a explodir....")

    