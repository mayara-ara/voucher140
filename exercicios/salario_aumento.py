####EXERCICIO NÚMERO 36#####
salario = float(input("Salario: "))
aumento = salario * 25 / 100
novo_salario = salario + aumento
desconto = novo_salario * 10 / 100
sal_com_desconto = novo_salario - desconto

print("NOVO SALARIO: ",novo_salario)
print("DESCONTO: ",desconto)
print("SALARIO LIQUIDO: ",sal_com_desconto)
