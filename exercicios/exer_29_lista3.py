####exercicio 29 da lista 3######
ano = int(input("Digite um ano: "))

if ano % 400 == 0:
    print(f"{ano} é um ano bissexto.")
elif ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")