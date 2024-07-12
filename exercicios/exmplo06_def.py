def montar_tabela():
    preco_por_item = 1.99
    print("Loja Quase Dois - Tabela de Preço")
    for quantidade in range(1, 51):
        total = quantidade * preco_por_item
        print(f"{quantidade} - R$ {total:.2f}")

# Chamando a função para exibir a tabela
montar_tabela()



