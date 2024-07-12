def calcular_media(*args):
    if not args:
        return 0
    soma = sum(args)
    quantidade = len(args)
    media = soma / quantidade
    return media

# Exemplo de uso da função:
media = calcular_media(1.5, 2.5, 3.5, 4.5)
print(f"A média dos argumentos é: {media}")
