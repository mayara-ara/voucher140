class Estudante:
    def __init__(self, matricula, nome, idade, nota):  # método construtor
        self.matricula = matricula  # atributo
        self.nome = nome  # atributo
        self.idade = idade  # atributo
        self.nota = nota  # atributo

    def hello(self):  # método
        print(f"olá {self.nome}")


aluno = Estudante(1212, "Pedro", 18, 80)
print(aluno.nome)
aluno2 = Estudante(1313,"Domitila",22,90)
print(aluno2.nome)

aluno2.hello()
