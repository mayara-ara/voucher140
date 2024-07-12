###EXERCICIO NÚMERO 40#####
salario_base = float(input("Informe o salário base: "))
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_final = salario_base + gratificacao - imposto
print(f"\n O salário base de ", {salario_base}, "equivale a salário final de",{salario_final})
