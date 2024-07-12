#####exercicio 37 da lista 3#####
custo_fabrica=int(input("digite o custo da fabrica do carro: "))

if custo_fabrica <=12000:
    comissao_distribuidor_percentual = 5
    imposto_percentual = 0
elif custo_fabrica <= 25000:
    comissao_distribuidor_percentual = 10
    imposto_percentual = 15
else:
    comissao_distribuidor_percentual = 15
    imposto_percentual = 20

comissao_distribuidor = custo_fabrica * comissao_distribuidor_percentual / 100
imposto = custo_fabrica + comissao_distribuidor / 100

custo_ao_consumidor = custo_fabrica +comissao_distribuidor + imposto
print("o custo do consumidor é: ",custo_ao_consumidor)
