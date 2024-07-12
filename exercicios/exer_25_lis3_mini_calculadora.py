######exercicio 25 da lista 3####
print("Selecione a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

escolha = input("Digite o número da operação desejada: ")

if escolha in ('1', '2', '3', '4'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", num1 + num2)
    elif escolha == '2':
        print("Resultado:", num1 - num2)
    elif escolha == '3':
        print("Resultado:", num1 * num2)
    elif escolha == '4':
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Erro: divisão por zero!")
else:
    print("Opção inválida!")






    