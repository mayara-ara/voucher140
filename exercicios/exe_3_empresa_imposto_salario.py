####exercicio número 17 lista 3####
valor_hora = 40.50
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))

salario_bruto = valor_hora * horas_trabalhadas
if salario_bruto > 2500:
    excedente = salario_bruto - 2500
    imposto_renda = excedente * 0.11
else:
    imposto_renda = 0
salario_liquido = salario_bruto - imposto_renda

print("O salário líquido é R$", salario_liquido)
 