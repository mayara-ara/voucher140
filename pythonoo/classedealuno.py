class Aluno:
    def __init__(self,nome,ra,nota1,nota2,nota3,nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def calcula_media(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4  

    def mostrar_situacao(self):
        media = self.calcula_media()
        if media >= 7:
            return "Aprovado"  
        elif 5 <= media < 7 :
            return "Exame"
        else:
            return "Reprovado"
        
aluno = Aluno ("maria aparecida","14562",6,5,7,8)
print(f"Aluno: {aluno.nome},ra: {aluno.ra},situação: {aluno.mostrar_situacao()}")