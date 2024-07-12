class Professor:
    def __init__(self, nome, idade, cpf, matricula):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.matricula = matricula

    def hello(self):
        print(f"Olá, melhor professor {self.nome}")

    def mostrarDados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"Matrícula: {self.matricula}")

professor = Professor("Thiago", 35, 45612314523, 12335)

professor.mostrarDados()
professor.hello()
