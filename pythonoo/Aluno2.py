class Aluno:
    def __init__(self, nome, ra, notas):
        self.nome = nome
        self.ra = ra
        self.notas = notas

    def mostrarSituacao(self):
        media = sum(self.notas) / len(self.notas)
        if media < 5:
            return "Reprovado"
        elif media >= 5 and media <= 6.9:
            return "Exame"
        else:
            return "Aprovado"

notas = []
nome = input("Digite o nome do caboco: ")
ra = int(input("Digite o ra do caboco: "))

i = 0
while i < 4:
    nota = float(input('Digite a nota do caboco: '))
    notas.append(nota)  
    i += 1

a = Aluno(nome, ra, notas)
print(a.mostrarSituacao())
