######exercicio 34#####
preco=float(input("digite o valor: "))
if preco <= 50:
    novo_preco=preco + (preco+ 0.05)
elif preco > 50 and preco <=100:
    novo_preco=preco + (preco * 0.10)
else:
    novo_preco=preco + (preco * 0.15)
print(novo_preco)
