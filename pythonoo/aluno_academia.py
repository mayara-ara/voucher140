class Aluno_academia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade
    
    def calcular_IMC(self):
        imc = self.peso / (self.altura ** 2)
        return imc
    
    def obter_valor_mensalidade(self):
        if self.idade < 18:
            return self.mensalidade * 0.9  
        else:
            return self.mensalidade

nome = input("Informe o nome do aluno: ")
idade = int(input("Informe a idade do aluno: "))
peso = float(input("Informe o peso do aluno (kg): "))
altura = float(input("Informe a altura do aluno (m): "))

aluno = Aluno_academia(nome, idade, peso, altura)

imc = aluno.calcular_IMC()
mensalidade = aluno.obter_valor_mensalidade()

print(f"Nome: {aluno.nome}")
print(f"Idade: {aluno.idade}")
print(f"Peso: {aluno.peso} kg")
print(f"Altura: {aluno.altura} m")
print(f"IMC: {imc:.2f}")
print(f"Valor da mensalidade: R$ {mensalidade:.2f}")
