from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade,formacao,disciplina,cargohora,salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.cargo = cargohora
        self.sal = salario

    def lecionar(self):
        return f"o melhor prof.{self.nome} acordou inpirado para lecionar"