loja={
    "calça": 150,
    "camisa": 150,
    "sapato": 150,
    "short":  150

}
produto=input("digite o nome do produto ")
if produto in loja:
   print(f"a contidade disponivel no estoque é {loja[produto]}unidade.")
else:
    print("não esta disponivel no estoque.")

texto = input("Digite um texto: ")

palavras = texto.split()

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print("A contagem de palavras é:", contagem_palavras)


