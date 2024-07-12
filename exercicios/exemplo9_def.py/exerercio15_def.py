#args(cria valores e salva em tuplas)
#kwargs(cria valores e salva no dicionario)
def media(*args):
    if not args:
        return 0
    soma = sum(args)
    quantidade = len(args)
    return soma / quantidade

result = media(1.5, 2.5, 3.5)
print(f"A média é: {result}")
print(type(result))
