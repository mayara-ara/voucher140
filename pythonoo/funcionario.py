class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = float(horas_trabalhadas)  
        self.valor_hora = float(valor_hora)  

    def nome_completo(self):
        print(f"Nome completo: {self.nome} {self.sobrenome}")

    def calcular_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"Salário: R${salario:.2f}")

    def incrementar_horas(self, horas):
        if horas > 0:
            self.horas_trabalhadas += horas
            print(f"Horas trabalhadas incrementadas em {horas} horas.")
        else:
            print("O valor de horas deve ser positivo.")


funcionario = Funcionario("Lidia", "Santos", 120, 15)

funcionario.nome_completo()

funcionario.calcular_salario()

funcionario.incrementar_horas(10)

funcionario.calcular_salario()
