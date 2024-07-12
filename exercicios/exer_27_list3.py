print("Escolha a opção:")
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")

opcao = input("Digite o número da opção desejada: ")

if opcao == "1":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("A soma é:", num1 + num2)
elif opcao == "2":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    diferenca = abs(num1 - num2)
    print("A diferença é:", diferenca)
elif opcao == "3":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("O produto é:", num1 * num2)
elif opcao == "4":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número (diferente de zero): "))
    if num2 != 0:
        print("A divisão é:", num1 / num2)
    else:
        print("Erro: O denominador não pode ser zero.")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")