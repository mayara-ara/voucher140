#####exerccio 28 da lista 3#####
idade = int(input("Digite a idade do trabalhador: "))
tempo_de_servico = int(input("Digite o tempo de serviço do trabalhador em anos: "))

if idade >= 65 or tempo_de_servico >= 30 or (idade >= 60 and tempo_de_servico >= 25):
    print("O trabalhador pode se aposentar.")
else:
    print("O trabalhador ainda não pode se aposentar.")

