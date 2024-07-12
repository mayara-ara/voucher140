from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, notas):
        super().__init__(matricula, nome, idade)
        self.notas = notas  # lista de notas
        self.media = self.calcular_media()

    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0

    def estudar(self):
        return f'{self.nome} está estudando.'

    def __str__(self):
        return f'{super().__str__()}, Notas: {self.notas}, Média: {self.media:.2f}'
