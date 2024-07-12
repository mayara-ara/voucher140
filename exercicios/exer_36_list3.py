###exercicio 36 da lista 3#####
salario_atual = float(input("Digite o salário atual do funcionário: "))
tempo_servico = int(input("Digite o tempo de serviço do funcionário em anos: "))

if salario_atual <= 1000:
    aumento_percentual = 0.2
elif salario_atual <= 3000:
    aumento_percentual = 0.15
elif salario_atual <= 5000:
    aumento_percentual = 0.1
else:
    aumento_percentual = 0.05

if tempo_servico < 1:
    bonus = 0
elif tempo_servico < 3:
    bonus = 100
elif tempo_servico < 6:
    bonus = 300
elif tempo_servico < 10:
    bonus = 500
else:
    bonus = 1000

# Calcular o aumento e o salário final reajustado
aumento = salario_atual * aumento_percentual
salario_final = salario_atual + aumento + bonus

# Verificar se o funcionário tem direito a aumento
if salario_atual <= 5000 or tempo_servico >= 1:
    print("O salário final reajustado é:", salario_final)
else:
    print("O funcionário não tem direito a nenhum aumento.")