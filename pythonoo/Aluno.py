class Aluno:
    def __init__(self,nome,ra,n1,n2,n3,n4):
        self.nome = nome
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4

    def mostrarSituacao(self):
        media = (self.n1 + self.n2 + self.n3 + self.n4 ) / 4

        if media < 5:
            return "Reprovado"
        elif media >=5 and media <=6.9:
            return "Exame"
        else:
            return "Aprovado"
        

aluno1 = Aluno("wendril ",1122,7.8,8.5,8.9,9.5)

print(aluno1.nome, aluno1.mostrarSituacao())
        