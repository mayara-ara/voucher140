#exercicio 33 da lista 3 ####

cardapio = {
    100: {"produto": "Hot Dog", "preco": 1.20},
    101: {"produto": "Bauru", "preco": 1.30},
    102: {"produto": "X-Salada", "preco": 1.50},
    103: {"produto": "X-BACON", "preco": 1.20},
    104: {"produto": "X-Burguer", "preco": 17.00},
    105: {"produto": "Suco de Laranja", "preco": 9.50},
    106: {"produto": "Refrigerante", "preco": 6.00}
}

codigo_produto = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade: "))

if codigo_produto in cardapio:
    preco_unitario = cardapio[codigo_produto]["preco"]
    valor_total = preco_unitario * quantidade
    print("Valor a ser pago pelo", cardapio[codigo_produto]["produto"], "é de R$", valor_total)
