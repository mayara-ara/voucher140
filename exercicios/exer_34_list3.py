# Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e 
#escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a 
#segunda tabela).
#PREÇO ANTIGO PERCENTUAL DE AUMENTO
#até R$ 50 5%
#entre R$ 50 e R$ 100 10%
#acima de R$ 100 15

preco_antigo=float(input("digite o preço antigo do produto: "))
if preco_antigo <= 50:
    percentual_aumento=0.05
elif preco_antigo <= 100:
    percentual_aumento= 0.10
else:
    percentual_aumento= 0.15

preco_novo=preco_antigo * (1 + percentual_aumento)
if preco_novo <= 80:
    mensagem="Barrato!"
elif preco_novo <= 115:
    mensagem="Normal!"
else:
    mensagem="Caro!"
print("o preço novo do produto é: R$",preco_novo)
print("mensagem: ",mensagem)