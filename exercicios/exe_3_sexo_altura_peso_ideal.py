#####exercicio 19 da lista 3#####
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo homem/mulher: ")

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print("peso ideal ",peso_ideal)
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(peso_ideal)
else:
    print("Sexo não reconhecido.")




